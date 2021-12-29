from flask import Flask,url_for,render_template,request,make_response,redirect
from werkzeug import secure_filename 
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
# HTTP 메소드,request
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # 아래의 코드는 요청이 GET 이거나, 인증정보가 잘못됐을때 실행된다.
    return render_template('login.html', error=error)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)
# 파일업로드
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
        
# 쿠키 읽기
@app.route('/a')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.

# 쿠키 저장
@app.route('/b')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
#리다이렉트
@app.route('/redirect')
def redirect():
    return redirect(url_for('login'))


#에러페이지 변경하기
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404







if __name__ =="__main__":
    app.run(debug=True)