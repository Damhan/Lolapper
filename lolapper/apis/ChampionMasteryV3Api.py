class ChampionMasteryV3Api():
	def __init__(self,bapi):
		self.api = bapi

	def all(self,summonerId):
		url = "/lol/champion-mastery/v3/champion-masteries/by-summoner/" + str(summonerId) 
		return self.api.apiRequest(url)

	def byId(self,summonerId,championId):
		url = "/lol/champion-mastery/v3/champion-masteries/by-summoner/" + str(summonerId) + "/by-champion/" +str(championId)
		return self.api.apiRequest(url)

	def sum(self,summonerId):
		url ="/lol/champion-master/v3/scores/by-summoner/" + str(summonerId)
		return self.api.apiRequest(url)