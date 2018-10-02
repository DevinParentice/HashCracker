import hashlib
import os
import time
import itertools
from progress.bar import Bar
import sys

choice = input("What type of cracking would you like?\n\n1. MD5 Hash\n2. SHA-256\n")

if choice == "1":
    attackType = "md5"
if choice == "2":
    attackType = "sha256"

password = input("Paste your hash here: ")

choice = input("\nChoose your cracking method:\n\n1. Brute Force\n2. Dictionary\n")

if choice == "1":
    uppercase = ["A", "B", "C", "D","E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowercase = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "?", "@", "#", "$", "%", "*", "&"]

    masterList = []

    start = time.time()
    CharLength = 1

    params = input("\n\nWould you like to add lowercase letters? (Y/N): ")

    if params == "Y":
        masterList.extend(lowercase)

    if params == "N":
        pass

    params7 = input("\n\nWould you like to add uppercase letters? (Y/N): ")

    if params7 == "Y":
        masterList.extend(uppercase)

    if params7 == "N":
        pass

    params2 = input("\nWould you like to add numbers? (Y/N): ")

    if params2 == "Y":
        masterList.extend(numbers)

    if params2 == "N":
        pass

    params3 = input("\nWould you like to add symbols? (Y/N): ")

    if params3 == "Y":
        masterList.extend(symbols)

    if params3 == "N":
        pass

    params4 = input("\nWhat is the minimum length of the password? ")
    minLength = params4

    params5 = input("\nWhat is the maximum length of the password? ")
    maxLength = params5

    params6 = input("\nAll settings loaded. Continue? (Y/N): ")

    if params6 == "Y":
        pass
    elif params6 == "N":
        exit()

    counter = 1
    attempt = 1
    found = False

    for CharLength in range(25):
        passwords = (itertools.product(masterList, repeat = CharLength))

        if int(CharLength) < int(minLength):
            pass
        elif int(CharLength) > int(maxLength):
            pass
        else:

            print("\nTrying all passwords that are " + str(CharLength) + " characters in length.")
            time.sleep(2)
            for i in passwords:
                counter += 1
                i = str(i)
                i = i.replace("[", "")
                i = i.replace("]", "")
                i = i.replace("'", "")
                i = i.replace(" ", "")
                i = i.replace(",", "")
                i = i.replace("(", "")
                i = i.replace(")", "")
                if attackType == "md5":
                    hashedGuess = hashlib.md5(i.encode('utf-8')).hexdigest()
                elif attackType == "sha256":
                    hashedGuess = hashlib.sha256(i.encode('utf-8')).hexdigest()

                if hashedGuess == password:
                    end = time.time()
                    timetaken = int(end - start)
                    print("\n\n[+] Password found: " + i)
                    print("\n\nFound it in " + str(timetaken) + " seconds and " + str(counter) + " attempts")
                    print("(" + str(int(counter / timetaken)) + " attempts per second.)")
                    input("Press enter when you have finished.")
                    found = True
                    exit(0)

                else:
                    print("Tried Password (" + str(attempt) + "): " + i)
                    attempt += 1

if choice == "2":
    dictionaries = os.listdir("/Users/devinparentice/Documents/Cracker/")
    txtFiles = list(filter(lambda x: x[-4:] == '.txt', dictionaries))
    start = time.time()
    attempt = 1

    check = input("\nFound " + str(len(txtFiles)) + " dictionaries. Continue? (Y/N): ")

    if check == "Y":
        for n in range(len(txtFiles)):
            with open(txtFiles[0], "r+") as f:
                for line in f:
                    line = line.replace("\n", "")
                    if attackType == "md5":
                        hashedGuess = hashlib.md5(line.encode('utf-8')).hexdigest()
                    elif attackType == "sha256":
                        hashedGuess = hashlib.sha256(line.encode('utf-8')).hexdigest()
                    if password == hashedGuess:
                        end = time.time()
                        timetaken = int(end - start)
                        print("\n\n[+] Hash has been cracked: " + line)
                        print("\n\nFound it in " + str(timetaken) + " seconds and " + str(attempt) + " attempts")
                        print("(" + str(int(attempt / timetaken)) + " attempts per second.)")
                        ex = input("\nPress enter to exit the program.")
                        exit(0)
                    else:
                        print("\rPassword tried (" + str(attempt) + "): " + line)
                        attempt += 1
            txtFiles.pop(0)

    if check == "N":
        exit(0)
