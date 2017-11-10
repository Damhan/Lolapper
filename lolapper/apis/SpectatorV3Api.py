class SpectatorV3Api():
	def __init__(self,bapi):
		self.api = bapi

	def bySummonerId(self,sumId):
		url = "/lol/spectator/v3/active-games/by-summoner/" + str(sumId)
		return self.api.apiRequest(url)

	def featuredGames(self):
		url = "/lol/spectator/v3/featured-games" 
		return self.api.apiRequest(url)