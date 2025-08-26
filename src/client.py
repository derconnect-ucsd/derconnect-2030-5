"""
Simulated Smart Inverter 2030.5 Client using pysep
This example demonstrates a DER (smart inverter) client that connects to a 2030.5 server and reports status.
"""
from pysep import sep_client
import time
from utils.inverter import get_inverter_status

# Configuration (update as needed)
SERVER_URL = "https://localhost:8443/sep"
CLIENT_CERT = "client.crt"
CLIENT_KEY = "client.key"
CA_CERT = "ca.crt"

def main():
    # Create a SEP 2.0 client
    client = sep_client.SEPClient(
        server_url=SERVER_URL,
        cert=CLIENT_CERT,
        key=CLIENT_KEY,
        ca_cert=CA_CERT
    )
    print("Smart inverter client started. Connecting to server...")
    client.connect()
    print("Connected. Sending status updates...")
    try:
        while True:
            status = get_inverter_status()
            # Send DERStatus (this is a placeholder, actual pysep API may differ)
            client.send_der_status(status)
            print(f"Status sent: {status}")
            time.sleep(10)  # Send every 10 seconds
    except KeyboardInterrupt:
        print("Client stopped.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
