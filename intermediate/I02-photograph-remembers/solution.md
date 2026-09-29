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
   strings challenge/photograph.jpg
   ```
3. Locate the comment: `exif metadata secret`.

Flag  
`exif metadata secret`
