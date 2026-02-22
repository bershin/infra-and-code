from flask import Flask
import os
import pwd
import grp

app = Flask(__name__)

@app.route('/')
def hello():
    user_id = os.getuid()
    username = pwd.getpwuid(user_id).pw_name

    grp_id = os.getgid()
    groupname = grp.getgrgid(grp_id).gr_name


    return f'Hello {username} ({user_id}) and {groupname} ({grp_id})!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    