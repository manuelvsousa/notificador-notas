import ConfigParser #Configuration files
import urllib #Page is up
import urllib2 #get source code
import sys
import ast
import json
import hashlib
from hashlib import md5
import urllib2

def get_sourcecode(link):
	response = urllib2.urlopen(link)
	m = hashlib.md5()
	m.update("Nobody inspects")
	print m.hexdigest()

get_sourcecode("http://google.com/")