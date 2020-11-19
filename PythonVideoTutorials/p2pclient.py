# Imports
from socket import *
from tkinter import *
from os import *
from getpass import *
from threading import *

# Sockets and constants
s1 = socket(AF_INET, SOCK_STREAM)
queue = 1

# Host name and port extraction
def BindScan(port):
    s1.bind((gethostname(), port))
    return str(gethostname()), str(s1.getsockname()[1])

# Key generation
print(' '.join(BindScan(0)))