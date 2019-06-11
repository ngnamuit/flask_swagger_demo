# -*- coding: utf-8 -*-
#!/usr/bin/python
from flask import Flask, request, render_template, make_response
from flask_restplus import Api, Resource, fields

flask_app = Flask(__name__)
flask_app.debug = True
app = Api(app = flask_app,
		  version = "1.0",
		  title = "RestAPIs UI",
		  description = "Manage routing of the application")

profile = app.namespace('profile', description='Own profile')
about = app.namespace('about', description='<a href="/about">Click here to view my info</a>')
coming_soon = app.namespace('coming_soon', description='<a href="/coming_soon">Click here to view new features coming soon</a>')
model = app.model('Name Model',
				  {'name': fields.String(required = True,
    					  				 description="Name of the person",
    					  				 help="Name cannot be blank.")})

HTTP_CODE = {
	'200': 'OK',
	'400': 'Bad Request and Invalid Argument',
	'403': 'FORBIDDEN',
	'500': 'Mapping Key Error',
}


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
