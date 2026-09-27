**I06 - SMALLEST BITS**

**Points**: 300  
**Category**: Intermediate / LSB Steganography  

**Challenge Overview**  
Steganography is the practice of concealing secret messages within ordinary non-secret data. Least Significant Bit (LSB) steganography modifies the lowest bit of pixel color values. Because changing the least significant bit only alters the RGB shade by 1/256th, the change is completely invisible to human vision while hiding full byte sequences.

**Participant Question**  
You looked at the image. You zoomed in. You still can't see anything. Maybe you're looking at the wrong part of the image.

**Clue**  
Extract bit 0 (the least significant bit) from the RGB color channels of each pixel in the PNG image.

**Challenge Files**  
- `challenge/image.png`
- `challenge/extract_lsb.py`

**Flag Format**  
`flag{...}`
