from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index.<a href="/hello">hello</a>'

@app.route('/hello')
def hello():
    return 'Hello World!<a href="/user/name">user/name</a>'

@app.route('/user/<username>')
def show_user(username):
    return 'Hello %s!<a href="/post/1">post/1</a>' % username

@app.route('/post/<int:post_id>/')
def show_post(post_id):
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
