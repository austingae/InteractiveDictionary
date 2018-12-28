import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def define(word):
    if word in data.keys():
        return data[word]
    elif len(get_close_matches(word,data.keys(),n = 1, cutoff = .80)) > 0:
        word = get_close_matches(word,data.keys(),n = 1, cutoff = .80)[0]
        return data[word]
    else:
        return "Word does not exist."

if __name__ == '__main__':
    user_input = input("Enter Word: ").lower()
    print(user_input)
    output = define(user_input)
    if type(output) == list:
        for i in output:
            print(i)


'''
I learned how to import and download libraries/packages.
I began on Project #1; learning about JSON and applying Python to real life applications. 

Tomorrow :
1. Learn about JSON (OK!)
2. Finish Project #1 (OK!) 
3. Begin making your own project consisting of JSON and Python (OK!)
4. Learn about difflib (SORT OF OK!)
'''