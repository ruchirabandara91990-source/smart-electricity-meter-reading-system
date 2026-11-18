import subprocess
import sys
import os

# ESP32-CAM stream URL
url = "http://192.168.8.179:81/stream"

def open_vlc(url):
    try:
        # try to run VLC directly
        subprocess.Popen(["vlc", url])
        print(f"Opening stream in VLC: {url}")
    except FileNotFoundError:
        print("VLC not found in PATH. Trying common installation paths...")

        if sys.platform.startswith("win"):
            # Typical VLC install paths on Windows
            possible_paths = [
                r"C:\Program Files\VideoLAN\VLC\vlc.exe",
                r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
            ]
            for path in possible_paths:
                if os.path.exists(path):
                    subprocess.Popen([path, url])
                    print(f"Opening stream in VLC (path: {path})")
                    return
            print("Could not find VLC. Please install VLC or add it to PATH.")
        elif sys.platform.startswith("darwin"):
            # macOS
            subprocess.Popen(["/Applications/VLC.app/Contents/MacOS/VLC", url])
        else:
            # Linux fallback
            subprocess.Popen(["/usr/bin/vlc", url])

if __name__ == "__main__":
    open_vlc(url)
