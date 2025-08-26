# derconnect-2030-5

## Setup and Testing Instructions

### 1. Install dependencies and set up virtual environment

```
make install
```

### 2. Generate certificates (if not already done)

```
./generate_certs.ps1
```

This will create `ca.crt`, `server.crt`, `server.key`, `client.crt`, and `client.key` in the project root.

### 3. Run the 2030.5 server

```
make run-server
```
The server will listen for incoming DER (smart inverter) client connections and print received status updates.

### 4. Run the 2030.5 client (simulated smart inverter)

In a new terminal:

```
make run-client
```
The client will connect to the server and periodically send simulated inverter status updates.

### 5. Verify communication

You should see status messages printed in the server terminal when the client is running.

---
For more details on the protocol and code, see the `src/` directory and comments in the code files.