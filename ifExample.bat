# Task 2 (Batch File)

# Create if-folder if one of the folder is called new_folder

if exist new_folder (
    mkdir if_folder
)

# Create Hyperion-Development-Folder, if if-Folder exists
# Create new folder "new_projects", if it does not exist

if exist if_folder ( 
    mkdir hyperionDev
) else (
    mkdir new_projects
)