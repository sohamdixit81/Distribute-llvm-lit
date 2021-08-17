# importing os module
import os
# importing shutil module
import shutil

# path
def transfer():
	path ='/home/soham/scripts/input'

	# List files and directories
	print("Before copying file:")
	print(os.listdir(path))


	# Source path
	#src ='/home/soham/scripts/input'

	# Destination path
	#dest ='/home/soham/scripts/output'

	# Copy the content of
	# source to destination
	destination = shutil.copytree('/home/soham/scripts/input', '/home/soham/scripts/output')

	# List files and directories
	print("After copying file:")
	print(os.listdir(path))

	# Print path of newly
	# created file
	print("Destination path:", destination)
