from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


if __name__ == '__main__':
    app.run() #仅本地可访问

#    flask  run - -host = 0.0.0.0 #可公网访问，开放IP限制

