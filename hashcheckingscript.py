#!/usr/bin/python
import os

runhash = ("md5sum /etc/shadow > newhash.txt")  
newfile = os.system(runhash)

with open("/passwordhash.txt") as file:
    hashes = file.readlines() 
    print("Original hash was: %s" % hashes)

with open("newhash.txt") as file2:
    hashes2 = file2.readlines()
    print("New hash created was: %s" % hashes2)

if hashes == hashes2:
    print("No changes since last check")
else:
    print("md5 hash has changed, if this is legitimate, please update baseline hash file")
    
