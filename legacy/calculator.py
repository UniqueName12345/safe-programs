import os
import platform as p

def safe_print(thing):
    if p.system() == "Windows":
        os.system("echo {}".format(thing))
    else:
        os.system("echo \"{}\"".format(thing))

def safe_input(prompt):
    if p.system() == "Windows":
        os.system("set /p \"output={}: \"".format(prompt))
        return os.getenv("output")
    else:
        os.system("read -p \"{}: \" output".format(prompt))
        return os.getenv("output")

safe_print("A very safe calculator!")
answer = eval(safe_input("Enter a python string"))
print(f"The answer is {answer}")