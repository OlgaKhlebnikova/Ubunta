import subprocess
import string


def chek (command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8", universal_newlines=True)
    if text in result.stdout:
        return True
    else:
        return False

def chek_2 (command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8", universal_newlines=True)
    tab = str.maketrans(string.punctuation, " " * len(string.punctuation))
    new_res = (result.stdout).translate(tab).split()
    print(new_res)
    if text in new_res:
        return True
    else:
        return False
if __name__ == "__main__":
    command = "cat /etc/os-release"
    text = "22.04.1"
    text2 = "22/04/1"
    text3 = "jammy"
    res = chek(command, text)
    print(f"res = {res}")
    res2 = chek(command, text2)
    print(f"res2 = {res2}")
    res3 = chek_2(command, text3)
    print(f"res3 = {res3}")
    res4 = chek_2(command, text)
    print(f"res4 = {res4}")
