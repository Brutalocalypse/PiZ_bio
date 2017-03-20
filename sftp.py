import os

# Brutal in the following command comes from the ssh config on the pi
#	it is simply shorthand for Brutalocalypse@fleshpound (Jordan's computer
#	and hostname)
# scp allows uploading of files from the commandline
# Input: a local path to the file to upload
def upload_file(fpath):
	# os.system("scp %s brutal:Desktop/" % fpath) # Desktop connection
	
	#cmd = "sh -c 'scp %s venom:Desktop/'" % fpath
	#print "'", cmd, "'"
	#os.system("%s" %cmd) # Laptop connection
		# bug where hostname isn't recognized even though it can be used in terminal just fine

	os.system("scp %s LethalInjection@192.168.137.1:Desktop/" %fpath) # Laptop connection
		# requires password prompt
