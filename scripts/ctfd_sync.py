#!/usr/bin/env python3
"""
CTFd Synchronization & Management Script
Automates:
1. Attaching challenge files to CTFd challenges (fixes missing download buttons like B08 & B09).
2. Setting up hints with point deductions (cost parameter in CTFd).
3. Synchronizing challenge metadata, descriptions, and flags.
"""

import os
import sys
import re
import glob
import argparse
import requests

DEFAULT_CTFD_URL = os.environ.get("CTFD_URL", "http://localhost:8000")
DEFAULT_API_TOKEN = os.environ.get("CTFD_TOKEN", "")

def get_headers(token):
    return {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

def get_session(url, token):
    s = requests.Session()
    s.headers.update({
        "Authorization": f"Token {token}",
        "Accept": "application/json"
    })
    return s

def fetch_all_challenges(session, base_url):
    """Fetch all challenges from CTFd API."""
    url = f"{base_url.rstrip('/')}/api/v1/challenges"
    r = session.get(url, headers={"Content-Type": "application/json", "Accept": "application/json"})
    if r.status_code != 200:
        print(f"[-] Failed to fetch challenges from {url}: HTTP {r.status_code}")
        print(f"[-] Response: {r.text}")
        return []
    try:
        data = r.json()
        return data.get("data", [])
    except Exception as e:
        print(f"[-] Error parsing JSON from {url}: {e}")
        return []

DEFAULT_TIER_HINT_CONFIG = {
    "B": {"count": 1, "cost": 2},  # Beginner: 1 hint, 2 pts deduction (5 -> 3 net)
    "I": {"count": 2, "cost": 2},  # Intermediate: 2 hints, 2 pts each (10 -> 8 or 6 net)
    "A": {"count": 3, "cost": 2},  # Advanced: 3 hints, 2 pts each (20 -> 18, 16, or 14 net)
}

def parse_tier_hints(text, challenge_code):
    """
    Parse hints from markdown based on tier specification:
    - Beginner ('B'): 1 consolidated hint
    - Intermediate ('I'): 2 hints
    - Advanced ('A'): 3 hints
    """
    tier = challenge_code[0].upper() if challenge_code else "B"
    body = re.sub(r"^(#|Hints:)[^\n]*\n+", "", text).strip()
    
    # Check if headers like ### Hint X exist
    header_parts = re.split(r"(?m)^###?\s*Hint\s*\d+[:\.]?\s*", text)
    header_parts = [p.strip() for p in header_parts[1:] if p.strip()]
    
    # Check numbered items like 1. ... 2. ...
    num_parts = []
    current = []
    for line in text.splitlines():
        m = re.match(r"^\d+\.\s*(.*)", line)
        if m:
            if current:
                num_parts.append("\n".join(current).strip())
            current = [m.group(1)]
        elif current:
            current.append(line)
    if current:
        num_parts.append("\n".join(current).strip())
        
    parts = header_parts if header_parts else num_parts
    if not parts:
        parts = [body]
        
    if tier == "B":
        return [body]
    elif tier == "I":
        if len(parts) >= 3:
            return [parts[0], parts[1] + "\n\n" + parts[2]]
        elif len(parts) == 2:
            return parts
        else:
            return [parts[0]]
    else:  # 'A'
        return parts[:3]

def sync_hints(session, base_url, challenge_id, challenge_code, hints_path, cost_override=None, replace_existing=True):
    """Sync hints for a challenge and assign tier-specific point deduction costs."""
    if not os.path.exists(hints_path):
        print(f"[*] No hints file found at {hints_path}")
        return
        
    with open(hints_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read().strip()
    if not text:
        print(f"[*] Hints file {hints_path} is empty")
        return
        
    prefix = challenge_code[0].upper() if challenge_code else "B"
    config = DEFAULT_TIER_HINT_CONFIG.get(prefix, {"count": 1, "cost": 2})
    hint_cost = cost_override if cost_override is not None else config["cost"]
    
    hints_to_post = parse_tier_hints(text, challenge_code)
    
    # Check existing hints on CTFd
    hints_list_url = f"{base_url.rstrip('/')}/api/v1/hints"
    r = session.get(hints_list_url)
    all_hints = r.json().get("data", []) if r.status_code == 200 else []
    existing_hints = [h for h in all_hints if h.get("challenge_id") == challenge_id or h.get("challenge") == challenge_id]
    
    if replace_existing and existing_hints:
        for eh in existing_hints:
            del_url = f"{base_url.rstrip('/')}/api/v1/hints/{eh['id']}"
            session.delete(del_url)
        print(f"[*] Cleared {len(existing_hints)} existing hint(s) for {challenge_code}")
    
    post_url = f"{base_url.rstrip('/')}/api/v1/hints"
    for idx, hint_content in enumerate(hints_to_post, 1):
        payload = {
            "challenge_id": challenge_id,
            "challenge": challenge_id,
            "content": hint_content,
            "cost": hint_cost,
            "type": "standard"
        }
        res = session.post(post_url, json=payload)
        if res.status_code in [200, 201]:
            print(f"[+] Added Hint {idx}/{len(hints_to_post)} for {challenge_code} (Cost: {hint_cost} pts deduction)")
        else:
            print(f"[-] Failed to add Hint {idx} for {challenge_code}: {res.text}")

def upload_files(session, base_url, challenge_id, challenge_code, challenge_dir):
    """Upload all challenge files from challenge/ to CTFd."""
    folder = os.path.join(challenge_dir, "challenge")
    if not os.path.exists(folder):
        print(f"[*] No challenge/ folder found for {challenge_code}")
        return
    
    # Get list of files already attached from challenge details
    chal_info_url = f"{base_url.rstrip('/')}/api/v1/challenges/{challenge_id}"
    r = session.get(chal_info_url)
    existing_files = []
    if r.status_code == 200:
        for f_path in r.json().get("data", {}).get("files", []):
            clean_name = f_path.split("?")[0].split("/")[-1]
            existing_files.append(clean_name)
    
    post_url = f"{base_url.rstrip('/')}/api/v1/files"
    
    files_to_upload = []
    for root, _, filenames in os.walk(folder):
        for fname in filenames:
            if fname.startswith(".") or fname == "README.md":
                continue
            full_path = os.path.join(root, fname)
            files_to_upload.append(full_path)
            
    if not files_to_upload:
        print(f"[*] No files found in {folder} to upload for {challenge_code}")
        return
        
    for fpath in files_to_upload:
        fname = os.path.basename(fpath)
        # Avoid duplicate uploads of the exact same basename
        if any(fname in ef for ef in existing_files):
            print(f"[*] File '{fname}' already attached to {challenge_code}. Skipping duplicate.")
            continue
            
        with open(fpath, "rb") as fh:
            files = {"file": (fname, fh.read())}
            data = {"challenge": challenge_id, "type": "challenge"}
            res = session.post(post_url, files=files, data=data)
            if res.status_code in [200, 201]:
                print(f"[+] Successfully attached '{fname}' to {challenge_code}")
            else:
                print(f"[-] Failed to attach '{fname}' to {challenge_code}: {res.text}")

def find_local_challenges(repo_root, track_filter=None):
    """Find challenge folders across beginner, intermediate, and advanced."""
    tracks = ["beginner", "intermediate", "advanced"]
    if track_filter and track_filter in tracks:
        tracks = [track_filter]
        
    results = {}
    for track in tracks:
        track_dir = os.path.join(repo_root, track)
        if not os.path.exists(track_dir):
            continue
        for entry in sorted(os.listdir(track_dir)):
            full = os.path.join(track_dir, entry)
            if os.path.isdir(full):
                # Match B01, I02, A03 prefixes
                m = re.match(r"^([BIA]\d{2})", entry)
                if m:
                    code = m.group(1)
                    results[code] = full
    return results

def main():
    parser = argparse.ArgumentParser(description="Sync challenges, files, and cost-deducting hints to CTFd")
    parser.add_argument("--url", default=DEFAULT_CTFD_URL, help=f"CTFd base URL (default: {DEFAULT_CTFD_URL})")
    parser.add_argument("--token", default=DEFAULT_API_TOKEN, help="CTFd Admin API Token (or set CTFD_TOKEN env var)")
    parser.add_argument("--track", choices=["beginner", "intermediate", "advanced", "all"], default="all", help="Track to sync")
    parser.add_argument("--challenge", help="Specific challenge code to sync (e.g. B08, B09)")
    parser.add_argument("--hint-cost", type=int, default=None, help="Point deduction cost override (default: B=2, I=4, A=8)")
    parser.add_argument("--action", choices=["all", "hints", "files"], default="all", help="Action to execute")
    
    args = parser.parse_args()
    
    if not args.token:
        print("[-] Error: CTFd Admin API token is required.")
        print("[-] Provide it via --token <TOKEN> or set the CTFD_TOKEN environment variable.")
        print("[-] You can generate a token in CTFd under: Settings -> Access Tokens -> Generate Token.")
        sys.exit(1)
        
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    local_challenges = find_local_challenges(repo_root, None if args.track == "all" else args.track)
    
    if args.challenge:
        code = args.challenge.upper()
        if code not in local_challenges:
            print(f"[-] Error: Challenge code {code} not found in local repo.")
            sys.exit(1)
        local_challenges = {code: local_challenges[code]}
        
    session = get_session(args.url, args.token)
    ctfd_challenges = fetch_all_challenges(session, args.url)
    
    if not ctfd_challenges:
        print("[-] No challenges found on CTFd or connection failed. Exiting.")
        sys.exit(1)
        
    print(f"[*] Connected to CTFd at {args.url}. Found {len(ctfd_challenges)} challenges online.\n")
    
    # Map CTFd challenges by code prefix in their title (e.g. "B08", "B09")
    ctfd_map = {}
    for c in ctfd_challenges:
        name = c.get("name", "")
        m = re.match(r"^([BIA]\d{2})", name)
        if m:
            ctfd_map[m.group(1)] = c
            
    for code, local_path in sorted(local_challenges.items()):
        if code not in ctfd_map:
            print(f"[-] Warning: {code} not found on CTFd server (check title prefix in CTFd). Skipping.")
            continue
            
        c_obj = ctfd_map[code]
        c_id = c_obj["id"]
        c_name = c_obj["name"]
        print(f"\n=== Processing {code}: {c_name} (CTFd ID: {c_id}) ===")
        
        # 1. Attach missing files
        if args.action in ["all", "files"]:
            upload_files(session, args.url, c_id, code, local_path)
            
        # 2. Setup hints with point deduction cost
        if args.action in ["all", "hints"]:
            hints_file = os.path.join(local_path, "hints.md")
            sync_hints(session, args.url, c_id, code, hints_file, cost_override=args.hint_cost)
            
    print("\n[+] Synchronization routine complete!")

if __name__ == "__main__":
    main()
