"""
Basic 2030.5 (SEP 2) server using pysep
This server listens for DER (smart inverter) client connections and receives status updates.
"""
from pysep import sep_server

# Configuration (update as needed)
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8443
SERVER_CERT = "server.crt"
SERVER_KEY = "server.key"
CA_CERT = "ca.crt"

class DERServer(sep_server.SEPServer):
    def on_der_status(self, client_addr, status):
        print(f"Received DER status from {client_addr}: {status}")

if __name__ == "__main__":
    server = DERServer(
        host=SERVER_HOST,
        port=SERVER_PORT,
        cert=SERVER_CERT,
        key=SERVER_KEY,
        ca_cert=CA_CERT
    )
    print(f"2030.5 server running on {SERVER_HOST}:{SERVER_PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
    finally:
        server.shutdown()
