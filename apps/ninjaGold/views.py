from django.shortcuts import render,HttpResponse,redirect
import random
from time import strftime,gmtime

# Create your views here.
def index(request):
	return render( request, "ninjaGold_index.html")

def process_money(request):
	if request.method != "POST":
		return redirect('/')

	time = strftime("%y-%m-%d %H:%M:%S", gmtime())

	if 'log' not in request.session:
		request.session['log'] = []

	if 'coin' not in request.session:
		request.session['coin'] = 0

	if request.form['building'] == "farm":
		gold = random.randrange(10,21)
		request.session['coin'] += gold
		string = "Earned "+str(gold)+" gold from the farm!"+ time
		request.session['log'].append('string')
		print string
		print request.session['coin']
		print gold
		return redirect('/')
	if request.form['building'] == "cave":
		gold = random.randrange(5,11)
		request.session['coin'] += gold
		string = "Earned "+str(gold)+" gold from the cave!"+ time
		request.session['log'].append('string')	
		print gold
		print request.session['coin']
		return redirect('/')
	if request.form['building'] == "house":
		gold = random.randrange(2,6)
		request.session['coin'] += gold
		string = "Earned "+str(gold)+" gold from the house!"+ time
		request.session['log'].append('string')	
		print gold
		print request.session['coin']
		return redirect('/')
	if request.form['building'] == "casino":
		gold = random.randrange(-50,51)
		request.session['coin'] += gold
		if gold > 0:
			string = "Earned "+str(gold)+" gold from the casino!"+ time
		else:
			string = "Entered a casino and lost"+str(gold)+" golds...Ouch.. "+time
		request.session['log'].append('string')	
		print gold
		print request.session['coin']
		return redirect('/')

def reset(request):
	if request.method == "GET":
		request.session.clear()
		return redirect('/')