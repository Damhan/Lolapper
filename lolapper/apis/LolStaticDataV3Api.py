class LolStaticDataV3Api():
	def __init__(self,bapi):
		self.api = bapi

	def champions(self):
		url = "/lol/static-data/v3/champions"
		return self.api.apiRequest(url)

	def championsById(self,championId):
		url = "/lol/static-data/v3/champions/" + str(championId)
		return self.api.apiRequest(url)

	def items(self):
		url = "/lol/static-data/v3/items"
		return self.api.apiRequest(url)

	def itemsById(self,itemId):
		url = "/lol/static-data/v3/items/" + str(itemId)
		return self.api.apiRequest(url)

	def languageStrings(self):
		url = "/lol/static-data/v3/language-strings"
		return self.api.apiRequest(url)

	def languages(self):
		url = "/lol/static-data/v3/languages"
		return self.api.apiRequest(url)

	def maps(self):
		url = "/lol/static-data/v3/maps"
		return self.api.apiRequest(url)

	def masteries(self):
		url = "/lol/static-data/v3/masteries"
		return self.api.apiRequest(url)

	def masteriesById(self,masteryId):
		url = "/lol/static-data/v3/masteries/" + str(masteryId)
		return self.api.apiRequest(url)

	def profileIcons(self):
		url = "/lol/static-data/v3/profile-icons"
		return self.api.apiRequest(url)

	def realms(self):
		url = "/lol/static-data/v3/realms"
		return self.api.apiRequest(url)

	def runes(self):
		url = "/lol/static-data/v3/runes"
		return self.api.apiRequest(url)

	def runesById(self,runeId):
		url = "/lol/static-data/v3/runes/" + str(runeId)
		return self.api.apiRequest(url)

	def summonerSpells(self):
		url = "/lol/static-data/v3/summoner-spells/"
		return self.api.apiRequest(url)

	def summonerSpellsById(self,spellId):
		url = "/lol/static-data/v3/summoner-spells/" + str(spellId)
		return self.api.apiRequest(url)

	def versions(self):
		url = "/lol/static-data/v3/versions/"
		return self.api.apiRequest(url)