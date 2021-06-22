import subprocess

def python_subprocess_shell():
    while True:
        try:
            command = raw_input('Enter command to execute: ')
            subprocess.call(command)
        except KeyboardInterrupt:
            break

python_subprocess_shell()
