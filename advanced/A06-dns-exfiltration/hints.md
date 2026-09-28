Hints: A06 - DNS EXFILTRATION

1. DNS queries often encapsulate exfiltrated data inside subdomains or query labels.
2. Filter and extract the requested domain names, observing any sequence indexing or payload chunks in the subdomains.
3. Order the extracted chunks sequentially, join the payload segments, and decode the combined hex representation into plaintext.
