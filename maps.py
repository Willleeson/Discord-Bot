class Maps:
    def __init__(self, size: int, gameMode: str):
        self.size = size
        self.gameMode = gameMode

    def getMapDetail(self, map: str) ->  list[str] | None:
        maps = {}
        
class raidMaps(Maps):
    def __init__(self, size: int, gameMode = "raid"):
        super().__init__(size, gameMode)

    def getMap(self, randomNumber: int, size = 12) -> str:
        if size == 8:
            maps = {1: "Site Kronos"}
        if size == 10:
            maps = {1: "Firebase Theia v2",
                    2: "Firebase Meridian",
                    3: "Caldrius Nest",
                    4: "Fort Greenhorn",
                    5: ""}
        if size == 12:
            maps = {1: "Firebase Theia v2",
                    2: "Firebase Meridian",
                    3: "Caldrius Nest",
                    4: "Fort Greenhorn",
                    5: "Scorpions Nest",
                    6: "Griffins Nest",
                    7: "FOB Hope",
                    8: "Firebase Pele"}
            pass
        return maps[randomNumber]



#IDEA FOR REPRESENTATION 
maps={"Site Kronos": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/429d41843b31ff18d16eb8ab58a53b4e7dfa5fe0/mapScreenShots/siteKronos.png",
                      "Attack",
                      "Defned"],
    "Firebase Thiea v2": ["https://github.com/Willleeson/Discord-Bot/blob/429d41843b31ff18d16eb8ab58a53b4e7dfa5fe0/mapScreenShots/firebaseTheia.png",
                          "Attack",
                          "Defend"],
    "Calrius Nest": ["https://github.com/Willleeson/Discord-Bot/blob/429d41843b31ff18d16eb8ab58a53b4e7dfa5fe0/mapScreenShots/caldriusNest.png",
                     "Attack",
                     "Defend"]}



