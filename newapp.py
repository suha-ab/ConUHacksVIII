from flask import Flask, render_template, request, redirect, url_for, session, flash
import joblib
import numpy as np
app = Flask(__name__)
app.secret_key='SECRET_KEY'

@app.route('/')
def landing():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        return redirect()

@app.route('/queueTime', methods=['POST', 'GET'])
def dateAndTime():
    if request.method== 'GET':
        return render_template('queueDateAndTime.html')
    if request.method == 'POST':
        session['dateTime'] = "09:26:00, Mon"
        return redirect("/resultPage")

@app.route('/killerMMR')
def killerMMR():
    return render_template('killerMMR.html')

@app.route('/survivorMMR', methods=['POST', 'GET'])
def survivorMMR():
    if request.method == 'GET':
        numSur = session['numSurvivors']
        print(numSur)
        return render_template('survivorMMR.html', numSur = numSur)
    if request.method == 'POST':
        session['partyMMR']=request.form.get("valueMMR")
        print(session['partyMMR'])
        return redirect('../userPlatform')

@app.route('/playerRole', methods=['POST', 'GET'])
def playerRole():
    if request.method == "GET":
        return render_template('playerRole.html')
    if request.method == "POST":
        playerRole = request.form["playerRole"]
        session['playerRole'] = playerRole
        if playerRole == "killer":
            return redirect("../killerMMR")
        else:
            return redirect("../partySize")

@app.route('/partySize', methods=['POST', 'GET'])
def partySize():
    if request.method == 'POST':
        numSurvivors = request.form.get("hidden_input")
        print(numSurvivors)
        session['numSurvivors']=numSurvivors
        print(session['numSurvivors'])
        return redirect('../survivorMMR')
    if request.method == 'GET':
        return render_template('survivorPartySize.html')

@app.route('/userPlatform', methods=['POST', 'GET'])
def userPlatform():
    if request.method == 'GET':
        return render_template('userPlatform.html')
    if request.method == 'POST':
        return redirect("../userRegion")

@app.route('/userRegion', methods=['POST','GET'])
def userRegion():
    if request.method == 'GET':
        return render_template('userRegion.html')
    else:
        userRegion = request.form['playerRegion']
        session['playerRegion'] = userRegion
        return redirect('/queueTime')
    
@app.route('/resultPage', methods=['POST', 'GET'])
def resultPage():
    # Load the trained model
    model = joblib.load('your_model.pkl')
    #load the label encoders
    le_list_x = joblib.load('le_list_x.pkl')
    le_y = joblib.load('le_y.pkl')
    
    time = session['dateTime'].split(", ")
    user_input = [time[0], time[1], session['playerRole'], session['numSurvivors'], session['playerRegion'], session['partyMMR']]
    #user_input = ["00:00:00", "Sun", "Killer", 1, "us-east-1", 1]
    
    # Encode the user input into numerical values
    for i in range(len(user_input)):
    # Check if the value is in the classes_ attribute
        if user_input[i] not in le_list_x[i].classes_:
        # If not, add it to classes_
            le_list_x[i].classes_ = np.append(le_list_x[i].classes_, user_input[i])
        # Transform the value
        user_input[i] = le_list_x[i].transform([user_input[i]])[0]
            
    print(user_input)        
            
    prediction = model.predict([user_input])
    prediction = prediction.astype(int)
    predicted_output = le_y.inverse_transform(prediction)      
    if request.method == 'GET':
        return render_template('resultPage.html', predicted_output = predicted_output)
    if request.method == 'POST':
        return redirect('/')
def predict():
    
    # Load the trained model
    model = joblib.load('your_model.pkl')
#load the label encoders
    le_list_x = joblib.load('le_list_x.pkl')
    le_y = joblib.load('le_y.pkl')
    
    datetime.datetime(year, month, date).strftime("%a")

    data = request.get_json()
    user_input = data['user_input']  # Adjust based on your input format
    
    user_input = ["00:00:00", "Sun", "Killer", 1, "us-east-1", 1]
    
    # Encode the user input into numerical values
    for i in range(len(user_input)):
    # Check if the value is in the classes_ attribute
        if user_input[i] not in le_list_x[i].classes_:
        # If not, add it to classes_
            le_list_x[i].classes_ = np.append(le_list_x[i].classes_, user_input[i])
        # Transform the value
        user_input[i] = le_list_x[i].transform([user_input[i]])[0]
          
        
            
        
    # Use the loaded model to make predictions
    # We specify [0] because the predict() method returns a list of predictions,
    # and we only have a single prediction
    prediction = model.predict([user_input])
    prediction = prediction.astype(int)
    predicted_output = le_y.inverse_transform(prediction)


    response = {'prediction': predicted_output}    


if __name__ == '__main__':
    app.run()
