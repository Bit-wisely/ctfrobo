# Solution: B12 - THE INBOX TRAP

## Concept
Email analysis involves scrutinizing message headers, sender domains, urgency cues, and embedded links to isolate targeted phishing lures from normal messages and noise. Attackers frequently use lookalike domains (such as typosquatting `rn` for `m`).

## Walkthrough
1. Inspect `challenge/email_dump.txt` or search for urgent profile/account verification messages:
   ```bash
   grep -n -C 5 -i "verification" challenge/email_dump.txt
   ```
2. Locate the deceptive social profile verification lure:
   - Sender: `Instagram Security Team <security-alerts@instagrarn-security-check.com>`
   - Notice the deceptive typosquatted domain (`instagrarn-security-check.com` with `rn` instead of `m`).
   - Subject: `Urgent: Your account requires identity verification`
3. Inspect the email footer:
   ```
   Reference ID: phish_beacon_tracked_77
   ```
4. Recover the flag:
   ```
   phish_beacon_tracked_77
   ```

## Flag
`phish_beacon_tracked_77`
