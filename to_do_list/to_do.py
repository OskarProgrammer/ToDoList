import pathlib
from os import system

def exist(path):
    if path.exists():
        print("Istnieje plik")
        return 1
    else:
        print("Nie istnieje ")
        return 0
