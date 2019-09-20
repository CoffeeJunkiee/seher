#!/usr/bin/env python 
# -*- coding: utf-8 -*-

### Libraries ###
import sys
import os
import getopt
import subprocess

### Global variable #### 
target  = ''

#Welcome message
def _print_message():
    print "_" * 50
    print
    print "┌─┐┌─┐┬ ┬┌─┐┬─┐"
    print "└─┐├┤ ├─┤├┤ ├┬┘"
    print "└─┘└─┘┴ ┴└─┘┴└─  Personalized Nmap scan"
    print 'By: InsaneGroove'
    print 'github.com/InsaneGroove'
    print '_' * 50

#Simple Usage
def usage():
    _print_message()
    print "Usage: seher -t target_host"
    print "-h --help                                    - Help"
    print "-t --target                                  - Target to scan"
    print "Example:"
    print "seher -t 192.168.2.10"
    sys.exit(0)

#Base to run scan
def run_scan(scan, stderr=None):
    return subprocess.check_output(scan, shell=True, stderr=stderr, universal_newlines=True)


#Handle some work
def main():
    global target
    
    if not len(sys.argv[1:]):
        print usage()
    
    # Read the commandline options
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h:t:",["help","target"])
    except getopt.GetoptError as err:
            print str(err)
            usage()
    
    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-t", "--target"):
            target   = a
        else:
            assert False, "Unhandled Option"
main()


#Set some work
def input_work():

    global target

    if not len(target):
        print "Please provide some input"
    elif target is not None:
        _print_message()
        print "[*]... Starting Scan for" , target 
        os.mkdir(target)
        sam_scan = "nmap -sC -sV -Pn --disable-arp-ping %s -oA %s/%s.scan" % (target, target, target)
        run_scan(sam_scan)
        print
        print "[!]... scan done!"
        print "[$] Look the folder called" , target
        print 
        print "( ͡° ͜ʖ ͡°) Thanks for using Seher!"

input_work()
