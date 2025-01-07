# Simple TCP Chatroom

This is a basic chatroom implementation using Python's `socket` and `threading` standard libraries, as well as the `Datetime` library.

**Features:**

* **Multi-user:** Multiple clients can connect to the server and chat with each other.
* **Threading:** Server handles multiple clients concurrently using threads.
* **Basic Error Handling:** Includes basic error handling for connection issues.
* **Timestamping:** Messages are displayed with timestamps for better readability.

**Files:**

* `server.py`: Contains the server-side logic.
* `client.py`: Contains the client-side logic.

**To run:**

1. **Start the server:**
   ```bash
   python server.py

2. **Run multiple client instances:**

   You can open multiple terminal windows to run multiple clients.

    ```bash
    python client.py
    
**How it works:**

1. **Server:**
     * Creates a socket and binds it to a specific address and port.
     * Listens for incoming client connections.
     * Accepts connections and creates a new thread for each client.
     * Handles incoming messages from clients and broadcasts them to all connected clients.
          
2. **Client:**
     * Connects to the server.
     * Sends and receives messages from the server.
     * Displays received messages in the terminal.

**This is a basic implementation and can be further enhanced with features like:**

 * User authentication
 * Private messaging
 * File transfer
 * Improved error handling and exception handling
