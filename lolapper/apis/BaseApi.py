import requests
class BaseApi(object):
	base_url = "https://euw1.api.riotgames.com"
	def __init__(self,key):
		self.apiKey = "?api_key=" + key

	def apiRequest(self,url):	
		r = requests.get(self.base_url+url+self.apiKey)
		return r.content