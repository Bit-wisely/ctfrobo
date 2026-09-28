Hints: A13 - BROKEN AUTHENTICATION

1. Analyze how password reset tokens or session keys are generated in the application source code.
2. Identify deterministic or predictable components such as fixed salts combined with usernames in the hashing logic.
3. Generate the expected hash for the privileged account and provide it to the verification endpoint to complete the reset.
