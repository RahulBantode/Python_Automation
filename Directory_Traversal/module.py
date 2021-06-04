'''===============================================================
	This is module file which imported in main python file
	or we can use this module.py file any of other application
	where we need such kind of functionality. 
	Modular way leads to reusability of code.
   ===============================================================
'''
from sys import *
import os

'''====================================================
	This function for display all files with its size
   ====================================================
'''
def Files_With_Size(path):
	file_dict = {}

	if not os.path.exists(path):
		return -1
		
	for Folder,sub_folder,filename in os.walk(path):
		
		for file in filename:
			file_pointer = os.path.join(Folder,file)
			file_size = os.stat(file_pointer).st_size
			#print("\t**  {}\t({})".format(file,file_size))	
			file_dict[file] = file_size

	return file_dict

'''====================================================
	This function for display the files having size 
	greater than input
   ====================================================
'''
def Files_With_Condition_Size(path,byte_size):
	File_list = []
	
	for Folder,sub_folder,filename in os.walk(path):
		
		for file in filename:
			file_pointer = os.path.join(Folder,file)
			file_size = os.path.getsize(file_pointer)
			if file_size >= int(byte_size):
				#print("\t**  {}\t({})".format(file,file_size))	
				File_list.append(file)

	return File_list


'''=======================================================
	This function find the files according to extension in it/
	or substring which is passed through command line
   =======================================================
'''
def Find_the_File(path,sub_string):
	file_list = []

	for Folder,sub_folder,filename in os.walk(path):
		
		for file in filename:
			file_pointer = os.path.join(Folder,file)
			if file_pointer.find(sub_string) != -1:
				#print("** {}".format(file))
				file_list.append(file)

	return file_list

'''===========================================================
	This function satisfies two condition one is file size
	greater than input and substring is present in that file
	then print all such files which satisfies above condition.
   ===========================================================
'''
def Find_File_size_substring(path,byte_size,sub_string):
	file_list = []


	for Folder,sub_folder,filename in os.walk(path):
		
		for file in filename:
			file_pointer = os.path.join(Folder,file)
			file_size = os.path.getsize(file_pointer)
			if (file_size >= int(byte_size)) and (file_pointer.find(sub_string) != -1):
				file_list.append(file)

	return file_list
