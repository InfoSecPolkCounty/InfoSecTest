import subprocess

def python_subprocess_shell():
    while True:
        try:
            command = input('Enter command to execute: ')
            subprocess.call(command)
        except KeyboardInterrupt:
            break

python_subprocess_shell()
