import os

# Get the current working directory
print("Current Working Directory:", os.getcwd())

# Change the current working directory
os.chdir('/tmp')
print("Changed Working Directory:", os.getcwd())

# List all files and directories in the current directory
print("Files and Directories in /tmp:", os.listdir('/tmp'))

# Create a new directory
os.mkdir('test_dir')
print("Created 'test_dir'")

# Rename the directory
os.rename('test_dir', 'renamed_test_dir')
print("Renamed 'test_dir' to 'renamed_test_dir'")

# Remove the directory
os.rmdir('renamed_test_dir')
print("Removed 'renamed_test_dir'")

# Get an environment variable
home_dir = os.getenv('HOME')
print("Home Directory from Environment Variables:", home_dir)

# Execute a system command
os.system('echo Hello, World!')
