from django.shortcuts import render
import requests
# Create your views here.

def index(request):
	g_summmay = None
	data = True
	result = None
    #globalsummary = None
	while(data):
		try:
			result = requests.get('https://api.covid19api.com/summary') 
			g_summmay = result.json()['Global']
			data = False
		except:
			data = True
		
	return render(request, 'index.html', {'g_summmay' : g_summmay})
	
