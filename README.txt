------- Tableau CSV to TDE Uploader ---------


******DISCLAIMER******
This repository is based on the repository from bsullins/tableau-uploader but using Flask instead of PHP.
The DataExtract folder is directly from Tableau Official team
The extract-upload.py is created by Ryan Robitialle.


Prerequisite
  - Python 2.7

Installation
  1. Make sure you have Python 2.7 install correctly (This can be check by running python --version or python in CMD)
  2. Install virtualenv library from python -> pip install virtualenv
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
