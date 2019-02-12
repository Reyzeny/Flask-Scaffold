#FLASK API SCAFFOLD
This is a flask api scaffold structured for api development with api versioning and other necessary tools.
It contains the following
- FLASK
- FLASK CORS
- FLASK RESTPLUS
- FLASK-JWT-EXTENDED
- FLASK SQLALCHEMY
- GUNICORN
- DOCKER
- API VERSIONING
- STRUCTURED ENVIRONMENT VARIABLES AND CONFIG FILES

You can add other dependencies to your project

#HOW TO START THE APP USING PYTHON DEVELOPMENT SERVER
from the command line, enter the following
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r req.txt`
- `python entry.py`

#HOW TO START THE APP USING GUNICORN SERVER
from the command line, enter the following
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r req.txt`
- `gunicorn --bind 0.0.0.0:5000 entry:app`

#HOW TO START THE APP USING DOCKER
from the command line, enter the following
- `docker build . -t appname:apptag`
- `docker run -p 5000:5000 appname:apptag`
Where appname is the name of you want to give your app and app tag is a tag for your app

