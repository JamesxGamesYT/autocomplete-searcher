import requests

def autocomplete(query):
	'''
	Returns autocomplete suggestions for a given query.\
	'''
	url = "https://suggestqueries.google.com/complete/search?q=" + query + "&client=firefox"
	autocomplete = requests.get(url)
	autocomplete = autocomplete.json()[1]
	results = ''
	for result in autocomplete:
		results += result + '\n'
	return results

def autocomplete_search(autocomplete):
	'''
	returns search results for given query, along with supporting information
	'''
	pass
