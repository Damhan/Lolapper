from apis.BaseApi import BaseApi
from apis.ChampionMasteryV3Api import ChampionMasteryV3Api
from apis.ChampionV3Api import ChampionV3Api
from apis.LeagueV3Api import LeagueV3Api
from apis.LolStaticDataV3Api import LolStaticDataV3Api
from apis.LolStatusV3Api import LolStatusV3Api

class Lolapper(object):
    
    def __init__(self,key):
        self.baseApi = BaseApi(key)
        self.champion =  ChampionV3Api(self.baseApi)
        self.championMastery = ChampionMasteryV3Api(self.baseApi)
        self.league = LeagueV3Api(self.baseApi)
        self.staticData = LolStaticDataV3Api(self.baseApi)
        self.status = LolStatusV3Api(self.baseApi)