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

@app.route('/deldir')
def del_dir():
    os.rmdir(request.args.get('dir'))
    return redirect('/')

@app.route('/delfile')
def del_file():
    os.remove(request.args.get('dfile'))
    return redirect('/')

@app.route('/md')
def md():
    try:
        os.mkdir(request.args.get('new_folder'))
    except FileExistsError:
        return redirect('/')
    return redirect('/')

@app.route('/mf')
def mf():
    return render_template('new_file.html')

if __name__ == "__main__":
    app.run(debug=True)
