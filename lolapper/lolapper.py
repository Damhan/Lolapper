from apis.BaseApi import BaseApi
from apis.ChampionV3Api import ChampionV3Api
class Lolapper(object):
    
    def __init__(self,key):
        self.baseApi = BaseApi(key)
        self.champion =  ChampionV3Api(self.baseApi)
        
def main():
	testWrapper = Lolapper("RGAPI-9bc7ab7f-555e-4946-a916-b8cb32c16e2b")
	print(testWrapper.champion.byId(10))

if __name__ == "__main__":
	main()