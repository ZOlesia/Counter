from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 



@app.route('/')
def increase():
	if 'counter' not in session:
		session['counter'] = 1
	else:
		session['counter'] += 1
	return render_template('index.html')



@app.route('/plus2', methods=['POST'])
def increase_by_two():
	session['counter'] += 2
	return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
	session['counter'] = 1
	return render_template('index.html')

app.run(debug=True)


