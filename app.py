from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='ゆうし教オフィシャルサイト')

@app.route('/teachings')
def teachings():
    return render_template('teachings.html')

if __name__ == '__main__':
    app.run(debug=True)
