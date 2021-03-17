#Demonstration of sending the text messege on whatsapp using specified number...

from pywhatkit import *
def main():
    mob_no = input("Enter the mobile number with country code (i.e +91) : ")
    messege = input("Enter the messege to send on whatsapp : ")

    try:
        #this mb. number is of nitin
        sendwhatmsg(mob_no,messege,00,9)
        print("Messege is sent ")
    except:
        print("Network error occured")

if __name__ == "__main__":
    main()