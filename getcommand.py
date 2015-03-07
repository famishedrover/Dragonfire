#!/usr/bin/python
import sys
import api
from lxml import etree
from api import Data
from subprocess import call
import time


def command(speech_object):
	previous_command = ""
	while(True):
		line = speech_object.readline()
		if(line.startswith("sentence1: ")):
			com = line[15:-6]
			if (previous_command == com):
				continue
			print com
			if (com == "DRAGON FIRE"):
				userin = Data([" "]," ")
				userin.espeak("Yes sir")
				previous_command = com
			if (com == "WHAT IS YOUR NAME"):
				userin = Data([" "]," ")
				userin.espeak("My name is Dragonfire.")
				previous_command = com
        		if(com == "OPEN FILE MANAGER"):
				userin = Data(["sudo","pantheon-files"],"File Manager")
				userin.espeak("File Manager")
				userin.interact(0)
				previous_command = com
			if(com == "OPEN WEB BROWSER"):
				userin= Data(["sensible-browser"],"Web Browser")
				userin.espeak("Web Browser")
				userin.interact(0)
				previous_command = com
			if(com == "SHUT DOWN THE COMPUTER"):
                                userin= Data(["sudo poweroff"],"Shutting down")
                                userin.espeak("Shutting down")
				userin.interact(3)
                                previous_command = com
            
			
			

if __name__ == '__main__':
	try:
		command(sys.stdin)
	except KeyboardInterrupt:
		sys.exit(1)
