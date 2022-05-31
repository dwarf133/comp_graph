import os


picDirect = "pictures/"


def sign(x):
    return 0 if x == 0 else -1 if x < 0 else 1


def clearPNGs():
    for file in os.listdir(picDirect):
        if file.endswith(".bmp") or file.endswith(".png"):
            os.remove(picDirect + file)
            print(f"File {file} removed!")