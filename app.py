#our web app framework!

#you could also generate a skeleton from scratch via
#http://flask-appbuilder.readthedocs.io/en/latest/installation.html

#Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the
#HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template engine 
#for you automatically.
#requests are objects that flask handles (get set post, etc)
from flask import Flask, render_template,request
#scientific computing library for saving, reading, and resizing images
import re
#for matrix math
import numpy as np
#for regular expressions, saves time dealing with string data
import re

#system level operations (like loading files)
import sys 
#for reading operating system data
import os
#tell our app where our saved model is
import base64
from PIL import Image
from io import BytesIO
#initalize our flask app
app = Flask(__name__)

	

@app.route('/')
def index():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("index.html")

@app.route('/predict/',methods=['GET','POST'])
def predict():
	file = request.get_data()
	# saving / gettingimage 
	#print(file)
	my_bytes = file.replace(b'data:image/png;base64,',b'')
	print(my_bytes)
	im = Image.open(BytesIO(base64.b64decode(my_bytes)))
	im.save('image.png', 'PNG')
	# sending model..
	

if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
	app.run()
	#optional if we want to run in debugging mode
	#app.run(debug=True)
