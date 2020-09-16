import json
import os
from difflib import get_close_matches

g_words_file = 'files/data.json'
g_matching_criteria_perc = 75


def get_min_length(first:str, second:str):
        min_length = 0
        if len(first) <= len(second):
            min_length = len(first)
        else:
            min_length = len(second)

        return min_length


def compare_words(first:str, second:str):
    matching_points = 0

    max_index = get_min_length(first, second)
    for index in range(0, max_index):
        if first[index] == second[index]:
            matching_points = matching_points + 1

    return float(matching_points/len(first)) * 100


def find_similar_word_old(word:str, keys_words:list) -> list:
    word_lenght = len(word)
    similar_words = []
    similar_words_by_chars = []

    possible_matches = [ new_word for new_word in keys_words if abs(len(new_word) - word_lenght) <=2]

    for new_word in possible_matches:
        if compare_words(word, new_word) >= g_matching_criteria_perc:
            similar_words.append(new_word)

    return similar_words

def find_similar_word(word: str, key_words:list) -> str:
    result = ''
    matches_list = get_close_matches(word, key_words)
    if len(matches_list) == 0:
        result = None
    else:
        result = matches_list[0]

    return result


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
                possible_matches = find_similar_word(word, file_content.keys())
                word_description = 'Word: "' + word + '" is not found in dictionary! Please double check it.'
                if possible_matches != None and  input('Did you mean word: ' + possible_matches + '? Y for yes, any key for no: ') == 'Y':
                    word_description = file_content[possible_matches]

        return word_description

print(find_word(input('Enter word: ')))
