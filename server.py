import http.server
import socketserver
import json
import os
import sys
import threading
import time
import webbrowser
import socket

# --- THE "NO CONSOLE" FIX ---
class NullWriter:
    def write(self, x): pass
    def flush(self): pass

if sys.executable.endswith("pythonw.exe") or getattr(sys, 'frozen', False):
    sys.stdout = NullWriter()
    sys.stderr = NullWriter()

# --- CONFIG ---
START_PORT = 8000
MAX_PORT_RETRIES = 20
BIND_ADDRESS = "127.0.0.1"

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def find_free_port(start_port):
    for port in range(start_port, start_port + MAX_PORT_RETRIES):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex((BIND_ADDRESS, port)) != 0:
                return port
    return start_port

# --- HEARTBEAT MONITOR ---
last_heartbeat = time.time() + 15 

def shutdown_monitor():
    global last_heartbeat
    while True:
        time.sleep(1)
        if time.time() - last_heartbeat > 5:
            os._exit(0)

threading.Thread(target=shutdown_monitor, daemon=True).start()

class CrosswordHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        if self.path == '/' or self.path.startswith('/CrosswordStudio.html'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            try:
                with open(resource_path('CrosswordStudio.html'), 'rb') as f:
                    self.wfile.write(f.read())
            except:
                pass
            return
        
        if self.path == '/CrosswordStudio.ico' or self.path == '/favicon.ico':
            self.send_response(200)
            self.send_header('Content-type', 'image/x-icon')
            self.end_headers()
            try:
                with open(resource_path('CrosswordStudio.ico'), 'rb') as f:
                    self.wfile.write(f.read())
            except:
                pass
            return

        super().do_GET()

    def do_POST(self):
        global last_heartbeat
        if self.path == '/heartbeat':
            last_heartbeat = time.time()
            self.send_response(200)
            self.end_headers()
            return

        if self.path == '/save':
            try:
                content_length = int(self.headers['Content-Length'])
                data = json.loads(self.rfile.read(content_length))
                title = data.get('title', 'Untitled')
                safe_title = "".join([c for c in title if c.isalnum() or c in ' _']).rstrip() or "Untitled"
                
                exe_dir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.getcwd()
                save_dir = os.path.join(exe_dir, 'Puzzles')
                if not os.path.exists(save_dir): os.makedirs(save_dir)
                
                filename = os.path.join(save_dir, f"{safe_title}.json")

                # --- FIX: INCREMENTING FILE NUMBERS RESTORED ---
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(filename):
                    filename = f"{base} ({counter}){ext}"
                    counter += 1
                # -----------------------------------------------
                
                with open(filename, 'w') as f:
                    f.write(json.dumps(data))
                    
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Saved")
                last_heartbeat = time.time()
            except:
                self.send_response(500)
                self.end_headers()

if __name__ == '__main__':
    PORT = find_free_port(START_PORT)
    url = f'http://{BIND_ADDRESS}:{PORT}/'
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer((BIND_ADDRESS, PORT), CrosswordHandler) as httpd:
            httpd.serve_forever()
    except:
        os._exit(1)