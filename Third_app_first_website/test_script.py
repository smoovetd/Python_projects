from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home() -> str:
    #return 'Home Page'
    return render_template('home.html')


@app.route('/about/')
def about() -> str:
    return 'Website content is here!'

if __name__ == '__main__':
    app.run(debug=True)