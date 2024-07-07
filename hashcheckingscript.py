#!/usr/bin/python
import os

#This script requires some initial setup to perform correctly, run the command md5sum /etc/shadow > passwordhash.txt in the / directory (or change the code on line 12 to reflect the correct file path), this will 
#give the script the baseline hash value to check against. 

#run md5sum on shadow file and save output to newhash.txt
runhash = ("md5sum /etc/shadow > newhash.txt")  
newfile = os.system(runhash)

#open passwordhash.txt file and check values
with open("/passwordhash.txt") as file:
    hashes = file.readlines() 
    print("Original hash was: %s" % hashes)

#open newhash file and check values
with open("newhash.txt") as file2:
    hashes2 = file2.readlines()
    print("New hash created was: %s" % hashes2)
    
#check if value stored in new file is the same as baseline file, inform user if they are different values.
if hashes == hashes2:
    print("No changes since last check")
else:
    print("md5 hash has changed, if this is legitimate, please update baseline hash file")
    
#This script checks the contents of a file named passwordhash.txt to a new file it creates named newhash.txt. If the file has been changed in any way since the original passwordhas.txt file was created
#the script will alert the user. 
