#File Contains the Code of Duplicate files detector and then sending the email to specified recipient


from sys import *
import os
import hashlib
import time

total_scanned_file = 0
file_path = " "

def CalculateCheckSum(path, blocksize = 512):
	global total_scanned_file
	total_scanned_file = total_scanned_file + 1
	
	file_descriptor = open(path,"rb")
	hash_obj = hashlib.md5()  #here we select the algorithm from the hashlib module.

	Buffer = file_descriptor.read(blocksize)
	while len(Buffer) > 0:
		hash_obj.update(Buffer)
		Buffer = file_descriptor.read(blocksize)

	file_descriptor.close()
	
	return hash_obj.hexdigest() # hexdigest will create hexadecimal string of our checksum.


def DirectoryTraversal(path):
	
	directory = " "
	duplicate_files = {}   #dictonary.
	
	if not os.path.exists(path):
		print("Failure : please enter valid path")
		exit()

	#if not os.path.isabs(path):       #here we check the path is absolute or not.
	directory = os.path.abspath(path)  #this function creates the path as absolute and returns the op
			                           # as string

	for Folder, Subfolder, Filename in os.walk(directory):
		
		for file in Filename:
			
			actual_path = os.path.join(Folder,file)
			hash = CalculateCheckSum(actual_path)

			if hash in duplicate_files:  #checksum is already present
				duplicate_files[hash].append(actual_path)
			else:                  #checksum not present then add it into the dictonary
				duplicate_files[hash] = [actual_path]  

	
	return duplicate_files

def Generate_list_duplicate_files(dict_duplicates):
	list_duplicates_files = list(filter(lambda x : len(x) > 1, dict_duplicates.values())) #nested list
	counter = 0
	files_duplicates = []  #this file for write in the file which files are going to deleted.


	if(len(list_duplicates_files) > 0):
		#print("There are duplicate files")
		for lists in list_duplicates_files:
			counter = 0
			for file_path in lists:
				counter = counter + 1
				if counter >= 2:
					files_duplicates.append(file_path)

	else:
		print("There is no duplicate files")
		exit()
		
	return files_duplicates


def Generate_Log_file(dup_files,Folder="Duplicate_Files"):
	global file_path

	if not os.path.exists(Folder):
		os.mkdir(Folder)
	
	file_path = os.path.join(Folder,"_filelog-{}.txt".format(time.ctime()))
	file_path = (file_path.replace(" ","_").replace(":","-"))


	file_descriptor = open(file_path,"w")

	for element in dup_files:
		file_descriptor.write("{}\n".format(element))

	file_descriptor.close()

	
def Display_Statistics(dup_files):
	print()
	print("----Statistics Of Operations----")
	print("Total Number of file scanned           : ",total_scanned_file)
	print("Total Number of duplicate files        : ",len(dup_files))
	print("Folder\\file name of file log created  : ",file_path)

	input_text = input("Are you want to delete duplicate files [y/n] ? ")
	if (input_text == "y") or (input_text == "Y"):
		for file in dup_files:
			os.remove(file)
	elif (input_text == "n") or (input_text == "N"):
		exit()


def main():
	
	print("----Duplicate file Detector----")

	if(len(argv) != 2):
		print("Error : Invalid number of arguments")
		exit()

	if(argv[1]=="-h") or (argv[1]=="-H"):
		print("Help : It's a Directory cleaner script")

	if(argv[1]=="-u") or (argv[1]=="-U"):
		print("Usage : Provide the absolute path of the target directory")

	dict_duplicates = {}
	dup_files = []

	dict_duplicates = DirectoryTraversal(argv[1])
	
	if dict_duplicates != 0:
		dup_files = Generate_list_duplicate_files(dict_duplicates)
	
	
	Generate_Log_file(dup_files)

	Display_Statistics(dup_files)

if __name__ == '__main__':
	main()
