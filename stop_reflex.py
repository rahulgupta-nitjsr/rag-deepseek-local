import os
import signal
import psutil

def stop_reflex_server():
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        if process.info['name'] == 'python' and 'reflex' in ' '.join(process.info['cmdline']):
            os.kill(process.info['pid'], signal.SIGTERM)
            return f"Stopped Reflex server with PID {process.info['pid']}"
    return "No running Reflex server found."

print(stop_reflex_server())
