# -*- coding: utf-8 -*-

#------------------- Text Freq class
class TextFrequency:
    
    def __init__(self, file_name):
        self.file_name = file_name
        self.text = []
        self.getText()
        
    def toLower(self):
        self.text = self.text.lower()
        
    def getText(self):
       file = open(self.file_name, 'r')
       self.text = file.read()
       file.close()
       
       
    def letterFreq(self):
        freq = {}
        temporal_text = self.text
        for letter in temporal_text:
            if letter in freq:
                # increment frequency count
                freq[letter] = freq[letter] + 1
            else: 
                #initialise
                freq[letter] = 1
        return freq
    
    def wordFreq(self):
        freq = {}
        temporal_text = self.text.split()
        for word in temporal_text:
             if word in freq:
                # increment frequency count
                freq[word] = freq[word] + 1
             else: 
                #initialise
                freq[word] = 1
        return freq
    
 #------------------- Histogram Printer class   
class HistogramPrinter(TextFrequency):
    
    def __init__(self, file_name):
        TextFrequency.__init__(self, file_name)
        
    def printLetterHist(self):
        freq = TextFrequency.letterFreq(self)
        for letter in freq:
            print(letter, "*" * freq[letter])
                

    def printWordHist(self):
        freq = TextFrequency.wordFreq(self)
        for word in freq:
            print(word, "*" * freq[word])
    
#------------------- Tests
testCount = 0  

def suggestedTest1():
    print("\nLetter Frequency Test:")
    textFrequency = TextFrequency("lyrics.txt")     
    letterFreq = textFrequency.letterFreq()
    for letter in letterFreq:
        print(letter, letterFreq[letter])
    return validateConsoleOutput()
        
def suggestedTest2():  
    print("\nWord Frequency Test:")
    textFrequency = TextFrequency("lyrics.txt")     
    wordFreq = textFrequency.wordFreq()
    for word in wordFreq:
        print(word, wordFreq[word])
    return validateConsoleOutput()
        

def suggestedTest3():
    print("\Letter Histogram Test:")
    histogramPrinter = HistogramPrinter("lyrics.txt")
    histogramPrinter.printLetterHist()
    return validateConsoleOutput()
    
def suggestedTest4():
    print("\nWord Histogram Test:")
    histogramPrinter = HistogramPrinter("lyrics.txt")
    histogramPrinter.printWordHist()
    return validateConsoleOutput()
    
def suggestedTest5():
    print("\nLowerCase Word Histogram Test:")
    histogramPrinter = HistogramPrinter("lyrics.txt")
    histogramPrinter.toLower()
    histogramPrinter.printWordHist()
    return validateConsoleOutput()
    
def suggestedTest6():
    print("\Lower Case Letter Histogram Test:")
    histogramPrinter = HistogramPrinter("lyrics.txt")
    histogramPrinter.toLower()
    histogramPrinter.printLetterHist()
    return validateConsoleOutput()
        
    
def validateConsoleOutput():
    result = input("OUTPUT PASS? : [Y/N] : ")
    if result.lower() == "y":
        print("\n[PASS]\n-----------------------------------------")
        return True
    else:
        print("\n[FAIL]\n-----------------------------------------")
        return False
    
#------------------- Script

testResults = [suggestedTest1() ,suggestedTest2(), suggestedTest3(), suggestedTest4(), suggestedTest5(), suggestedTest6() ]
print("\nTEST OUTCOME: \n")
for testResult, item in zip(testResults, range(len(testResults))):
    print("TEST NO.", item +1 ,"PASS?", testResult)