#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os
import sys
import time 

def _print_welcome_():
    print
    print "Welcome to Seher!"
    print 
    print "[!] Please run this script as root!"
    time.sleep(1)
    print "[*] Getting everything ready for a nice usage..."
    time.sleep(2)



def _all_done():
    print "[*] Everything has been set up!"
    print
    print "Thank you for using Seher ( ͡° ͜ʖ ͡°)"


def setup():
    _print_welcome_()

    os.system("cp seher.py /usr/local/bin/seher")
    os.system("chmod +x /usr/local/bin/seher")

    _all_done()

setup()

