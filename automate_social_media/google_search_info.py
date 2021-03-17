#demonstration of searching some data and get the information about that topic

from pywhatkit import *

def main():
    search_something = input("Type keyword or website to search on google : ")

    try:
        info(search_something,lines = 5)
        print("Information is getting from the ggole and display output on console...")
    except:
        print("Network issue occured")

if __name__ == "__main__":
    main()
