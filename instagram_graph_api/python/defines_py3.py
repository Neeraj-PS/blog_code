import requests
import json

def getCreds():
	""" Get creds required for use in the applications
	
	Returns:
		dictonary: credentials needed globally

	"""

	creds = {
		'access_token': 'ACCESS-TOKEN',
		'graph_domain': 'https://graph.facebook.com/',
		'graph_version': 'v6.0',
	}

	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
	creds['instagram_account_id'] = 'INSTAGRAM-BUSINESS-ACCOUNT-ID' # users instagram account id

	return creds

def makeApiCall( url, endpointParams, type ):
	""" Request data from endpoint with params
	
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters


	Returns:
		object: data from the endpoint

	"""

	if type == 'POST' : # post request
		data = requests.post( url, endpointParams )
	else : # get request
		data = requests.get( url, endpointParams )

	response = {
		'url': url,
		'endpoint_params': endpointParams,
		'endpoint_params_pretty': json.dumps(endpointParams, indent=4),
	}

	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

	return response # get and return content