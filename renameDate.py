#Renaming files with American files dates to indian file dates
'''
What exactly you have to do here, you have to identify the filename with date format and then match
the filename with american-style format if it found then rename it by using shutil.move function with
indian-date format , and if you found the filename without date you have to ignore it.
'''
'''step-1 create regex (regular expression) for American-Style Dates
    1st part - Here program will need to import the necessary module and create regex that can identify
               MM-DD-YYYY date format.
'''

from re import *
from os import *
from shutil import *

def main():
    #create regex object pattern from MM-DD_YYYY pattern to search over the american date format
    date_pattern = compile(r"""^(.*?)                   #all the text before the date
                             ((0|1)?\d)-               #one or two digits for month means the first digit either 0 or 1
                             ((0|1|2|3)?\d)-           #one or two digits for day means the first digit either 0,1,2,3
                             ((19|20)\d\d)             #four digits for year
                             (.*?)$                    #all the text after the date
                             """, VERBOSE) #VERBOSE which are second argument which allows whitespacess and comments in the
                                   #first argument
    ''' for year-
    (Yes, this regex will accept some invalid dates such as 4-31-
    2014, 2-29-2013, and 0-15-2014. Dates have a lot of thorny special cases that
    can be easy to miss. But for simplicity, the regex in this program works well
    enough.)
    While 1885 is a valid year, you can just look for years in the 20th or 21st
    century. This will keep your program from accidentally matching nondate
    filenames with a date-like format, such as 10-10-1000.txt.
    '''

    #step 2 - Identify the date parts from the filenames
    '''     Now you have loop over the filename using os.listdir() function and under the 
            loop you have to match them with your regex object and then you have to move it
            and rename it. and the filename which doesnt have date you have to skip it
    '''
    #now change the working directory its an optional part

    chdir(r"D:\Projects_pythons\organising_files\rename_date")

    # . means current directory
    for american_filename in listdir('.'):
        #here we search filename with our regex object regex object is date_pattern and search is function for searching
        search_found = date_pattern.search(american_filename)

        #skip files without having any date format
        if search_found == None:
            continue

        #get the different parts of the filenmaes
        beforepart = search_found.group(1)
        monthpart  = search_found.group(2)
        daypart   = search_found.group(4)
        yeartpart  = search_found.group(6)
        afterpart  = search_found.group(8)

        #step 3 - form the new filenames and rename the files

        indian_filenames = beforepart + daypart + '-' + monthpart + '-' + yeartpart + afterpart
        #get the full absolute file path

        absworkingdir = path.abspath('.')
        american_filename = path.join(absworkingdir,american_filename)
        indian_filenames  = path.join(absworkingdir,indian_filenames)

        #Rename the files
        print('Renaming "%s" to "%s".... ' % (american_filename, indian_filenames))
        move(american_filename,indian_filenames)



if __name__=="__main__":
    main()




