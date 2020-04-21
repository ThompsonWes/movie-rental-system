from flask import Flask, render_template

app = Flask(__name__)

# this is a comment

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/home')
def login():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
