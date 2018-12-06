#!/usr/bin/python
import os
import time
import subprocess

softs = ['GitHub Desktop', 'Deezer', 'Enpass', 'GitKraken', 'PhpStorm', 'Microsoft Teams', 'Skype', 'Utilities/Terminal', 'Google Chrome', 'Sublime Text']

for soft in softs :
	subprocess.call(["/usr/bin/open",  "-a", "/Applications/"+soft+".app"])