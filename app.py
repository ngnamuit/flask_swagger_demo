# -*- coding: utf-8 -*-
#!/usr/bin/python
from flask import Flask, request, render_template, make_response
from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy

## config and connect to database
flask_app = Flask(__name__)
flask_app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:1@35.232.87.105/flask-swagger-db'
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
flask_app.config["SQLALCHEMY_ECHO"] = True # log all the statements issued to stderr which can be useful for debugging
db = SQLAlchemy(flask_app)

## config to use swagger UI
app = Api(app = flask_app,
		  version = "1.0",
		  title = "RestAPIs UI",
		  description = "Manage routing of the application")

## define route
profile = app.namespace('profile', description='Own profile')
about = app.namespace('about', description='<a href="/about">Click here to view my info</a>')
coming_soon = app.namespace('coming_soon', description='<a href="/coming_soon">Click here to view new features coming soon</a>')
model = app.model('Name Model',
				  {'name': fields.String(required = True,
    					  				 description="Name of the person",
    					  				 help="Name cannot be blank.")})
##
HTTP_CODE = {
	'200': 'OK',
	'400': 'Bad Request and Invalid Argument',
	'403': 'FORBIDDEN',
	'500': 'Mapping Key Error',
}
## Define TABLE
class ResUsers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)



## Routing
@coming_soon.route("/", methods=['GET'])
class ComingSoon(Resource):
	def get(self):
		headers = {'Content-Type': 'text/html'}
		return make_response(render_template('coming_soon.html'), 200, headers)

@about.route("/", methods=['GET'])
class About(Resource):
	def get(self):
		headers = {'Content-Type': 'text/html'}
		return make_response(render_template('about.html'), 200, headers)

@profile.route("/owner")
class ProfileClass(Resource):
	def get(self):
		try:
			return {
				"name": 'Nguyen Thanh Nam',
				"status": "Single",
				"contact": {
					"skype": "ngnamuit994",
					"linked": "https://www.linkedin.com/in/nam-nguyen-thanh-3bb2b4117/",
					"resume": "https://www.topcv.vn/xem-cv/68dc63745ac65e8682f02dcd73582943",
					"email": "ngnamuit@gmail.com"
				},
				"notes": '''Finding a professional workplace environment.
						   Trying to improve myself every day.
						'''
			}
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")


## APP RUN
if __name__ == "__main__":
	db.create_all()
	flask_app.run(debug=True)