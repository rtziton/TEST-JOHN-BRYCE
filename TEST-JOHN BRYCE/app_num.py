import os

# Specify the path for the new folder and subfolder
folder_path = 'tools'
subfolder_path = os.path.join(folder_path, 'numbers')

# Check if the folder "tools" already exists
if not os.path.exists(folder_path):
    # Create the folder "tools"
    os.makedirs(folder_path)
    print(f'The folder "{folder_path}" has been created.')

# Check if the subfolder "tools/numbers" already exists
if not os.path.exists(subfolder_path):
    # Create the subfolder "numbers" inside "tools"
    os.makedirs(subfolder_path)
    print(f'The subfolder "{subfolder_path}" has been created.')
else:
    print(f'The subfolder "{subfolder_path}" already exists.')
