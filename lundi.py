#!/usr/bin/python
import os
import time
import subprocess

softs = ['GitHub Desktop', 'Spotify', 'Enpass', 'PhpStorm', 'Microsoft Teams', 'Utilities/Terminal', 'Google Chrome', 'Sublime Text', 'Docker', 'Microsoft Outlook']

for soft in softs :
	subprocess.call(["/usr/bin/open",  "-a", "/Applications/"+soft+".app"])