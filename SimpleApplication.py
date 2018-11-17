from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('HelloWorld.html')

@app.route('/news')
def news():
    if request.method == 'POST':
        return render_template('HelloWorld.html')
    else:
        return render_template('News.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')


if __name__ == '__main__':
    app.run()
