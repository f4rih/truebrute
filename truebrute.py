#!/usr/bin/env python
# TrueBrute Version 1.0 Beta
# Author : Fardin Allahverdinazhand
# Year : 2014

import optparse, os, sys
from lib import core
class main:
    def __init__(self):
        if not os.getuid()==0:
            sys.exit("\nOnly root can run this script\n")
        usage = '''usage: truebrute.py [options]
truebrute.py -t [TrueCrypt File] -w [Wordlist File]   
*-* 
Description :
TrueBrute Version 1.0 Beta
Digital Forensics - TrueCrypt Brute Forcer
Written By Fardin Allahverdinazhand (0x0ptim0us)
Email : 0x0ptim0us@Gmail.com
Founder & Developer Of The Websploit Framework Project
*-*'''
        parse = optparse.OptionParser(usage=usage)
        parse.add_option('-t', '--truefile', help="TrueCrypt File")
        parse.add_option('-w', '--wordlist', help="Dictionary File")
        opt, args = parse.parse_args()
        self.truefile = opt.truefile
        self.wordlist = opt.wordlist
        if self.wordlist and self.truefile:
            print "[+] Attack Has Been Started ..."
            core.engine(self.truefile, self.wordlist)
        else:
            print "[!] Wordlist or TrueCrypt File Not Found !"
            print "[+] Use --help Switch For More Info."

if __name__ == "__main__":
    root = main()
    