import subprocess

def open_calc():
    subprocess.call('calc.exe')

try:
    open_calc()
except KeyboardInterrupt:
    exit()
