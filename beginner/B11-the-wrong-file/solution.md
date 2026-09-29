# Solution: B11 - THE WRONG FILE

## Concept
File extensions can be spoofed, but file identification utilities (`file`) check magic bytes to reveal the true format. Zip archives start with the ASCII signature `PK\x03\x04` regardless of their file extension.

## Walkthrough
1. Inspect the true type of `challenge/photo.jpg`:
   ```bash
   file challenge/photo.jpg
   ```
   Output confirms: `Zip archive data`.
2. Extract the disguised archive into a folder or inspect its contents:
   ```bash
   unzip challenge/photo.jpg -d extracted/
   ```
3. Read `extracted/photo/metadata.txt`:
   ```bash
   cat extracted/photo/metadata.txt
   ```
4. Recover the flag:
   ```
   magic_header_unmasked_55
   ```

## Flag
`magic_header_unmasked_55`
