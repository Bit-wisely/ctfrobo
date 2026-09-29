# Solution: B01 - THE MACHINE SPEAKS

## Concept
Base-2 binary representation converts binary octets into integer values, which map directly to ASCII characters (where bit values correspond to powers of 2 from $2^0$ to $2^7$).

## Walkthrough
1. Inspect the binary strings produced by the challenge:
   - `01110000` -> 112 -> 'p'
   - `01110101` -> 117 -> 'u'
   - `01101100` -> 108 -> 'l'
   - `01110011` -> 115 -> 's'
   - `01100001` -> 97  -> 'a'
   - `01110010` -> 114 -> 'r'
   - `01011111` -> 95  -> '_'
   - `01110011` -> 115 -> 's'
   - `01101001` -> 105 -> 'i'
   - `01100111` -> 103 -> 'g'
   - `01101110` -> 110 -> 'n'
   - `01100001` -> 97  -> 'a'
   - `01101100` -> 108 -> 'l'
   - `01011111` -> 95  -> '_'
   - `01100100` -> 100 -> 'd'
   - `01100101` -> 101 -> 'e'
   - `01110100` -> 116 -> 't'
   - `01100101` -> 101 -> 'e'
   - `01100011` -> 99  -> 'c'
   - `01110100` -> 116 -> 't'
   - `01100101` -> 101 -> 'e'
   - `01100100` -> 100 -> 'd'
   - `01011111` -> 95  -> '_'
   - `00110001` -> 49  -> '1'
   - `00111001` -> 57  -> '9'
2. Concatenate the decoded characters to form the flag:
   ```
   pulsar_signal_detected_19
   ```

## Flag
`pulsar_signal_detected_19`
