from flask import Flask, request, jsonify, render_template,json, send_from_directory

#Create the app object
app = Flask(__name__)

#importing function for calculations
import datetime
from new_calculator import alt_calc
from split_calculator import split_calc

#Define route for google ads.txt file
@app.route("/ads.txt")
def ads():
    return send_from_directory("static", "ads.txt")

#Define route for robots.txt file
@app.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt")

#Define route for sitemap.txt file
@app.route("/sitemap.txt")
def sitemap():
    return send_from_directory("static", "sitemap.txt")
    
#Define route for sitemap.txt file
@app.route("/sitemap.txt/")
def google():
    return send_from_directory("static", "googleb8c14849d55df27a.html")

#Define routes for webpages
@app.route('/')
def home():
	return render_template('index.html')
@app.route('/about/')
def about():
    return render_template('about.html')    
@app.route('/contact/')
def contact():
    return render_template('contact.html')	
@app.route('/splits/')
def splits():
    return render_template('splits.html')	
#Define altitude calculator	route
@app.route('/',methods=['POST'])
#Define altitude calculator
def predict():
    
    Sex = request.form.get('Sex')    
    Event = request.form.get('Event')
    Hours = request.form.get('Hours',type=int)
    Minutes = request.form.get('Minutes',type=int)        
    Seconds = request.form.get('Seconds', type=float)
    Elevation = request.form.get('Elevation',type=int)
    Units = request.form.get('Units',type=str)
    Prediction_Elevation = request.form.get('Prediction_Elevation',type=int)
    prediction =alt_calc(Sex,Event,Hours,Minutes,Seconds,Elevation,Units,Prediction_Elevation)
    input_time=str(str(Hours) + ":"+ str(Minutes).zfill(2)+":"+ ('{0:05.2f}'.format(Seconds)) + " at " + str(Elevation) + " " + (Units))
    input_time= input_time.lstrip('0,:')
    sentence = " at a prediction elevation of " + str(Prediction_Elevation) +" "+ Units + " for a " + str(Sex) + " completing the " + str(Event) + " in " + input_time
    print(sentence, type(sentence))
    if prediction and sentence:
        response= jsonify({'prediction':'Predicted Time of  '+ prediction, 'sentence':sentence})
        return response
    return jsonify({'error': 'Missing data!'})
    
   


@app.route('/Splits/',methods=['POST'])
def splitsform():
     Hours=request.form.get('Hours',type=int)
     Minutes=request.form.get('Minutes',type=int)
     Seconds=request.form.get('Seconds', type=float)
     Race_Distance= request.form.get('Race_Distance', type=float)
     Race_Units= request.form.get('Race_Units',type=str)
     Split_Distance=request.form.get('Split_Distance', type=float)
     Split_Units=request.form.get('Split_Units',type=str)
     splitresult=split_calc(Hours,Minutes,Seconds,Race_Distance,Race_Units,Split_Distance,Split_Units)
     splitsentence= "per " + str(Split_Distance) +" "+ str(Split_Units)
     print(splitresult)
     print(splitsentence)
     if splitresult and splitsentence:
        response= jsonify({'split': splitresult, 'splitphrase': splitsentence})
        return response
     return jsonify({'error': 'Missing data!'})
if __name__=="__main__":
    app.run(host="0.0.0.0", port=3000)