#!/bin/bash

# Configuration Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${REPO_DIR:-$(cd "$SCRIPT_DIR/.." && pwd)}"
CTFD_CONTAINER="${CTFD_CONTAINER:-ctfd-ctfd-1}"
HINT_COST="${HINT_COST:-1}"

echo "[1/4] Checking Git repository at $REPO_DIR..."
cd "$REPO_DIR" || exit 1

echo "[2/4] Generating Python sync payload..."
cat << 'EOF' > /tmp/update_challenges.py
import sys
sys.path.insert(0, "/opt/CTFd")

import os
import re
import shutil
import tempfile
from werkzeug.datastructures import FileStorage
from CTFd import create_app
from CTFd.models import (
    db, Challenges, Flags, Hints, ChallengeFiles, Solves, Submissions
)
from CTFd.utils.uploads import upload_file

app = create_app()

BASE_REPO = "/tmp/repo"
if os.path.exists(os.path.join(BASE_REPO, "ctfrobo")):
    BASE_REPO = os.path.join(BASE_REPO, "ctfrobo")

TIERS = [
    ("beginner", "Beginner", 5, 1),
    ("intermediate", "Intermediate", 10, 2),
    ("advanced", "Advanced", 20, 4),
]

with app.app_context():
    print("\n[1/3] Flushing old challenge data and resetting test submissions...")
    Solves.query.delete()
    Submissions.query.delete()
    
    for f in ChallengeFiles.query.all():
        disk_path = os.path.join(app.config.get("UPLOAD_FOLDER", "/var/uploads"), f.location)
        if os.path.exists(disk_path):
            try:
                os.remove(disk_path)
            except Exception:
                pass
        db.session.delete(f)

    Hints.query.delete()
    Flags.query.delete()
    Challenges.query.delete()
    db.session.commit()
    print("[✔] Challenge records cleared. User accounts preserved.")

    print("\n[2/3] Parsing and deploying updated questions...")
    total_added = 0

    for tier_folder, category_name, points, hint_cost in TIERS:
        tier_path = os.path.join(BASE_REPO, tier_folder)
        if not os.path.exists(tier_path):
            continue

        for chal_dir_name in sorted(os.listdir(tier_path)):
            chal_dir = os.path.join(tier_path, chal_dir_name)
            if not os.path.isdir(chal_dir):
                continue

            if "-" in chal_dir_name:
                code, rest = chal_dir_name.split("-", 1)
                display_name = f"{code.upper()}: {rest.replace('-', ' ').title()}"
            else:
                display_name = chal_dir_name

            readme_file = os.path.join(chal_dir, "README.md")
            flag_file = os.path.join(chal_dir, "answer.txt")
            hints_file = os.path.join(chal_dir, "hints.md")
            dist_dir = os.path.join(chal_dir, "challenge")

            if not os.path.exists(readme_file) or not os.path.exists(flag_file):
                continue

            with open(readme_file, "r", encoding="utf-8", errors="ignore") as f:
                description = f.read().strip()

            with open(flag_file, "r", encoding="utf-8", errors="ignore") as f:
                flag_val = f.read().strip().strip('"').strip("'")

            chal = Challenges(
                name=display_name,
                category=category_name,
                description=description,
                value=points,
                state="visible",
                type="standard"
            )
            db.session.add(chal)
            db.session.commit()

            flag = Flags(
                challenge_id=chal.id,
                type="static",
                content=flag_val
            )
            db.session.add(flag)
            db.session.commit()

            if os.path.exists(hints_file):
                with open(hints_file, "r", encoding="utf-8", errors="ignore") as f:
                    hints_content = f.read().strip()
                if hints_content:
                    # Parse separate hints and apply deduction cost
                    sections = re.split(r"(?m)^###?\s*Hint\s*\d+", hints_content)
                    parsed_hints = [s.strip() for s in sections[1:] if s.strip()]
                    if not parsed_hints:
                        # Fallback for bullet list or raw text
                        parsed_hints = [hints_content]
                    
                    for h_text in parsed_hints:
                        hint = Hints(challenge_id=chal.id, content=h_text, cost=hint_cost)
                        db.session.add(hint)
                    db.session.commit()

            if os.path.exists(dist_dir) and os.path.isdir(dist_dir):
                for item in os.listdir(dist_dir):
                    if item.startswith(".") or item == "README.md":
                        continue
                    
                    item_path = os.path.join(dist_dir, item)

                    if os.path.isdir(item_path):
                        zip_name = f"{item}.zip"
                        with tempfile.TemporaryDirectory() as tmp_dir:
                            zip_base = os.path.join(tmp_dir, item)
                            archive_path = shutil.make_archive(zip_base, "zip", item_path)
                            with open(archive_path, "rb") as fp:
                                fs = FileStorage(stream=fp, filename=zip_name)
                                upload_file(file=fs, challenge_id=chal.id, type="challenge")
                        print(f"    [+] Packaged directory: {zip_name} -> {display_name}")

                    elif os.path.isfile(item_path):
                        if item.lower() in ["final_flag.txt", "page.txt"]:
                            print(f"    [!] Blocked leak artifact: {item} in {display_name}")
                            continue

                        with open(item_path, "rb") as fp:
                            fs = FileStorage(stream=fp, filename=item)
                            upload_file(file=fs, challenge_id=chal.id, type="challenge")
                        print(f"    [+] Uploaded file: {item} -> {display_name}")

            total_added += 1

    print(f"\n[3/3] Update complete. {total_added} challenges deployed successfully.")
EOF

echo "[3/4] Pushing files to CTFd container..."
docker exec -u root "$CTFD_CONTAINER" rm -rf /tmp/repo
docker cp "$REPO_DIR" "$CTFD_CONTAINER":/tmp/repo
docker cp /tmp/update_challenges.py "$CTFD_CONTAINER":/tmp/update_challenges.py

echo "[4/4] Executing sync process inside container..."
docker exec -u root "$CTFD_CONTAINER" bash -c "cd /opt/CTFd && /opt/venv/bin/python /tmp/update_challenges.py"

echo "[✔] Automated sync complete!"

