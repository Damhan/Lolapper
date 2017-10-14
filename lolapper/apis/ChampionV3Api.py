
class ChampionV3Api():
	"""
	This class is a wrapper for all the Champion-V3 APIs provided by Riot currently.
	"""
	def __init__(self,bapi):
		self.api = bapi


	#all retrieves all lol champions.
	def all(self):
		url = "/lol/platform/v3/champions"
		return self.api.apiRequest(url)

	#byId retrieves a lol champion using it's ID.
	def byId(self,id):
		url = "/lol/platform/v3/champions/" + str(id)
		return self.api.apiRequest(url)