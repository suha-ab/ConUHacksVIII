from flask import Flask, render_template, request, redirect, url_for, session, flash
app = Flask(__name__)
app.secret_key='SECRET_KEY'

@app.route('/')
def landing():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        return redirect()

@app.route('/queueTime')
def dateAndTime():
    return render_template('queueDateAndTime.html')

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

@app.route('/playerRole')
def playerRole():
    return render_template('playerRole.html')

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

@app.route('/userPlatform')
def userPlatform():
    return render_template('userPlatform.html')

@app.route('/userRegion')
def userRegion():
    return render_template('userRegion.html')


if __name__ == '__main__':
    app.run()
