class LolStatusV3Api():
	
	def __init__(self,bapi):
		self.api = bapi

	def shardData(self):
		url = "/lol/status/v3/shard-data"
		return self.api.apiRequest((url))