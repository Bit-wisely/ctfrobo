# Hints: B11 - THE WRONG FILE

### Hint 1
Operating system file extensions like `.jpg` or `.txt` are merely cosmetic naming conventions and do not enforce what format is actually stored inside the file.

### Hint 2
Most binary formats begin with standardized header bytes ("magic bytes") that distinguish images, executables, and compressed archives regardless of what name they are given.

### Hint 3
Use system file diagnostic tools to inspect the underlying signature of `photo.jpg`, determine its true archive structure, and extract its contents.
