import json
import os
import mysql.connector
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


def find_word(word:str) -> list:
    '''find_word - takes argument word - and will list with description from g_words_file content - default ..files/data.json and returns list with explanations or error message'''

    word_description = []
    if os.path.exists(g_words_file) == False:
        word_description.append('ERROR no such file: ' + g_words_file)
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

                if possible_matches != None and  input('Did you mean word: ' + possible_matches + '? Y for yes, any key for no: ') == 'Y':
                    word_description = file_content[possible_matches]
                else:
                    word_description.append('Word: "' + word + '" is not found in dictionary! Please double check it.')
        return word_description

def find_word_db(word:str) -> list:
    '''find_word - takes argument word - and will list with description from remote DB - from the Udemy course and returns list with explanations or error message'''

    result = []

    conn = mysql.connector.connect(
        user        = 'ardit700_student',
        password    = 'ardit700_student',
        host        = '108.167.140.122',
        database    = 'ardit700_pm1database'
    )

    cursor = conn.cursor()

    cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s' OR Expression = '%s' OR Expression = '%s'" % (word.lower(), word.title(), word.upper()))
    res = cursor.fetchall()

    if len(res) == 0:
        cursor.execute('SELECT DISTINCT(Expression) FROM Dictionary')
        all_keys = [key[0] for key in cursor.fetchall()]

        matches = get_close_matches(word, all_keys)
        if matches:
            new_word = matches[0]
        else:
            new_word = None

        if new_word and input('Did you mean word: %s? Press "Y" for Yes ' % (new_word))=='Y':
            cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % (new_word))
            res = cursor.fetchall()
        else:
            res = [('Word "%s" was not found in the dictionary.' % (word),)]

    for item in res:
        result.append(item[0])

    #print(result)
    #print(type(result))

    return result


def get_list_printable(input_list:list) -> str:
    header_message= 'Search result:'
    result = header_message
    start_of_line = ' * '
#    print(type(input_list))
#    print(input_list)
    for item in input_list:
        result = result + '\n' + start_of_line + item

    return result

def run_dictionary(use_db = True):
    '''run_dictionary takes user input and searches for matching word in the dictionary. Can be used with DB or file depending on parameter use_db'''

    is_end = False
    print('To Exit type: "/end"')
    while (not is_end):
        my_word = input('Enter word: ' )
        if my_word == '/end':
            is_end = True
            break
        if use_db:
            content = get_list_printable(find_word_db(my_word))
        else:
            content = get_list_printable(find_word(my_word))
        print(content)

    print('Goodbye')

#print(find_word(input('Enter word: ')))
#print(get_list_printable(find_word(input('Enter word: '))))
#find_word_db('test')
run_dictionary()
