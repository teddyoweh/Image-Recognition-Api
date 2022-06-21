 
from flask import Flask, request as req





main = Flask(__name__)
#app.config.from_object(config_filename)

#main.register_blueprint(views.blueprint)


from app.controllers import views