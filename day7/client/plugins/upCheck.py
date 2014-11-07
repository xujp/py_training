#!/usr/bin/env python

import commands

def monitor():
    shell_command = "uptime"
    
    status , result = commands.getstatusoutput(shell_command)
    
    if status != 0:
        value_dict = {'status': status} 
    else:
        value_dict = {
            'result' : result,
            'status' : status
        }
    return value_dict

if __name__ == "__main__":
    print monitor()
    
    

