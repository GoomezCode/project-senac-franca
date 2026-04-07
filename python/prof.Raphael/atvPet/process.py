import os
import subprocess

def clearTerminal():
    os.system('cls' if os.name == "nt" else 'clear')

def stopProcess():
     pid = os.getpid()
     subprocess.run(['taskkill', '/F', '/PID', str(pid)], check=True)
     
