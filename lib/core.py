#!/usr/bin/env python

import os
import subprocess, sys
def engine(file, wordlist):
    if wordlist:
        wfile = open(wordlist, 'r').readlines()
        for password in wfile:
            password = password.strip() 
            comm = "truecrypt -t --non-interactive %s -p %s"%(file, password)
            exec1 = subprocess.Popen(comm, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            result = exec1.stderr.read()
            if 'Incorrect' in result:
                sys.stdout.write("\r[?] Attempting With : %s"%password)
                sys.stdout.flush()
                
            else:
                print "\n[+] Password Found : %s"%password
                print "[+]Done."
                break
                
