#!/usr/bin/env python3
"""
Dynamic  Balancer - Launch Script
Starts the Flask backend server.
Open _balancer_dashboard.html in your browser to interact with it.
"""
import subprocess
import sys
import os
import time
import webbrowser
import signal

print("""
╔══════════════════════════════════════════════════════════╗
║   Dynamic  Balancer — Multiprocessor Simulation      ║
╠══════════════════════════════════════════════════════════╣
║  Starting Flask backend on http://localhost:5000          ║
║  Open _balancer_dashboard.html in your browser        ║
╚══════════════════════════════════════════════════════════╝
""")

backend_path = os.path.join(os.path.dirname(__file__), 'backend.py')

proc = subprocess.Popen(
    [sys.executable, backend_path],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print(f"Backend PID: {proc.pid}")
print("Press Ctrl+C to stop.\n")

def cleanup(sig, frame):
    print("\nShutting down...")
    proc.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)

# Wait for it to be ready
time.sleep(1.5)
if proc.poll() is not None:
    print("ERROR: Backend failed to start!")
    out, err = proc.communicate()
    print(err.decode())
    sys.exit(1)

print("Backend is running!")
print("Dashboard: open _balancer_dashboard.html")
print()

# Keep running
proc.wait()
