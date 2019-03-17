This Project is based on the kishstats/flask-s3-browser Project -- Thanks to B Kishkis for his Great Tutorial

Project Layout  

/home/user/Projects/FlaskS3Inst
├── flaskS3/
│   ├── app.py
│   ├── config.py
│   ├── filters.py
│   ├── templates/
│   │   ├── files.html
│   │   ├── index.html
│   │   ├── layout.html
│   └── static/
│       └── style.css
├── venv/
├── setup.py
├── .gitignore
├── requirements.txt
└── MANIFEST.in

Step 1 --> Create a folder called FlaskS3Inst on AWS 
mkdir FlaskS3Inst

Step 2 --> Create a Virtual Env in this folder called venv
cd FlaskS3Inst
virtualenv -p python3 venv

Step 2.1 --> Start the Virtual Env
source venv/bin/activate

Step 3 -- install Dependencies
pip install -r requirements.txt

Step 4 -- Modify the contents of Config.py to your AWS Keys
_S3_ACCESS_KEY = ' '
_S3_SECRET = ''

Step 5 -- Run the App -- Command for Linux -- (Change export to set if AWS on Windows)
export FLASK_APP = app.py
export FLASK_ENV = development


Step 6 --> Open AWS, Select the Security Group and Add a Custom Inbound Rule to open up port 5000


