class MasteriesV3Api():
	def __init__(self,bapi):
		self.api = bapi

	def bySummoner(self,summonerId):
		url = "/lol/platform/v3/masteries/by-summoner/" + str(summonerId)
		self.api.apiRequest(url)

