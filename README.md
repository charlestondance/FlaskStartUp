# FlaskStartUp
Base Flask Set-Up for Synthetic Biology Start-ups

This allows start up companies to create their own web app based custom intranet software.

Set up a virtual env with all the requirements

if there is a database delete it:
python manage.py shell
db.drop_all()

export your email environment variable: 
export FLASKY_ADMIN=xxxxx@gmail.com

Create user roles:
python manage.py shell
db.create_all()
Role.insert_roles()

Manually add the admin user:
user = User(email="xxxxx@gmail.com", username="dmcclymo", password="xxxx")
db.session.add(user)
db.session.commit()

Based on the Book Flask Web Development By Miguel Grinberg
