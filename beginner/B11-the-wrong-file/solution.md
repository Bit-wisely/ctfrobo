# Solution: B11 - THE WRONG FILE

Concept
File signatures, magic bytes, misleading file extensions, and archive extraction.

Walkthrough
1. Inspect the file photo.jpg using the file command: `file photo.jpg`.
2. Observe that the file is identified as a Zip archive data rather than a JPEG image.
3. Extract the archive using unzip: `unzip photo.jpg`.
4. Inspect the extracted folder `photo/`.
5. Open `photo/metadata.txt` to find the secret answer.

Flag
false_identity
