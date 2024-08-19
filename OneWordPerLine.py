#script to read txt file and put all words into a new text file 1 word per line

import os


class One_Word_Per_Line:
    
    def __init__(self):
        inFile = input("Enter file name: ")
        outFile = input("Enter output file name: ")
        with open(inFile, 'r') as file:
            lines = file.readlines()

        with open(f'{outFile}.txt', 'w') as file:
            for line in lines:
                words = line.split()
                for word in words:
                    file.write(word + '\n')
            


