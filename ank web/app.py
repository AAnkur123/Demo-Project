from flask import Flask, render_template, request
app = Flask(__name__,template_folder='template')

@app.route('/')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/Blog')
def Blog():
    return render_template('Blog.html')

@app.route('/About')
def About():
    return render_template('About.html')

 


if __name__ == '__main__':
    app.run(debug=True)