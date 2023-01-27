import flask
from werkzeug.utils import secure_filename

app = flask.Flask(__name__)
app.secret_key = 'random'

@app.route('/')
def index():
    flask.flash('You were successfully logged in')
    return flask.render_template('index.html')

@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if flask.request.method == 'POST':
        user = flask.request.form['nm']
        resp = flask.make_response(
            flask.render_template('test.html', name=user))
        resp.set_cookie('username', user)
        return resp
    else:
        name = flask.request.cookies.get('username')
        return '<h1>welcome '+name+'</h1>'

@app.route('/upload', methods=['GET'])
def upload_file():
    return flask.render_template('upload.html')

@app.route('/uploader', methods=['POST'])
def upload():
    if flask.request.method == 'POST':
        f = flask.request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)