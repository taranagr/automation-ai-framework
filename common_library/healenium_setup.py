import os
import shutil
import subprocess
import time

import requests

def healenium_setup():
    shared_path = "<Enter Here Shared File Path>"
    # Check Healenium server is up or not
    if api_get_request("http://<SERVER_ID>:7878/healenium/report/"):
        # Check Selenium Server is up or not
        if not api_get_request("http://localhost:4444/status"):
            copy_file(
                shared_path + "/selenium-server-4.25.0.jar",
                "C:/Healenium/selenium-server-4.25.0.jar")
            copy_file(
                shared_path + "/StartSeleniumServer.bat",
                "C:/Healenium/StartSeleniumServer.bat")
            print("Starting Selenium server...")
            execute_batch_file("C:/Healenium/StartSeleniumServer.bat")
            if not api_get_request("http://localhost:4444/status"):
                os.environ["HEALENIUM_FLAG"] = "NO"
                raise Exception("Selenium Server is not up and running")
        # Check Healenium proxy is up or not
        if not api_get_request("http://localhost:8085/"):
            kill_process("bash.exe")
            # parent_path = os.path.abspath(os.path.dirname("./"))
            parent_path = ""
            # healenium_path = os.path.abspath(os.path.dirname("./healenium/shell-installation/selenium-grid/"))
            healenium_path = os.path.abspath(os.path.dirname("C:/Healenium/"))
            copy_file(
                shared_path + "/stop_healenium.sh",
                "C:/Healenium/stop_healenium.sh")
            copy_file(
                shared_path + "/download_services.sh",
                "C:/Healenium/download_services.sh")
            copy_file(
                shared_path + "/start_healenium.sh",
                "C:/Healenium/start_healenium.sh")
            copy_file(
                shared_path + "/StopHealenium.sh",
                "C:/Healenium/StopHealenium.sh")
            copy_file(
                shared_path + "/DownloadServices.sh",
                "C:/Healenium/DownloadServices.sh")
            copy_file(
                shared_path + "/StartHealenium.sh",
                "C:/Healenium/StartHealenium.sh")
            print(parent_path)
            print(healenium_path)
            execute_shell_file(os.path.join(healenium_path, "StopHealenium.sh"))
            execute_shell_file(os.path.join(healenium_path, "DownloadServices.sh"))
            print("Starting Healenium-proxy...")
            execute_shell_file(os.path.join(healenium_path, "StartHealenium.sh"))
            if not api_get_request("http://localhost:8085/"):
                os.environ["HEALENIUM_FLAG"] = "NO"
                # raise Exception("Healenium-proxy is not up and running")
                print("Healenium-proxy is not up and running")
    else:
        os.environ["HEALENIUM_FLAG"] = "NO"
        # raise Exception("Healenium backend server is not up and running")
        print("Healenium backend server is not up and running")

def copy_file(src_file, dst_file):
    # check file exists
    # src_file = "source/file.txt"
    # dst_file = "destination/file.txt"
    os.makedirs(os.path.dirname(dst_file), exist_ok=True)
    if not os.path.exists(dst_file):
        print(f"Copying {src_file} to {dst_file}...")
        shutil.copyfile(src_file, dst_file)
        print("Copy complete.")
    else:
        print(f"The file {dst_file} already exists. Skipping copy operation.")

def api_get_request(url, api_body="", api_response=""):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"API {str(url)} is up and running")
            return True
    except Exception as e:
        print(f"API Exception Occurred {e}")
        return False
    return False

def execute_batch_file(path):
    try:
        # process = subprocess.Popen(path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # flags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
        process = subprocess.Popen(path)
        print(f"executed file {path}")
        print(f"The subprocess ID is: {process.pid}")
        time.sleep(10)
        return True
    except FileNotFoundError:
        print("Error: path not found")
        return False

def execute_shell_file(path):
    try:
        # flags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
        # process = subprocess.Popen(path, creationflags=flags, shell=True)
        process = subprocess.Popen(path, shell=True)
        print(f"executed file {path}")
        print(f"The subprocess ID is: {process.pid}")
        time.sleep(30)
        return True
    except FileNotFoundError:
        print("Error: 'java' command not found. Ensure Java is installed and in your PATH.")
        return False

def kill_process(process_name = "bash.exe"):
    command = f"taskkill /f /im {process_name}"
    try:
        result = os.system(command)
        if result == 0:
            print(f"All instances of {process_name} terminated successfully")
        else:
            print(f"command executed, but an issue might exist or no processes found. Result code: {result}")
    except Exception as e:
        print(f"An exception occurred: {e}")
