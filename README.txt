------- Tableau CSV to TDE Uploader ---------


******DISCLAIMER******
This repository is based on the repository from bsullins/tableau-uploader but using Flask instead of PHP.
The DataExtract folder is directly from Tableau Official team
The extract-upload.py is created by Ryan Robitialle.


Prerequisite
  - Python 2.7
  - Tabcmd 10.4 (You can get it here https://www.tableau.com/support/releases/server/10.4 )  (Or any version that you Server use)

Installation
  1. Make sure you have Python 2.7 install correctly (This can be check by running python --version in CMD)\
  1. Make sure you have Tabcmd installed correctly (This can be check by running tabcmd in CMD)
	**NOTE If you don't want to use virtualenv to control your environment variable you can skip to Step 5 **
  2. Install virtualenv library from python -> pip install virtualenv  
  3. Create virtualenv by open Command Line in -> virtualenv env
  3. Activate virtualenv by open Command Line in /env/Script folder then input the command -> activate
  4. Navigate back to the first folder of the program (cd ../..)
  5. Install other dependency by typing this command to Command Line -> pip install -r requirement
  6. Install the DataExtract tableau library by going into the DataExtract folder
  7. From CMD input command -> python setup.py build
  8. After building is done input -> python setup.py install

Running Flask Application
  1. Set the Flask App Environment variable by input this to CMD -> set FLASK_APP=app.py
  2. Lastly, you can run the Application by using -> python -m flask run
  3. Web can be access by the port number 5000

Usage
  1. From UI, input all the field as shown, please make sure that the filename is correct.
  2. After you're ready you can execute the form to upload the file.
  3. Progress or Bug can be track through the CMD that run the Server

TODO
  1. More file guarding condition (try catch/make sure filename function properly)
  2. More upload format (TDE,TDS,TWB)
