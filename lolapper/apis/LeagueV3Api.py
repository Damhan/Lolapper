class LeagueV3Api():

	def __init__(self,bapi):
		self.api = bapi

	def challengerByQueue(self,queue):
		url = "/lol/league/v3/challengerleagues/by-queue/" + queue
		return self.api.apiRequest(url)

	def bySummoner(self,summonerId):
		url = "/lol/league/v3/leagues/by-summoner/" + str(summonerId)
		return self.api.apiRequest(url)

	def byId(self,leagueId):
		url = "/lol/league/v3/leagues/" + str(leagueId)
		return self.api.apiRequest(url)

	def mastersByQueue(self,queue):
		url ="/lol/league/v3/masterleagues/by-queue/" + queue
		return self.api.apiRequest(url)

	def positionBySummoner(self,summonerId):
		url = "/lol/league/v3/positions/by-summoner/" + str(summonerId)
		return self.api.apiRequest(url)