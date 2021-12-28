from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'hello,world!'
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User '+username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
# HTTP 메소드
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
if __name__ =="__main__":
    app.run(debug=True)