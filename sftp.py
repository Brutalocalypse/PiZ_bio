import os

# Brutal in the following command comes from the ssh config on the pi
#	it is simply shorthand for Brutalocalypse@fleshpound (Jordan's computer
#	and hostname)
# scp allows uploading of files from the commandline
# Input: a local path to the file to upload
def upload_file(fpath):
	os.system("scp %s brutal:Desktop/" % fpath)
