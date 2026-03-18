#!/usr/bin/env python3
import http.server, os, webbrowser, threading

PORT = 8765
DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIR)

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")

threading.Timer(0.5, open_browser).start()
print(f"🖼️  Image Compressor running at http://localhost:{PORT}")
print("Press Ctrl+C to stop.")

http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=PORT, bind="127.0.0.1")
