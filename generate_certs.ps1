# Certificate generation instructions for 2030.5/SEP 2 demo
# Run these commands in PowerShell from your project root

# 1. Generate CA key and certificate
openssl req -x509 -newkey rsa:2048 -days 365 -nodes -keyout ca.key -out ca.crt -config openssl.conf -extensions v3_ca

# 2. Generate server key and CSR
openssl req -newkey rsa:2048 -nodes -keyout server.key -out server.csr -config openssl.conf

# 3. Sign server certificate with CA
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365 -extensions req_ext -extfile openssl.conf

# 4. Generate client key and CSR
openssl req -newkey rsa:2048 -nodes -keyout client.key -out client.csr -config openssl.conf

# 5. Sign client certificate with CA
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365 -extensions req_ext -extfile openssl.conf

# Clean up
Remove-Item server.csr, client.csr
