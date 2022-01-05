#!/usr/bin/python3

import os
import sys
import shlex
import subprocess

name = "mysh"
command = [ "pwd", "cd", "ls", "exit"]


class shell:

    def pwd():
        try:
            print(os.getcwd())
        except Exception as err:
            self.error()
    
    def exit():
        try:
            sys.exit()
        except Exception as err:
            self.error()

    def cd(path): 
        try:
            os.chdir(path)
        except Exception as err:
            self.error()

        
    def ls(): 
        try:
            tmp = os.listdir()
            for i in tmp: print(i)
        except Exception as err:
            self.error()
    
    def error(self):
        err = "An error has occurred\n"
        print(err, file=sys.stderr)

def runShell(args, out=sys.stdout):
    subprocess.run(args, stdout=out, stderr=out)

def execute(cmd):
    p = shlex.split(cmd)
    l = len(p)
    if l==0:
        pass
    elif l==1: 
        exec(f'shell.{p[0]}()')
    elif l==2: 
        exec(f'shell.{p[0]}("{p[1]}")')
    elif l==3:
        exec(f'shell.{p[0]}("{p[1]}", "{p[2]}")')
    else:
        tc = f"shell.{p[0]}("
        for i in range(1, l+1):
            if i==l:
                tp = f'"{p[i]}"'
                tc += tp
            else:
                tp = f'"{p[i]}", '
                tc += tp
        tc += ")"
        exec(tc)
    

def batch_mode(path):
    with open(path, 'r') as f:
        for line in f:
            print(line.strip())
            processCommand(line)

        

while True:
    try:
        if len(sys.argv) == 2:
          batch_mode(sys.argv[1])
        else:
          cmd = input(f"{name}$ ")
          execute(cmd)
    except Exception as err:
        print("Error:", str(err))