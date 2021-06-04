'''========================================================================================
   Problem statement :- Directory traversal using python.

   	The program is designed in the modular way where main file contains entry point function
   	and some basic function and the another file which is module.py file which contains
   	all the logic for the particular problem statement.

   	input - Input is getting from the command line as problem statement need so when giving
    		so please give the input in proper way as suggested in the help function which
    		are called first to see how to write an commands.
   ========================================================================================
'''

from sys import *
import os
from module import *

'''====================================================
	This function traverse through the directory
   ====================================================
'''
def Directory_traversal(path):
	
	if not os.path.exists(path):
		print("Failure : please enter valid path")
		exit()

	directory = os.path.abspath(path)

	'''================================
		++   Main Directory
		--	 Sub  Directory
		**	 Files in that directory
	   ================================
	'''
	print("Files in the directory : ",directory)
	print()
	
	for Folder,sub_folder,filename in os.walk(directory):
		print("++",Folder)
		
		for sub in sub_folder:
			print("\t--",sub)

		for file in filename:
			print("\t**",file)


def help():
	print("---Usage and command line input to the program---")
	print()
	print("  File path should be absoulute ")
	print("  without arguments - <executable>")
	print("  Traverse  - <executable> <absoulute path name>")
	print("  File size - <executable> <absoulute path name> <-s>")
	print("  Find File - <executable> <absoulute path name> <-f> <file substring>")
	print("  File size greater than - <executable> <absoulute path name> <-s> <size_of_file in byte>")
	print("  File size and extensin - <exe> <abs path name> <-s> <-f> <size> <exten/substring>")
	print()
	print("  NOTE / All the file arguments should be in above format because this is command line input")

def main():
	
	'''====================================================================
		Note :- The project are in modular way for that most of functions
		        are written in module.py file
	   ====================================================================
	'''
	print("---Directory/File traversal---")
	help()
	print()
	'''========================================
		Directory_traversal(directory) function
	   ========================================
	'''
	if len(argv) == 1:		
		directory = os.getcwd()
		Directory_traversal(directory)
		exit()

	if len(argv) == 2:
		Directory_traversal(path=argv[1])
		exit()
	'''=======================================================================
		Function covered in this block
		1. Files_With_Size(path)
	   =======================================================================
	'''
	if len(argv) == 3:
		if (argv[2] == "-s") or (argv[2] == "-S"):
			
			dictonary_file = Files_With_Size(path=argv[1])
			
			if dictonary_file != -1:
				print("File with size : ")
				for key,value in dictonary_file.items():
					print("\t{}  ({}) ".format(key,value))
			else:
				print("Failure : Directory/file not found (please type -h or -H)")
			
		exit()

	'''=======================================================================
		Function covered in this block 
	   	1. Files_with_Condition_Size(path,byte_size)
	   	2. Find_the_File(path,substring)
	   =======================================================================
	'''
	if len(argv) == 4:
		if not os.path.exists(argv[1]):
			print("Failure : Directory/file not found (please type -h or -H)")
			exit()

		if (argv[2] == "-s") or (argv[2] == "-S"):
			
			file_list = Files_With_Condition_Size(path=argv[1],byte_size=argv[3])
			
			if len(file_list) != 0:
				print("Filename which size greater than : ",argv[3]," bytes")
				for file in range(len(file_list)):
					print("\t{}".format(file_list[file]))
			else:
				print("There is no file greater than size you entered")
		
		else:

			file_list = Find_the_File(path=argv[1],sub_string=argv[3])
			
			if len(file_list) != 0:
				print("Searched file with given extension/substring = ",argv[3])

				for file in range(len(file_list)):
					print("\t{}".format(file_list[file]))
			else:
				print("There is no file present with your extension/sub_string")
		
		exit()	

	'''=======================================================================
		This block print the files which satisfies both condition as file
		with substring and file size greater than input given from cmd line
	   =======================================================================
	'''
	if len(argv) == 6:
		if not os.path.exists(argv[1]):
			print("Failure : Directory/file not found (please type -h or -H)")
			exit()

		file_list = Find_File_size_substring(path=argv[1],byte_size=argv[4],sub_string=argv[5])
		
		if len(file_list) != 0:
			print("Files having executable = {} size greater than = {}".format(argv[5],argv[4]))

			for file in range(len(file_list)):
				print("\t{}".format(file_list[file]))
		
		else:
			print("There is no file present with your condition.")

		exit()

if __name__ == '__main__':
	main()
