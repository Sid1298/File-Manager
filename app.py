import os
import subprocess
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def welcome(methods=['Get', 'Post']):
    mypath = os.getcwd()
    files = subprocess.check_output('dir', shell=True).decode('utf-8').split('\n')
    return render_template('index.html', mypath=mypath, file_list=files)

@app.route('/cd')
def cd():
    os.chdir(request.args.get('path'))
    return redirect('/')

# view text files
@app.route('/view')
def view():
    # get file content
    return subprocess.check_output('type '+ request.args.get('file'), shell=True).decode('utf-8').replace('\n', '<br>')
    # return request.args.get('file')

if __name__ == "__main__":
    app.run(debug=True)
