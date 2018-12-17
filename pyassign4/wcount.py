"""
Author: 黄新迪 1700094621 元培学院
Python作业 Assign4 (Dec/11/2018)

wcount.py: This module provides a function to calculate the frequency of the words
that appears in a text file from a given url. The user inputs the target url and
the number of most frequent words (default = 10) to be displayed from the command prompt.
"""
import sys
from urllib.request import urlopen
import string

def retrieve_file(url):
    """
    The function retrieves the text file from a given url.
    """
    doc = urlopen(url)
    lines = doc.read().decode()
    doc.close()
    return lines

def wcount(lines,topn = 10):
    """
    lines: text input
    topn: number of the most frequent words that appear in the text file to be printed.
    
    The function process each line of the text file and create a dictionary with 
    the words and the frequency they appear in the text file. Then, the function
    ranks the words and output the n most frequent words that appear in the text file.
    """
    word_dict = {}
    line = lines.replace("-"," ")
    to_remove = string.punctuation + string.whitespace
    
    #process the line and create the dictionary with key:word and value:frequency.
    for word in line.split():
        word = word.strip(to_remove)
        word = word.lower()
        word_dict[word] = word_dict.get(word,0) + 1
    
    #arrange the data in terms of the frequency of word.
    arranged = []
    for word,freq in word_dict.items():
        arranged.append((freq,word))
    arranged.sort(reverse = True)

    #print the list with the top n most frequent words.
    output_list = []
    if topn >= len(arranged):
        for freq,word in arranged:
            output_list.append((word,freq))
    else:
        for freq,word in arranged[:topn]:
            output_list.append((word,freq))
    
    for word,freq in output_list:
        print(word,"\t",freq)
    return output_list    

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:
        paras = sys.argv
        url = paras[1]
        if len(paras) > 2:
            try:
                topn = int(paras[2])
            except Exception as err1:
                print(err1, "\n","Will run the function with default topn = 10")
        
        try:
            lines = retrieve_file(url)
        except Exception as err2:
            print(err2)
        else:
            try:
                wcount(lines,topn)
            except:
                wcount(lines)           
