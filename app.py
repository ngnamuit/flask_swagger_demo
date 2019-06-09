# -*- coding: utf-8 -*-
#!/usr/bin/python
from flask import Flask, request
from flask_restplus import Api, Resource, fields

flask_app = Flask(__name__)
flask_app.debug = True
app = Api(app = flask_app,
		  version = "1.0",
		  title = "RestAPIs UI",
		  description = "Manage routing of the application")

profile = app.namespace('profile', description='Own profile')
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


@profile.route("/owner")
class ProfileClass(Resource):

	@app.doc(responses={ 200: HTTP_CODE['200'], 403: HTTP_CODE['403'], 500: HTTP_CODE['500'] },
			 params={'': 'Get owner\'s project information'})
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
