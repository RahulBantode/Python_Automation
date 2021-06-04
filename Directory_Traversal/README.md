Objective :-
	To Implement the directory traversal system using python 
  (system is like a UNIX/LINUX or any operating system command line interpreter works)

Description :-
	Implement the system like UNIX/LINUX commands line terminal which traverse the directory after passing the directory name to it 
  and many other functions on the file systems. Implement this type of system using python technology or we can say that, 
  to the system is file/directory manipulation and search the particular one.

The system supports following functionality :-
  1.	Application takes the directory name from user using command line prompt (the directory name/path should be absolute) 
      if relative path is given then search application search for current working directory only.and after getting an input 
      traverse through the directory and print all the files and subdirectory in it.
  2.	If user fails to give an input at the time of execution of application then system consider the current working directory 
      and traverse through it.
  3.	The format of the files ,sub-directory in directory looks like as follow :-

        ++<main_directory>
            --<sub_directory 1>
            --<sub_directory 2>
            **<file_name 1>
            **<file_name 2>
        ++<sub_directory in main directory>
            **<files within directory>
            
4.	The program should also supports the following command line options.
    a)	–s or –S   If user entered this literal followed by directory path then he will displays the file name with its file size.
    b)	–s or –S <file_size>  If user entered this combination with directory path then he will displays the files names 
        which size greater than input in size.
    c)	–f or –F <substring/extension> If user entered this combination followed by directory then he will displays the files names 
        with specified extensions.

5.	The program have one extension which accept the –s and –f i.e file size and file extension from user 
    and display those files who  satisfies above both criteria.

Note :- Repository contains the documetation please reffer tht documentation for better understanding.
