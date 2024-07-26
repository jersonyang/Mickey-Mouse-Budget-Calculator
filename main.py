income = 0.0
#needs
rent = 0.0
groceries = 0.0
utilities = 0.0
healthcare = 0.0
transportation = 0.0
debt = 0.0
#wants
entertainment = 0.0
splurges = 0.0
goingout = 0.0
other = 0.0
#savings
efund = 0.0
retirement = 0.0
other_sav = 0.0
#suggest
needs_suggestion = 0.0
wants_suggestion = 0.0
savings_suggestion = 0.0
#total
sum_of_needs = 0.0
sum_of_wants = 0.0
sum_of_savings = 0.0
socgood = ""
# ---- YOUR APP STARTS HERE ----

# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)

# -- Routes section --

# INDEX
@app.route('/')
@app.route('/templates/index.html')
def index():
  return render_template('/templates/index.html')



@app.route('/templates/calc.html')
def calc():
  return render_template('/templates/calc.html')

@app.route('/templates/results.html', methods=['POST'])
def results():
  income = float(request.form.get('income'))

  #needs
  rent = float(request.form.get('rent'))
  groceries = float(request.form.get('groceries'))
  utilities = float(request.form.get('utilities'))
  healthcare = float(request.form.get('healthcare'))
  transportation = float(request.form.get('transportation'))
  debt = float(request.form.get('debt'))

  #wants
  entertainment = float(request.form.get('entertainment'))
  splurges = float(request.form.get('splurges'))
  goingout = float(request.form.get('goingout'))
  other = float(request.form.get('other'))

  #savings
  efund = float(request.form.get('efund'))
  retirement = float(request.form.get('retirement'))
  other_sav = float(request.form.get('other-sav'))

  needs_suggestion = round(income*0.5,2)
  wants_suggestion = round(income*0.3,2)
  savings_suggestion = round(income*0.2,2)

  sum_of_needs = rent + groceries + utilities + healthcare + transportation + debt
  sum_of_wants = entertainment + splurges + goingout + other
  sum_of_savings = efund + retirement + other_sav

  return_statement = f"With a monthly income of ${income}, you should spend ${needs_suggestion} on your monthly needs, ${wants_suggestion} on your monthly wants, and ${savings_suggestion} for your monthly savings. As it is, you spend ${sum_of_needs} on your monthly needs, ${sum_of_wants} on your monthly wants, and ${sum_of_savings} on your monthly savings. "

  

  if sum_of_needs > needs_suggestion:
    return_statement += "\nCongratulations, you're off to a great start. Due to your financial circumstances, we recommend you rethink your spending choices, prioritize paying your needs, and earning more money. \nOn the social good page, you should check out options to contribute that don't require income!"

  if sum_of_needs < needs_suggestion:
    extra = needs_suggestion - sum_of_needs
    return_statement += f"Congratulations! You have an extra ${extra}. Consider putting it towards your savings or debt. If not, look at ways you can do social good by checking out ways to contribute monetarily to a cause of your choice!"
    

  
  if sum_of_needs == needs_suggestion:
    return_statement += "\nCongratulations! Your budget is perfectly balanced. \n\nLook at ways you can do social good by checking out ways to contribute to a cause of your choice without disrupting your income!"

  
  return render_template('/templates/results.html', return_statement = return_statement, needs_suggestion = needs_suggestion, wants_suggestion = wants_suggestion, savings_suggestion = savings_suggestion, sum_of_needs = sum_of_needs, sum_of_wants = sum_of_wants, sum_of_savings = sum_of_savings)



@app.route('/templates/socialgood.html')
def socialgood():
  sum_of_needs = 100
  needs_suggestion = 500

  if sum_of_needs < needs_suggestion:
    socgood = "We suggest: With Disposable Income!"
  if sum_of_needs > needs_suggestion:
    socgood = "We suggest: No Money Required!"
    
  return render_template('/templates/socialgood.html', socgood = socgood)

@app.route('/templates/about.html')
def about():
  return render_template('/templates/about.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
