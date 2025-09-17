import os, requests, subprocess, time, json

SERVER_URL = "http://127.0.0.1:5000"   # or your LAN IP
LOCAL_VERSION_FILE = "current_version.json"
DOWNLOAD_DIR = "."

def get_local_version():
    if not os.path.exists(LOCAL_VERSION_FILE):
        return "0.0"
    with open(LOCAL_VERSION_FILE, "r") as f:
        return json.load(f)["version"]

def save_local_version(version):
    with open(LOCAL_VERSION_FILE, "w") as f:
        json.dump({"version": version}, f)

def download_update(filename):
    url = f"{SERVER_URL}/download/{filename}"
    r = requests.get(url)
    path = os.path.join(DOWNLOAD_DIR, filename)
    with open(path, "wb") as f:
        f.write(r.content)
    return path

def run_update(file_path):
    print("🚀 Running new update...")
    subprocess.run(["python", file_path])  # use python on Windows

while True:
    try:
        r = requests.get(f"{SERVER_URL}/version")
        print("📡 Raw response from server:", r.text)   # Debug print
        data = r.json()   # ✅ Safe JSON parsing
        cloud_version = data["version"]
        filename = data["file"]

        local_version = get_local_version()
        if cloud_version != local_version:
            print(f"🔔 New update found: {cloud_version}")
            file_path = download_update(filename)
            save_local_version(cloud_version)
            run_update(file_path)
        else:
            print("✅ No new update.")
    except Exception as e:
        print("❌ Error:", e)

    time.sleep(30)  # check every 30s
