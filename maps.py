class Maps:
    def __init__(self, size: int, gameMode: str):
        self.size = size
        self.gameMode = gameMode
        
class raidMaps(Maps):
    def __init__(self, size, gameMode = "raid"):
        super().__init__(size, gameMode)

    def getMap(self, randomNumber, size = 12):
        if size == 8:
            maps = {1: "Site Kronos"}
        if size == 10:
            pass
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


    def mapScreenshot(map):
        screenshot = {"Site Kronos": r"mapScreenShots\siteKronos.png",
                      "Firebase Theia v2": r"mapScreenShots\firebaseTheia.png",
                      "Caldrius Nest": r"mapScreenShots\caldriusNest.png",
                      "Fort Greenhorn": r"mapScreenShots\fortGreenhorn.png"}