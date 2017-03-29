from flask import Flask, jsonify,render_template, request
from listOfGlams import list_glams
from NationaalArchief import main
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    """Main page."""
    return render_template('login.html')


@app.route('/result', methods=['POST'])
def receiveData():
    glam1 = request.form['glam_name']
    id = request.form['file_id']
    glam_list = list_glams()
    IsValidGLAM = 0
    for glam in glam_list: 
         if glam['name'] == glam1:
		IsValidGLAM=1
    		break
    if IsValidGLAM == 0:
	 return "GLAM Not Found in our list"
    else:
         #upload the image
         howManyMatches = main(id)
	 print('passes main')
	 if howManyMatches == 0:
		return 'No match found!'
	 else:
                returnString = 'Upload of ' + str(howManyMatches) + ' files successful. or File already exists'
	        return returnString

@app.route('/glam', methods=['GET'])
def showForm():
    """Glam Form"""
    return render_template('glam_form.html')	

if __name__ == "__main__":
    app.run()
