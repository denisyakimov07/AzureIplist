import re
import requests
import time
import os
from os import listdir
from os.path import isfile, join

MICROSOFT_URL = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.110 Safari/537.3"
    )
}

SLEEP = 60


def get_latest_json_url() -> dict:
    """Extract latest Azure IP list JSON URL from Microsoft's confirmation page."""
    response = requests.get(MICROSOFT_URL, headers=HEADERS, timeout=10)
    match = re.search(r"https://download\.microsoft\.com/download[^\s\"']*?\.json", response.text).group(0)
    return dict({"url": match, "file_name": re.search(r'/([^/]+)$', match).group(1)}) if match else {}


def remove_file(file_list, path):
    for file_path in file_list:
        # Check if the file exists before trying to delete it
        if os.path.exists(f'./{path}/{file_path}') and os.path.isfile(f'./{path}/{file_path}'):
            try:
                os.remove(f'./{path}/{file_path}')
                print(f"Removed: {f'./{path}/{file_path}'}")
            except OSError as os_e:
                print(f"Error removing {f'./{path}/{file_path}'}: {os_e}")
        else:
            print(f"File not found, skipping: {f'./{path}/{file_path}'}")


while True:
    try:
        data = get_latest_json_url()
        only_files = [f for f in listdir("./ip_data/") if isfile(join("./ip_data/", f))]
        print(data)
        print(only_files)
        if data["file_name"] not in only_files:
            file_download = requests.get(data["url"], headers=HEADERS, timeout=10)
            open(f'./ip_data/{data["file_name"]}', "wb").write(file_download.content)
            print(f'File saved to ip_data/{data["file_name"]}')
            remove_file(only_files, "ip_data")

        else:
            print(f"file {data['file_name']} in {only_files} sleep time 60 min.")
        SLEEP = 60
    except Exception as e:
        SLEEP = 1
        print(f"An unexpected error occurred: {e} sleep time {SLEEP * 60} sec.")
    time.sleep(SLEEP * 60)
