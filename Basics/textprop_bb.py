import re

g_user_messages = []
g_question_words = ('How', 'Why', 'Can', 'May', 'Would',
                    'When', 'Who', 'Which', 'Where',
                    'Does', 'Did', 'Is','Are','What')
g_question_ends = ('isn\'t it', 'aren\'t they', 'isn\'t he', 'isn\'t she', 'aren\'t we', 'aren\'t you')

def get_user_input() ->str:
    result = input('Say something: ')
    return result

def is_question(input_txt, is_verbose_mode=False):
    first_word = input_txt.split(' ')[0].title()
    result = False

    if is_verbose_mode:
        print('DEBUG: first_word: ' + first_word)
        print('DEBUG: contains first_Word: ' + str(g_question_words.__contains__(first_word)))

    if g_question_words.__contains__(first_word):
        result = True
    elif len(input_txt.split(' ')) > 1:
        last_word = input_txt.split(' ')[-1]
        before_last_word = input_txt.split(' ')[-2]
        if g_question_ends.__contains__( before_last_word + ' ' + last_word):
            result = True

    return result


def process_input(input_txt:str, is_verbose_mode=False):
    # check for empty sentance and add message that it is empty
    if is_verbose_mode: print('DEBUG is space: ' + str(input_txt.isspace()))
    if input_txt.isspace() == True or input_txt == '':
        g_user_messages.append('<No valid input was entered>')
        return

    #replace whitespaces with single space
    input_txt = re.sub(r'\s+', ' ', input_txt)

    processed_input = input_txt.capitalize()

    if is_question(input_txt, is_verbose_mode):
        processed_input +='?'
    else:
        processed_input +='.'

    if is_verbose_mode: print('DEBUG process_input:' + processed_input)
    g_user_messages.append(processed_input)
    return

def run_program(is_verbose_mode = False):
    print('Wellcome to text processor program!')
    print('To exit type "\\end"')

    while True:
        crnt_input = get_user_input()
        if crnt_input == '\\end':
            break
        else:
            process_input(crnt_input, is_verbose_mode)
            continue

    print('Thank you for using text processor program!')
    print('Your output is: ')
    print(*g_user_messages, sep=' ')

run_program()
