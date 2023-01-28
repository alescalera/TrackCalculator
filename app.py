from flask import Flask, request, jsonify, render_template

#Create the app object
app = Flask(__name__)

#importing function for calculations
import datetime
from new_calculator import alt_calc


#Define calculator
@app.route('/')
def home():
	return render_template('index.html')
	
@app.route('/',methods=['POST'])
def predict():
	
    Sex = request.form['Sex']
    
    Event = request.form['Event']
    
    Hours = request.form.get('Hours',type=int)
    
    Minutes = request.form.get('Minutes',type=int)
    
    Seconds = request.form.get('Seconds', type=float)
    
    Elevation = request.form.get('Elevation',type=int)
    
    Units = request.form.get('Units',type=str)
    
    Prediction_Elevation = request.form.get('Prediction_Elevation',type=int)
    result=alt_calc(Sex,Event,Hours,Minutes,Seconds,Elevation,Units,Prediction_Elevation)
    sentence =  "at a prediction elevation of " + str(Prediction_Elevation) +" "+ Units + " for a " + str(Sex) + " completing the " + str(Event) + " in " + str(Hours) + ":"+ str(Minutes).zfill(2)+":"+ ('{0:05.2f}'.format(Seconds)) + " at " + str(Elevation) + " " + (Units)
	
    return render_template('index.html',Prediction=result,Phrase=sentence)
    
	
if __name__=="__main__":
    app.run(debug=False, host="0.0.0.0" port=81)