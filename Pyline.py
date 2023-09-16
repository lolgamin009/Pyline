import os
import socket
import Funcs as funcions
import Commands

hostid = socket.gethostname()
hostip = socket.gethostbyname(hostid)

def mainloop():
    funcions.starttext()
    while True:
        dir = str(os.getcwd())
        cmdbef = dir + ">"
        global cmdinput
        cmdinput = input(cmdbef)
                            
mainloop()