class MatchV3Api():
	def __init__(self,bapi):
		self.api = bapi

	def matchById(self,matchId):
		url = "/lol/match/v3/matches/" + str(matchId)
		return self.api.apiRequest(url)

	def matchlistByAccount(self,accountId,queue="",endTime="",beginIndex="",beginTime="",season="",champion="",endIndex=""):
		args = locals()
		isFirst = True
		url = "/lol/match/v3/matchlists/by-account/" + str(accountId)
		for key in args:
			if args[key] and key != "accountId" and key != "self":
				if isFirst:
					url += "?" + key + "=" + str(args[key])
					isFirst = False
				else:
					url += "&" + key + "=" + str(args[key])
		print(url)
		self.api.apiKey = "&" + self.api.apiKey[1:]
		ret = self.api.apiRequest(url)
		self.api.apiKey = "?" + self.api.apiKey[1:]
		return ret

	def recentMatchesByAccount(self,accountId):
		url = "/lol/match/v3/matchlists/by-account/" + str(accountId) + "/recent"
		return self.api.apiRequest(url)

	def timelineByMatchId(self,matchId):
		url = "/lol/match/v3/timelines/by-match/" + str(matchId)
		return self.api.apiRequest(url)

	def matchesByTournament(self,tournamentCode):
		url = "/lol/match/v3/matches/by-tournament-code/" + str(tournamentCode) + "/ids"

	def matchByIdAndTournament(self,matchId,tournamentId):
		url = "/lol/match/v3/matches/" + str(matchId) + "/by-tournament-code/" + str(tournamentCode)