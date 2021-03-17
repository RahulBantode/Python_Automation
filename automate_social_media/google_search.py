#demonstration of searching some text on google using python script

from pywhatkit import *

def main():
    search_something = input("Type keyword or website to search on google : ")

    try:
        search(search_something)
        print("Search will done on google please check your browser...")
    except:
        print("Network issue occured")

if __name__ == "__main__":
    main()
