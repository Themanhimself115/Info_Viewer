import socket
import subprocess
import platform

def get_ssid():
    os_type = platform.system()
    ssid = None

    if os_type == "Windows":
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if "SSID" in line:
                ssid = line.split(":")[1].strip()
                break

    elif os_type == "Darwin":  # macOS
        result = subprocess.run(
            ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'],
            capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if "SSID" in line:
                ssid = line.split(":")[1].strip()
                break

    elif os_type == "Linux":
        result = subprocess.run(['iwgetid', '-r'], capture_output=True, text=True)
        ssid = result.stdout.strip()

    return ssid

ssid = get_ssid()

print(ssid)