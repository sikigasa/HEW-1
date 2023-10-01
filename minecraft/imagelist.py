import os

def list_path():
    i_path = []
    for root, dirs, files in os.walk(".\\media\\images"):
        for fi in files:
            i_path.append(fi)

    return i_path