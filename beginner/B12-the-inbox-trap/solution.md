# Solution: B12 - THE INBOX TRAP

## Concept
Email analysis involves scrutinizing message headers, sender domains, urgency cues, and embedded links to isolate targeted phishing lures from normal messages and noise.

## Walkthrough
1. Inspect `challenge/email_dump.txt` or search for urgent profile/account verification messages:
   ```bash
   grep -n -C 5 -i "verification" challenge/email_dump.txt
   ```
2. Locate the deceptive social profile verification lure:
   - Sender: `Instagram Support <support@instagram.com>`
   - Subject: `Your profile requires verification`
3. Inspect the email footer around line 496:
   ```
   Reference ID: phish_beacon_tracked_77
   ```
4. Recover the flag:
   ```
   phish_beacon_tracked_77
   ```

## Flag
`phish_beacon_tracked_77`
