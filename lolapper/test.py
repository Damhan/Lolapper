from lolapper import Lolapper

lap = Lolapper("RGAPI-52a6772c-fbd5-488e-ab7d-bbc7a3acfd86")
print(lap.staticData.summonerSpellsById(20))
print(lap.staticData.versions())