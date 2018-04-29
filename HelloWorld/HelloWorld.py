from flask import Flask, url_for, request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'index.<a href="%s">hello</a>' % url_for('hello')

@app.route('/hello')
def hello():
    return render_template('hello.html', name='test')

@app.route('/user/<username>')
def show_user(username):
    return '<head><link rel="stylesheet" type="text/css" href="%s" /></head>Hello %s!<a href="%s">post</a>' % (url_for('static', filename="style.css"), username, url_for('show_post', post_id=1))

@app.route('/post/<int:post_id>/', methods=['GET', 'POST'])
def show_post(post_id):
    if request.method == 'GET':
        return 'GET Post %d' % post_id
    else:
        return 'POST Post %d' % post_id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
