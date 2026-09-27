Hints: A13 - BROKEN AUTHENTICATION

1. The reset token is calculated using `MD5(username + "_secret_recovery_salt_2026")`.
2. Compute the MD5 hash for the string `admin_secret_recovery_salt_2026`.
3. Send a request to `/reset?token=04519965d1d64380eb9a3dd732958f2d`.
