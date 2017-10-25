from lolapper import Lolapper

lap = Lolapper("RGAPI-6ccf3a61-0f3f-444d-84d9-2e57e3300642")
print(lap.match.timelineByMatchId(3355787581))
print(lap.match.recentMatchesByAccount(223793867))

#223793867