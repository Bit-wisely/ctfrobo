Hints: A01 - THE BINARY SECRET

1. Static analysis tools such as Ghidra, IDA, or objdump can help inspect the disassembled validation function.
2. The binary compares your input against an internal byte array after applying a simple bitwise byte transformation.
3. Trace the transformation applied during the loop and write a reverse script to invert the operation on the target byte sequence.
