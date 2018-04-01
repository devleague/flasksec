## FlaskSec
 - Python web app for pentesting / intro to web development with python

### Initial setup / install Dependancies:
 - clone repo to local machine
 - ```pip install -r requirements.txt```

### Create virtualenv
```virtualenv env```

### Start virtualenv
```source env/bin/activate```

### Run .env 
```source .env```

### Start flask server
```flask run```

### Initialize Alembic for migrations
```python manage.py db init```

### Create first migration
```python manage.py db migrate```

### Apply migration
```python manage.py db upgrade```

### Add test user to db:
 - Requires set_password method from werkzeug.security module
 - ``` python```
 - ```from app import db```
 - ```from app.models import User```
 - ```new_user = User(username='whatever', email='test@example.com')```
 - ```new_user.set_password('whatever')```
 - ```db.session.add(new_user)```
 - ```db.session.commit()```

 ### Check new user was added to DB
 - ```from app import db```
 - ```from app.models import User```
 - ```users = User.query.all()```
 - ```for user in users: print(user.username)```
