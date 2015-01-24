#!/usr/bin/env python
# -*- coding: utf-8 -*-
#imports

import commands
import re



def main():
    interface_wireless = commands.getoutput("iwconfig")
    interface_wireless = interface_wireless.split("\n")
    for line in interface_wireless:
        if(re.search("802.11",line)):
            interface_wireless = line.split(" ")[0].strip()
    work = commands.getoutput("airmon-ng start "+ interface_wireless)
    if(re.search("monitor mode enabled on",work)):
        print("Monitor Mode Enabled: \033[92m SUCESS\033[0m")
    else:
        print("Monitor Mode Enabled: \033[91m FAILED\033[0m")
        exit()
    ret = commands.getoutput("airodump-ng "+interface_wireless)
    print ret
    
    
main()