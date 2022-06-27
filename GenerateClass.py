#import random library to choice Charactors
import random

from tkinter import messagebox as mb


class Generate_Random_Password:
    #all valid symbols
    __gen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
             "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z",
             "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
              "T", "U", "V", "W", "X", "Y", "Z", "~", "!", "?", "@", "#", "$", "%", "&", "*", "_", "-", "+"]


    #this function chooses random symbols from __gem list
    def generate(self, number):
        Result = ""
        if 8<=number<=16:
            for num in range(number):
                temp = str(random.choice(self.__gen))
                Result += temp
            return Result
        else:
            return False


