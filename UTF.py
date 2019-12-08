from consolemenu import ConsoleMenu  # https://console-menu.readthedocs.io/en/latest/
from consolemenu.items import SubmenuItem, FunctionItem
from colorama import Fore, Back
import os

def utf_menu():
    menu = ConsoleMenu("Decimal number convertor & File Decoder", "Created with Python")

    submenu = ConsoleMenu("About Us")
    submenu.prologue_text = "This is Decimal number convertor which takes a decimal number as a input and shows " \
    						"number's Unicode, UTF-8 and single character. Created by Vilnius Gediminas " \
    						"Technical University PRIfs 18/6 student - Rimvydas Kanapka." \
                            " This program is created for Architecture of Computers and Computer Networks."

    menu.append_item(FunctionItem("GET Unicode, UTF-8 & Char of a Decimal Number", get_info))  # First menu item
    menu.append_item(FunctionItem("Decode File", decode))  # Second menu item
    menu.append_item(SubmenuItem("About Us", submenu, menu=menu))  # Third menu item
    menu.show()

def get_info():
    number = 1

    print("Enter {-1} if you want to quit.\n")

    while number != -1:
        try:
            number = int(input("Enter a decimal number: "))

            if number == -1:
                break
            #print("[ Binary: " + str(bin(number))[2:] + " | " + "Total digits: " + str(len(str(bin(number))) - 2) + " ]")
            print(Fore.GREEN + "Unicode: U+" + str(hex(number))[2:].upper())

            if number <= 127:
                #print("Operating with 1 byte (8 bits): ")
                byte1 = str(bin(number))[2:]
                byte1 = (8 - len(byte1)) * "0" + byte1
                print(("UTF-8: " + hex(int(byte1, 2))[2:]).upper())
            elif 128 <= number and number <= 2047:
                #print("Operating with 2 bytes (16 bits): ")
                byte2 = "10" + str(bin(number)[-6:]) # take 6 digits from binary end and ad 10 in front
                byte1 = str(bin(number)[:-6]) # read everything that's left in our binary
                byte1 = byte1[2:] # take out first two symbols, caus that's unnecessary "0b"
                byte1 = "11" + (6-len(byte1))*"0" + byte1 # in front it always will be 11 & added additional zeros after if length is not enought
                print(("UTF-8: " + hex(int(byte1, 2))[2:] + " " + hex(int(byte2, 2))[2:]).upper()) # no need to print first 2 digits 0x
            elif 2048 <= number and number <= 65535:
                #print("Operating with 3 bytes (24 bits): ")
                byte3 = "10" + str(bin(number)[-6:]) # take 6 digits from binary end and ad 10 in front
                byte2 = str(bin(number)[-14:-6]) # read from -14 to -6 to get 6 bits (we will add 2 more)
                byte2 = "10" + byte2[2:] # take out first two symbols, caus that's unnecessary "0b"
                byte1 = str(bin(number))[2:]
                if len(byte1) > 12: # checking if there are digits left for byte 3
                    byte1 = byte1[:len(byte1) - 12]
                else:
                    byte1 = ""
                byte1 = "1110" + (4 - len(byte1)) * "0" + byte1
                print(("UTF-8: " + hex(int(byte1, 2))[2:] + " " + hex(int(byte2, 2))[2:] + " " + hex(int(byte3, 2))[2:]).upper()) # no need to print first 2 digits 0x
            else:
                #print("Operating with 4 bytes (32 bits): ")
                byte4 = "10" + str(bin(number)[-6:]) # take 6 digits from binary end and ad 10 in front
                byte3 = str(bin(number)[-14:-6]) # read from -14 to -6 to get 6 bits (we will add 2 more)
                byte3 = "10" + byte3[2:] # take out first two symbols, caus that's unnecessary "0b"
                byte2 = str(bin(number))[2:] # taking out 0b
                byte1 = str(bin(number))[2:]
                if (len(byte2) == 17):
                    byte2 = "100" + byte2[:5]
                else:
                    byte2 = "10" + byte2[-18:-12]
                if (len(byte1) > 18): # if for checking if any digits left to put in to byte 1
                    byte1 = byte1[:len(byte1) - 18]
                    byte1 = "11110" + "0" * (3 - len(byte1)) + byte1
                else:
                    byte1 = "11110000" # byte value if there won't be any digits left

                print(("UTF-8: " + hex(int(byte1, 2))[2:] + " " + hex(int(byte2, 2))[2:] + " " + hex(int(byte3, 2))[2:] + " " + hex(int(byte4, 2))[2:]).upper()) # no need to print first 2 digits 0x
            #print(Back.RED + "File doesn't exist. Try other name." + Back.BLACK) type error
            print("Char: " + str(chr(number)) + Fore.WHITE)

        except ValueError:
            print(Fore.GREEN + "That's not decimal number!" + Fore.WHITE)

def decode():

    print("Enter a file name (with type) which you need to decode.\n")
    file_name = "none"

    while not os.path.isfile(file_name):
        file_name = input()

        if not os.path.isfile(file_name):
            print(Back.RED + "File " + file_name + " doesn't exist!" + Back.BLACK)


    print("\n" + Back.GREEN + "File " + file_name + " exist!" + Back.BLACK)

    f_result = open(file_name[:-4] + "_decoded.txt", "w")


    cp437 = open("CP437.txt", "r")
    content = cp437.readlines()
    for i, line in enumerate(cp437):
        if i == 1365:
            print(line)
            break
    cp437.close()

    take_from_file = open(file_name, "r", encoding='ISO-8859-1')

    for char in take_from_file.read():
        if ord(char) > 127: # if larger than 127 it mean symbol is unknows
            # CONVERTING character larger than 127 here

            unicode1 = hex(ord(char)) # char unicode of unknown symbol

            for line in content:
                if unicode1 in line:
                    unicode2 = line[5:12] # new unicode from cp437 table
                    
                    sk = int(unicode2, 0) # With the 0x prefix, Python can distinguish hex and decimal automatically.
                    ans = chr(sk)

            f_result.write(ans)
        else:
            f_result.write(char)

    take_from_file.close()
    f_result.close()

    print(Back.GREEN + "File " + file_name + " decoded to a file " + file_name[:-4] + "_decoded.txt" + " successfully!" + Back.BLACK + "\n")
    input("Press Enter to continue...")

utf_menu()