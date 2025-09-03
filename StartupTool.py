import psutil
import os

#************************* Functions *************************************

def is_program_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

def read_config_files():
    global C
    with open('config/processes.txt', 'r') as file:
        processes = file.readlines()
        processes = [s.strip() for s in processes]

    with open('config/applications.txt', 'r') as file:
        applications = file.readlines()
        applications = [s.strip() for s in applications]

    return applications, processes

applications, processes = read_config_files()

#************************* logic ***************************************

i = 1
while i == 1:
    if is_program_running("iRacingUI.exe"):  # For Windows
        #print("iRacing is running")
        if not is_program_running("chrome.exe"):
            print("programs are not running, starting chrome")
            for application in applications:
                os.startfile(application)
            

