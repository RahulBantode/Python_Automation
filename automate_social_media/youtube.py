#demonstration of sending or open the youtube video using python script

from pywhatkit import *

def main():
    video = input("Enter the video name/url to view : ")
    try:
        playonyt(video)
        print("video is playing on youtube")
    except:
        print("Network issue occured")

if __name__ == "__main__":
    main()
