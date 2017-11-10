class RunesV3Api():
	def __init__(self,bapi):
		self.api = bapi

	def runesBySummonerId(self,sumId):
		url = "/lol/platform/v3/runes/by-summoner/" + str(sumId)
		return self.api.apiRequest(url)