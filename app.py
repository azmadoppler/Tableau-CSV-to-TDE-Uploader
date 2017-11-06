from flask import Flask, render_template , request , redirect
from flask_bootstrap import Bootstrap
import os;
import sys
import subprocess;

app = Flask(__name__)
app.config.from_object(__name__)
# Make sure to install 'Flask-Bootstrap'
Bootstrap(app)

UPLOAD_FOLDER = currentPath = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # with open('all_command.txt' , 'r') as f:
    #     content = [line.strip() for line in f]
    # name = []
    # command = []
    #
    # for item in content:
    #     spliter = item.split(',')
    #     name.append(spliter[0])
    #     command.append(spliter[1])
    # output_value = zip(name,command)
    return render_template('index.html')

@app.route('/result')
def execute():
    command = request.args.get('command')
    execute_command = command.split( )
    execution = subprocess.check_output(execute_command, shell=True)
    # return render_template('result.html',command=command,execution=execution)

    return render_template('result.html', command = command , execution = execution)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginTo',methods=['GET','POST'])
def loginTo():
    if request.method == 'POST':
        #Getting Parameter
        hostURL = request.form['url']
        username = request.form['username']
        password = request.form['password']


        #Convert to command
        hostCommand = " -s " + hostURL
        userCommand = " -u " + username
        passwordCommand = " -p " + password
        # print "tabcmd login" + hostCommand + userCommand + passwordCommand;
        result = subprocess.check_output("tabcmd login" + hostCommand + userCommand + passwordCommand, shell=True)
        print result

        return render_template('result.html', result = result )

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploadTo',methods=['GET', 'POST'])
def uploadTo():
    if request.method == 'POST':
        #Getting Parameter
        hostURL = request.form['url']
        username = request.form['username']
        password = request.form['password']


        #Convert to command
        hostCommand = " -s " + hostURL
        userCommand = " -u " + username
        passwordCommand = " -p " + password
        # print "tabcmd login" + hostCommand + userCommand + passwordCommand;
        result = subprocess.check_output("tabcmd login" + hostCommand + userCommand + passwordCommand, shell=True)

        file = request.files['file']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
        if os.path.exists(filepath):
            os.remove(filepath)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        tableauName = filepath.replace(".csv",".tde")
        if os.path.exists(tableauName):
            os.remove(tableauName)

        sys.argv = ['extract-upload.py',  file.filename]
        execfile('extract-upload.py')

        new_name = request.form['new_name']
        project_name = request.form['project_name']

        file_name_command = " -n "+new_name
        project_name_command = " -r "+project_name

        publishCmd = 'tabcmd publish '+ file.filename.replace(".csv",".tde") + file_name_command + project_name_command + " -o"
        result = subprocess.check_output(publishCmd, shell=True)

        return render_template('result.html', result = result )

@app.route('/convert')
def convert():
    if request.method == 'POST':
        file = request.files['file']
        return 'Convert Page Received'

@app.route('/logout')
def logout():
    result = subprocess.check_output("tabcmd logout", shell=True)
    print result
    return render_template('result.html', result = result )

if __name__ == "__main__":
    app.secret_key = 'Stelligence Secret'
    app.debug = True
    app.run()
