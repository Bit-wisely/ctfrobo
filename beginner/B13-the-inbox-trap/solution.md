Solution: B13 - THE INBOX TRAP

Concept
Email forensics, header analysis, and distinguishing targeted phishing messages from decoys and legitimate traffic.

Walkthrough
1. Inspect the exported email dump (`challenge/email_dump.txt`).
2. Identify that the dump contains a mixture of legitimate communications, automated newsletters, security notifications, and several decoy phishing attempts.
3. Analyze and compare candidate emails by inspecting headers, subject lines, context, and message bodies.
4. Locate the targeted Instagram Support phishing message:
   - From: Instagram Support <support@instagram.com>
   - Subject: Your profile requires verification
   - Date: Tue, 29 Sep 2026 11:17:42 +0530
5. Inspect the full body of the email to identify the unique tracking metadata:
   - Reference ID: emailtrailflag
6. Extract the answer string: emailtrailflag.

Flag
emailtrailflag
