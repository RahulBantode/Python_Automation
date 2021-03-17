'''Write a Program which gets backup of all files into the newly created zip file
and every time you are running this program backup.zip file will increment by 1 like
backup1.zip , backup2.zip, backup3.zip'''

#step 1 - figure out the zip file name for that purpose we create the function name backuptofolder which are more readable
from os import *
from zipfile import *

def backuptofolder(folder):
    #backup the entire content of the folder into zip files
    folder = path.abspath(folder)

    #figure out the filenames this code should based on what files are already exist

    number = 1
    while True:
        #here basename means folder name then underscore and number then .zip
        zipfilename = path.basename(folder) + '_' + str(number) + '.zip'

        #here we checking that zipfilename is exist in that location or not, if not exist then break it
        if not path.exists(zipfilename):
            break

        number = number + 1

    #step -2 create a zip file

    print("Creating ", zipfilename, ".....")
    #by using ZipFile function we are opening the zipfile in append mode according to second argument are passed into the function
    backupzip = ZipFile(zipfilename, "a")

    #step -3 Walk the directory tree and add the file and folder to zip file

    #walk the entire folder tree and compress the files into the zip files

    for foldername, subfolder, filenames in walk(folder):
        print("Adding files in ", foldername)
        #Add the current folder to zip file
        backupzip.write(foldername)

    #add all the files in this folder to the zip file

        for filename in filenames :
            newBase = path.basename(folder) + '_'

            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #dont backup the backup zip files

            backupzip.write(path.join(foldername,filename))
    '''
    Summarry of the above loop from for loop and nested for loop in it --
    
                You can use os.walk() in a for loop u, and on each iteration it will
                return the iteration’s current folder name, the subfolders in that folder,
                and the filenames in that folder.
                In the for loop, the folder is added to the ZIP file v. The nested for
                loop can go through each filename in the filenames list w. Each of these is
                added to the ZIP file, except for previously made backup ZIPs.
    '''

    backupzip.close()

    print("Done.....")



if __name__ == '__main__':

    backuptofolder(r"D:\Projects_pythons\organising_files\extracted_doc")
    # here folder is organising_files and we taking the backup of this folder into zip file

