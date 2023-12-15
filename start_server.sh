#!/bin/bash

# Start Flask server
python3 app.py &

# Display host IP address
echo "Host IP address:"
ipconfig getifaddr en0  # Use 'en0' for Wi-Fi, 'en1' for Ethernet

# Open browser with server URL
sleep 2  # Wait for the server to start (adjust as needed)
open http://127.0.0.1:5000/
