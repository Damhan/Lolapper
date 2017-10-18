from lolapper import Lolapper

lap = Lolapper("RGAPI-6ccf3a61-0f3f-444d-84d9-2e57e3300642")
print(lap.staticData.summonerSpellsById(20))
print(lap.masteries.bySummoner(38302))