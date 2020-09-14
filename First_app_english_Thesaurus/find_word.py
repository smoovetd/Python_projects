import json
import os

g_words_file = 'files/data.json'

#def find_similar_word(word:str) -> str:


def find_word(word:str) -> str:
    '''find_word - takes argument word - and will be returned description from g_words_file content - default ..files/data.json '''

    word_description = ''
    if os.path.exists(g_words_file) == False:
        word_description = 'ERROR no such file: ' + g_words_file
    else:

        with open(g_words_file, 'r') as data_file:
            file_content = json.load(data_file)
            if word in file_content.keys():
                word_description = file_content[word]
            elif word.title() in file_content.keys():
                word_description = file_content[word.title()]
            elif word.lower() in file_content.keys():
                word_description = file_content[word.lower()]
            elif word.upper() in file_content.keys():
                word_description = file_content[word.upper()]
            else:
                word_description = 'Word: "' + word + '" is not found in dictionary! Please double check it.'

        return word_description

print(find_word(input('Enter word: ')))
