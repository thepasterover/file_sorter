"""
Author: Boobalan R Shettiyar
Github: https://github.com/thepasterover
facebook ID : https://www.facebook.com/boopalan.shettiyar
"""

import os
import shutil

while 1:
    
    print("Welcome to Python File Sorter.")
    old_folder = input("\nWhich directories you want to check?\n\t(Copy"
                       " the exact location for eg: '\C:\example\example'): ")

    ending = input("\nWhat type of files you want to be moved? \n\t(for"
                   " eg: '.pdf', '.jpg', '.png'): ")

    dst = input("\nWhere do you want it to be moved?\n\t(Copy the exact"
                " location for eg: '\C:\example\example'): ")

    try:
        # Walk through the given directory as long as loop runs.
        for root, dirs, files in os.walk(old_folder.strip()):
            for file in files:

                #Search for files with specific extension.
                if file.endswith(ending.strip()):
                    path = os.path.join(root, file)
                    # Move the files to the given folder of destination.
                    shutil.move(path, dst.strip())
            break
        response = input("The files have been moved successfully!\n\t Do you want to continue? (Y/n): ")
        if response.lower() == 'n':
            break
    except shutil.Error:
        print("The files already exist in the specified directory or some other Error. Contact Author for more info!")
    
    
