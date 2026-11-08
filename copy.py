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
	""" Copy the contents of the src folder to the dest folder.
	Files land directly in dest; subfolders map to ~/.config/<name>/.
	"""
	print("Copying from {}".format(src))
	for filename in os.listdir(src):
		if filename in ignoreList:
			continue
		srcPath = os.path.join(src, filename)
		if os.path.isdir(srcPath):
			destPath = os.path.join(dest, ".config", filename)
			print("Copying {} to {}".format(filename, destPath))
			shutil.copytree(srcPath, destPath, dirs_exist_ok=True)
		else:
			print("Copying {}".format(filename))
			shutil.copy(srcPath, dest)

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
	# Work config is optional; skip when moving between jobs
	if os.path.isdir('work'+os.sep) and os.listdir('work'+os.sep):
		if input("> Copy work config? (y/N) ").lower() == "y":
			folderCopy('work'+os.sep, destination)
