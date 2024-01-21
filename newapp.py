from flask import Flask, render_template, request, redirect, url_for, session, flash
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
        return redirect("../resultPage")

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

@app.route('/userRegion')
def userRegion():
    return render_template('userRegion.html')


if __name__ == '__main__':
    app.run()
