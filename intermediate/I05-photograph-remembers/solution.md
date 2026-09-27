Solution: I05 - THE PHOTOGRAPH REMEMBERS

Concept  
Image metadata extraction and EXIF analysis.

Walkthrough  
1. Run `exiftool` on `challenge/photograph.jpg`:
   ```bash
   exiftool challenge/photograph.jpg
   ```
2. Or use `strings`:
   ```bash
   strings challenge/photograph.jpg | grep "flag{"
   ```
3. Locate the comment: `flag{exif_metadata_secret}`.

Flag  
`flag{exif_metadata_secret}`
