from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'index.<a href="%s">hello</a>' % url_for('hello')

@app.route('/hello')
def hello():
    return 'Hello World!<a href="%s">user</a>' % url_for('show_user', username='test')

@app.route('/user/<username>')
def show_user(username):
    return 'Hello %s!<a href="%s">post</a>' % (username, url_for('show_post', post_id=1))

@app.route('/post/<int:post_id>/', methods=['GET', 'POST'])
def show_post(post_id):
    if request.method == 'GET':
        return 'GET Post %d' % post_id
    else:
        return 'POST Post %d' % post_id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
