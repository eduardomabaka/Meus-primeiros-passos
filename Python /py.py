from flask import Flask, render_template, redirect, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'EduardoEVEN'

@app.route('/modelo', method=['post'])

@app.route('/')
def happy(): 
  return render_template('iindex.html')
def modelo():
  nome=request.form.get('nome')
  senha=request.form.get('senha')
  
  return redirect('/')
  