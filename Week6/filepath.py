import os

def cwd():
    path = os.getcwd()
    print(f"Current working Directory is {path}")
    print(f"The directory contains the following files")
    for files in os.listdir(path):
        print(files)

def run():
    print("Processing...")
    cwd()

run()