# Tutorial
# This program will go through the a list of dictionaries and spit out all
# the possible valid words for a typo

import itertools, time

class Dictionary:

    def _init_(self):
        print('Initializing..')
    
    def main(self):
        print('Program Begin...')
        #opening the text file and create a collection of all the words in the file
        # (lower case) it , we called it ' english_words'. Text file has 10000 words 
        with open("list.txt") as word_file:
            english_words = set(word.strip().lower() for word in word_file)
            print('Created dictionary set...')
            
        valid = 'yes'
        while(valid.lower() == 'yes'):
            word=input('Please Enter data : ')
            wordGen =[]
                
            #checking words exit in the list ()  
            if word.lower() in english_words:
                print('Word exist')
            else:
               self.checkWordInDictionary(word, english_words)
            
            valid = self.getExitValue()
            
    #check the program should exist or not
    def getExitValue(self):
        validInputList = ['yes', 'no']
        valid=input('Do you want to continue (yes/no) ?')
        return valid
    
    #check word exist in the ditionary list
    def checkWordInDictionary(self, word, english_words):
        print('Word doesn\'t exist..')
        print('Suggestions .... ')
        for i in range(0, len(word)):
            wordGen = list(itertools.permutations(word,i))
                
            for j in range(0, len(wordGen)):
                if "".join(wordGen[j]).lower() in english_words:
                    print(' ---> ', "".join(wordGen[j]))
#----------------------END of the Class -------------------------
                    
# creating the object
dictionary = Dictionary()
#calling the main funtion
dictionary.main()
