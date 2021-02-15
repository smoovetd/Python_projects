from flask import Flask, render_template, request
import json

app = Flask(__name__)

def get_current_data() -> dict:
    try:
        with open('helper/test_mails.txt', 'r') as file:
            users = json.load(file)
            #print(str(users))
    except:
        users = {}
    #print('get_current_data() -> ' + str(users))
    return users

def write_users_to_file(users):
    if type(users) != dict:
        print('Error: users is not dictionary')
    else:
        with open('helper/test_mails.txt', 'w+') as file:
            json.dump(users, file)

def save_users(mail, height) -> None:
    users = get_current_data()
    #print(f'save_users() {str(users)}')
    users[mail] = height
    #print(f'save_users() {str(users)}')
    write_users_to_file(users)

def get_average_height():
    users = get_current_data()
    avg = calc_average(users.values())
    print(f'Average height is: {avg}')

def calc_average(items) -> float:
    count = 0
    sum = 0
    for item in items:
        crnt_item = 0
        try:
            crnt_item = float(item)
        except:
            crnt_item = 0
            count = coint -1

        sum = sum + crnt_item
        count = count + 1

    try:
        avg = sum/count
    except:
        print('Error: division by zero')
        avg = 0

    return avg

@app.route('/height/')
def collect_height() -> str:
    return render_template('index.html')

@app.route('/height/', methods = ['POST'])
def collect_height_input() -> str:
    crnt_user_mail = request.form['email']
    crnt_user_height = request.form['height']
    save_users(crnt_user_mail, crnt_user_height)
    get_average_height()
    return render_template('success.html')

#@app.route('/success/')
#def load_success() -> str:
#    return render_template('success.html')

print(calc_average([3,4,5]))

if __name__ == '__main__':
    app.run(debug=True)
