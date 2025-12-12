"""Contains a list of maps and their details for pulling."""
class Maps:
    def __init__(self, size: int, gameMode: str):
        self.size = size
        self.gameMode = gameMode

    def getMapDetail(self, map: str) ->  list[str] | None:
        """Function to pull map details based on the map name returned through the function "getMap"

        Args :
            map (str): Name of map being passed in

        Returns :
            maps (list[str]): in respective order of returning list:
            0th Element: Image
            1st Element: Attacking Weapons
            2nd Element: Attacking Equipment
            3rd Element: Defending Weapons
            4th Element: Defending Equipment
            5th Element: Vehicles
            or None
        Raises :
            KeyError: map cannot be found within dictionarhy map

        Examples:
            >>> test = Maps(8, "Raid")
            >>> print(test.getMapDetail("Site Kronos"))
            >>> ['https://raw.githubusercontent.com/Willleeson/Discord-Bot/429d41843b31ff18d16eb8ab58a53b4e7dfa5fe0/mapScreenShots/siteKronos.png', 'Attack weapons', 'Attack equipment', 'Defend weapons', 'Defend equipment', 'Vehicles']
        """
        maps={"Site Kronos": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/429d41843b31ff18d16eb8ab58a53b4e7dfa5fe0/mapScreenShots/siteKronos.png",
                              "2 x BR\n2 x AR\n2 x Commando\n1 x Sidekick\n1 x SMG\n1 x Longshot AR\n1 x Skewer (1 shot)\n1 x HMG Turret (100%)\n1 x Red Gun (100%)\n1 x Heatwave (100%)\n1 x Ravenger (100%)",
                              "1 x Shroud Screen Spawner\n1 x Drop Shield Spawner\n1 x Overshield Spawner",
                              "Defend weapons",
                              "Defend equipment",
                              "Vehicles"],
            "Firebase Thiea v2": ["https://github.com/Willleeson/Discord-Bot/blob/429d41843b31ff18d16eb8ab58a53b4e7dfa5fe0/mapScreenShots/firebaseTheia.png",
                              "Attack weapons",
                              "Attack equipment",
                              "Defend weapons",
                              "Defend equipment",
                              "Vehicles"],
            "Calrius Nest": ["https://github.com/Willleeson/Discord-Bot/blob/429d41843b31ff18d16eb8ab58a53b4e7dfa5fe0/mapScreenShots/caldriusNest.png",
                              "Attack weapons",
                              "Attack equipment",
                              "Defend weapons",
                              "Defend equipment",
                              "Vehicles"],}
        try:
            return maps[map]
        except KeyError as e:
            print(f"Error Occured: {e}")
            return None
        
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




