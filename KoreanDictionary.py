'''
Make a Korean Dictionary of 15 words.
'''
import json
from difflib import get_close_matches

korean_data = json.load(open("korean_vocabulary.json"))

def my_translator(word):
    if word in korean_data.keys():
        return korean_data[word]

    word = get_close_matches(word,korean_data.keys(),n=1,cutoff=.69)
    if word:
        return korean_data[word[0]]
    else:
        raise Exception("Word does not exist.")




if __name__ == '__main__':

    user_input = input("Define:")
    definition = str(my_translator(user_input)).replace('[','').replace(']','').replace("'",'')
    print(user_input + ": " + definition)



'''
LOAD is used to read from the json files!!! (JSON to Python)
json.load - used for json files
json.loads - used for json formatted lines inside the python file

json.load() expects to get the text from a file-like object
json.loads() expects to get its text from a string object


DUMPS is used to modify or edit the json files!!! (Python to JSON)

12/24 : Summary: I learned to create my own JSON content, make a Korean Dictionary, went into a little more
depth into json and learned smaller commands.
'''

'''
Tomorrow :
1. Create Hangman incorporating JSON. 
2. Watch Khan Academy: Computer Science : How Computers Work : ALL
'''