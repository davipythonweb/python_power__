import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

FILE_TO_WATCH = "class_3.py"

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(FILE_TO_WATCH):
            print("\n🔄 Arquivo salvo! Executando...\n")
            subprocess.run(["python", FILE_TO_WATCH])

event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, ".", recursive=False)
observer.start()

print("👀 Monitorando alterações no arquivo...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
