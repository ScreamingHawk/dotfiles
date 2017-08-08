from pathlib import Path
import platform
import os
import shutil

# Default the destination to the home location
userHome = str(Path.home())
# Ignore a couple files
ignoreList = [".gitkeep"]

def requestDestination():
	""" Request the desination from the user. """
	return input("> Enter destination: ({})".format(userHome)) or userHome


def folderCopy(src, dest):
	""" Copy the contents of the src folder to the dest folder. """
	print("Copying from {}".format(src))
	for filename in os.listdir(src):
		if filename not in ignoreList:
			print("Copying {}".format(filename))
			shutil.copy(src+filename, dest)


if __name__ == "__main__":
	# Get destination
	destination = requestDestination()
	print("Copying to {}".format(destination))
	# Copy shared folder first in case OS specific overrides
	folderCopy('shared'+os.sep, destination)
	if platform.system() == 'Windows':
		# Windows
		folderCopy('windows'+os.sep, destination)
	else:
		# There is no Apple
		folderCopy('linux'+os.sep, destination)


