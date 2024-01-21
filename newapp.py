from flask import Flask, render_template, request, redirect, url_for, session, flash
app = Flask(__name__)

@app.route('/')
def landing():
    if request.method == 'GET':
        return render_template('index.html', boolean=True)
    if request.method == 'POST':
        return redirect()

@app.route('/queueTime')
def dateAndTime():
    return render_template('queueDateAndTime.html', boolean=True)

@app.route('/killerMMR')
def killerMMR():
    return render_template('killerMMR.html')

@app.route('/survivorMMR')
def survivorMMR():
    return render_template('survivorMMR.html')

@app.route('/playerRole')
def playerRole():
    return render_template('playerRole.html')

@app.route('/partySize')
def partySize():
    return render_template('survivorPartySize.html')

@app.route('/userPlatform')
def userPlatform():
    return render_template('userPlatform.html')

@app.route('/userRegion')
def userRegion():
    return render_template('userRegion.html')


if __name__ == '__main__':
    app.run()
