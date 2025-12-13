"""Contains a list of maps and their details for pulling."""
class Maps:
    def __init__(self, size: int, gameMode: str) -> None:
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
            6th Element: Builders
            or None
        Raises :
            KeyError: map cannot be found within dictionary map

        Examples:
            >>> test = Maps(8, "Raid")
            >>> print(test.getMapDetail("Site Kronos"))
            >>> ['https://raw.githubusercontent.com/Willleeson/Discord-Bot/429d41843b31ff18d16eb8ab58a53b4e7dfa5fe0/mapScreenShots/siteKronos.png', 'Attack weapons', 'Attack equipment', 'Defend weapons', 'Defend equipment', 'Vehicles']
        """
        maps={"Site Kronos": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/siteKronos-min.png",
                              "2 x BR 20s Del\n2 x AR 20s Dis\n2 x Commando 20s Del\n1 x Longshot AR 20s Del\n1 x HMG Turret 30s Del\n1 x Red Gun (100%) 45s Del\n1 x Heatwave (100%) 30s Del\n1 x Ravenger (100%) 20s Del",
                              "1 x Shroud Screen Spawner 90s\n1 x Drop Shield Spawner 90s\n4x Kinetic Ammo Box",
                              "4 x Commando 20s Del\n2 x BR 20s Del\n1 x HMG Turret 30s Del\n1 x SPNKR (4 Rockets) 60s Del\n1 x Shotgun 30s Del,\n1 x Sniper (8 Shots) 45s Del",
                              "1 x Drop Shield 90s\n1 x Threat Sensor 90s\n4 x Kinetic Ammo Box",
                              "None",
                              "Neptunee FPS"],
            "Firebase Theia": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/firebaseTheia-min.png",
                              "Redgun 45s\nHeatwave 45s\nRavager 60s\n2 BRs 60s\n4 Commandos 45s\n4 Pistols 20s\n4 AR 45s\nScrap Cannon 90s",
                              "Thruster 90s\nDrop Wall 60s\nShroud 60s\n2 x Grenade 30s\n2 x Kinetic Ammo Box",
                              "Sniper 1 spare clip 45s\nRockets 1 spare clip 60s\n2 BR 60s\nShotgun 45s\nSMG 60s \nHydra 45\n2 Pistol 30s\nAvenger 45s",
                              "2 x Grenade 30s\n1 x Kinetic Ammo Box",
                              "2 Chain Hogs 90s\nRazorback 90s\nChopper 90s\n2 Mongoose 60s",
                              "DontGetMadUrBad\nDa Caboose\nCleanestNine69"],
            "Caladrius Nest": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/caladriusNest-min.png",
                              "1 x Stalker rifle 120s\n3 x BRs\n3 x Commandos\n8 x bandits\n1 x Needler\n1 x HMG Turret \n3 x avengers \n1 x sidekick",
                              "1 x threat seeker\n2 x Spike Grenade\n1 x Kinetic Ammo Box",
                              "1 x Sniper 60s 2 clips\n1 x Rockets 60s 2 clips\n3 x BRs\n3 x Commandos\n1 x avenger \n1 x shotgun\n1 x hydra ",
                              "1 x Drop wall\n1 x Kinetic Ammo Box",
                              "1 x Warthog\n4 x Mongoose\n1 x Gungoose",
                              "CleanestNine69\nd solo monster"],
            "Archipelago Ruins": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/archipeligoRuins-min.png",
                              "1 x Fuel Rod 90s 1 clip\n1 x Shotgun\n2 x BRs\n4 x ARs\n4 x Commandos\n4 x Bandits\n4 x Sidekicks\n1 x Needler",
                              "None",
                              "1 x Sniper 90s 3 clips\n1 x Rockets 90s 3 clips\n1 x Shotgun\n1 x Hydra\n3 x BRs\n4 x ARs\n4 x Commandos\n4 x Sidekicks\n8 x bandits\n1 x Avenger",
                              "1 x Drop wall\n1 x Threat Sensor",
                              "1 x Wraith 240s\n1 x Ghost\n1 x Warthog\n1 x Razorback\n3 x Mongoose",
                              "d solo monster"],
            "Facility Nightfall": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/facilityNightfall-min.png",
                              "1 x Stalker rifle 60s\n1 x Heatwave 60s\n1 x Ravager 60s\n2 x BRs\n4 x Sidekicks\n3 x ARs\n4 x Commandos\n8 x Bandits\n1 x Avenger",
                              "4 x frag grenades\n1 x Thruster\n1 x Shroud screen\n2 x Kinetic Ammo Box",
                              "1 x Sniper 60s 2 clips\n1 x Rockets 60s 2 clips\n1 x Shotgun\n1 x Hydra\n1 x Avenger\n4 x Commandos\n8 x Bandits\n1 x HMG Turret",
                              "4 x frag grenades\n1 x Drop wall\n1 x Threat sensor\n2 x Kinetic Ammo Box",
                              "1 x Warthog\n1 x Razorback\n2 x Mongoose ",
                              "II J0HNS0N II"],
            "Facility Perdition": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/facilityPeridition-min.png",
                              "1 x Stalker Rifle 45s\n1 x Ravager 60s\n1 x Disruptor\n1 x BR\n2 x ARs\n2 x Commandos",
                              "1 x shroud screen\n1 x drop wall\n2 x Kinetic Ammo Box",
                              "1 x Sniper 45s 2 clips\n1 x Rockets 60s 2 clips\n1x  BR\n2 x Commandos\n2 x ARs\n2 x Sidekicks\n8 x Bandits\n1 x Hydra\n1 x Shotgun",
                              "6 x frag grenades\n1 x threat sensor \n1 x drop wall\n2 x Kinetic Ammo Box",
                              "1 Rockethog 90s\n1 Razorback\n2 Mongoose",
                              "DontGetMadUrBad\ndeaddealer95\nMrNotTZG\nDa Caboose\nII J0HNS0N II"],
            "Firebase Meridian": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/firebaseMeridian-min.png",
                              "1 x Redgun 45s\n1 x Heatwave 45s\n1 x Ravager 60s\n1 x Carbine 45s\n1 x Mangler 30s\n2 x Commando 20s\n2 x Pistol 20s",
                              "1 x Shroud screen 60s",
                              "1 x Sniper 1 spare clip 30s\n1 x Rockets 1 spare clip 45s\n1 x Hydra 30s\n1 x Shotgun 30s\n1 x SMG 30s\n1 x BR 30s\n2 x Commando 45s\n2 x AR 45s\n2 x Pistol 30s",
                              "1 x Drop wall  60s\n1 x Threat sensor 60s ",
                              "1 x Chain Hog 60s",
                              "Tinsilverwolf22\nSpartanNat05\nDa Caboose\nDontGetMadUrBad"],
            "Firebase Sierra": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/firebaseSierra-min.png",
                              "1 x talker Rifle 180s\n1 x Ravager 120s\n1 x Gravity Hammer 120s\n7 x BRs\n1 x Shotgun\n4 x Sidekicks\n4 x ARs\n8 x Commandos\n2 x HMG Turrets\n1 x scrap cannon",
                              "2 x frag grenades\n6 x dynamo grenades\n2 x spike grenades\n3 x Overshields 180s\n18 x repulsors\n3 x Thrusters\n2 x hardlight coils\n4 x shock coils\n2 x kinetic coils\n1 x Shroud screen\n1 x threat sensor\n1 x drop wall",
                              "1 x Sniper 60s 2 clips\n1 x Rockets 60s 2 clips\n3 x BRs\n1 x Shotgun\n1 x Hydra\n4 x commandos\n4 x sidekicks\n4 x ARs\n6 x bandits\n2 x HMG Turrets",
                              "2 x frag grenades\n1 x shock coil\n1 x threat sensor\n1 x grappleshot\n2 x Kinetic Ammo Box",
                              "1 x Rocket Hog\n1 x Banshee 180s\n1 x Ghost\n2 x Warthogs\n1 x Razorback\n3 x Gungoose\n2 x Mongoose",
                              "CleanestNine69"],
            "FOB: Hope": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/fobHope-min.png",
                              "1 x Stalker Rifle 90s\n1 x Heatwave 60s\n2 x BRs\n1 x Mangler\n2 x commando",
                              "1 x Thruster\n1 x Shroud\n1 x threat seeker\n2 x dynamo grenades\n2 x plasma grenade",
                              "1 x Sniper 60s 2 x clips\n3 x BRs\n1 x hydra\n1 x shotgun\n8 x Bandits\n2 x ARs",
                              "2 x Kinetic Ammo Box",
                              "1 x Warthog",
                              "CleanestNine69\nDontGetMadUrBad\nMrNotTZG\nDa Caboose"],
            "Fort Frosthollow": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/fortFroshollow-min.png",
                              "1 x Stalker Rifle 60s\n1 x Ravager 60s\n1 x Heatwave 60s\n2 x BRs\n1 x Avenger\n3 x Commandos\n3 x ARs\n4 x sidekicks\n5 x bandits ",
                              "4 x frag grenades\n1 x shroud screen\n1 x thruster\n2 x Kinetic Ammo Box",
                              "1 x Sniper 60s 2 clips\n1 x Rockets 60s 2 clips\n2 x BRs\n1 x Hydra\n1 x Shotgun\n1 x Avenger\n2 x Commandos\n2 x ARs\n2 x sidekicks\n8 x bandits\n1 x HMG Turret",
                              "4 x frags\n1 x threat sensor\n1 x thruster\n1 x shock coil\n2 x Kinetic Ammo Box",
                              "1 x Warthog\n2 x Mongoose",
                              "II J0HNS0N II"],
            "Fort Greenhorn": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/fortGreenhorn-min.png",
                              "1 x Stalker rifle 90s\n1 x Ravager 60s\n1 x heatwave 60s",
                              "1 x shroud screen\n1 x thruster\n6 x dynamo grenades\n2 x Kinetic Ammo Box",
                              "1 x Sniper 60s 2 clips\n1 x Rockets 60s 2 clips\n2 x BRs\n2 x Commandos\n2 x sidekicks\n1 x Hydra\n1 x Shotgun\n1 x Avenger",
                              "4 x Frag Grenade\n1 x Kinetic Ammo Box",
                              "2 x mongoose\n1 x Warthog\n1 x Razorback",
                              "DontGetMadUrBad\nMrNotTZG\nDa Caboose"],
            "Griffins Nest": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/griffinsNest-min.png",
                              "1 x Stalker rifle 60s\n1 x elite bloodblade\n1 x Hydra\n1 x Pulse carbine\n3 x BRs\n6 x commandos\n4 x sidekicks\n1 x avenger\n1 x Mangler\n1 x bandit\n2 x HMG Turret",
                              "2 x spike grenades\n4 x frag grenades\n2 x dynamo grenades\n1 x shock coil\n2 x hardlight coils\n1 x kinetic coil\n3 x drop walls\n6 x threat sensors\n4 x thrusters\n1 x Overshield",
                              "1 x Sniper 60s 2 clips\n1 x Rockets 60s 2 clips\n1 x Shotgun\n1 x Hydra\n1 x HMG Turret\n3 x BRs\n4 x Commandos\n4 x ARs\n4 x Sidekicks\n8 x Bandits",
                              "2 x thrusters\n4 x Frag grenades\n1 x shock coil",
                              "1 x Brute Chopper\n2 x Warthogs\n1 x Razorback\n2 x Mongoose",
                              "CleanestNine69"],
            "Interpeak Outpost": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/interpeakOutpost-min.png",
                              "1 x Stalker Rifle 60s\n1 x Shotgun\n1 x Avenger\n3 x BRs\n5 x ARs\n1 x Longshot AR\n4 x Commandos\n4 x sidekicks\n6 x needlers\n2 x pulse carbine\n1 x energy sword\n1 x scrap cannon\n1 x HMG Turret",
                              "1 x Overshield 80s\n1 x drop wall\n4 x Thrusters",
                              "1 x Sniper 60s 2 clips\n1 x Rockets 60s 2 clips\n1 x Hydra\n1 x Shotgun\n3 x BRs\n4 x ARs\n4 x sidekicks\n4 x Commandos\n18 x bandits\n1 x HMG Turret",
                              "1 x drop wall\n1 x threat sensor\n2 x frag grenades\n1 x shock coil\n2 x kinetic coils",
                              "1 x Warthog\n1 x Razorback\n1 x Ghost\n5 x Mongoose",
                              "d solo monster"],
            "Outpost Illustria": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6988b53761e2730171f9e0e3803c31f36228ac71/optimisedMapScreenshots/outpostIllustria-min.png",
                              "1 x Stalker rifle 35s\n1 x Ravager 50s\n1 x BR\n2 x Commandos\n3 x ARs\n1 x sidekick\n1 x avenger\n 11 bandits",
                              "1 x shroud screen\n6 x frag grenades\n2 x Kinetic Ammo Box",
                              "1 x Sniper 30s 2 clips\n1 x Rockets 45s 2 clips\n1 x BRs\n2 x Commandos\n3 x ARs\n2 x sidekicks\n10 x bandits\n1 x Shotgun\n1 x Avenger",
                              "4 x frag grenades\n1 x Kinetic Ammo Box",
                              "2 x mongoose\n1 x Warthog\n1 x Razorback",
                              "DontGetMadUrBad\nMrNotTZG"],
            "Outpost Paragon": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/outpostParagon-min.png",
                              "1 x Stalker Rifle 45s\n1 x Heatwave 45s\n1 x Ravager 45s\n2 x BRs\n4 x commandos\n4 x ARs\n4 x sidekicks",
                              "2 x spike grenades\n2 x frag grenades\n2 x plasma grenades\n1 x thruster\n1 x shroud screen\n2 x Kinetic Ammo Box",
                              "1 x Sniper 45s 2 clips\n1 x Rockets 30s 1 clip\n3 x BRs\n1 x Shotgun\n1 x Hydra\n1 x Avenger\n2 x sidekicks\n4 x commandos\n6 x ARs\n4 x bandits\n1 x HMG Turret",
                              "1 x shock coil\n4 x frag grenades\n2 x Kinetic Ammo Box",
                              "1 x Razorback\n1 x Gungoose\n1 x Mongoose",
                              "Da Caboose"],
            "Outpost Jupiter": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/outpostJupiter-min.png",
                              "2 x Commandos 45s\n1 x Redgun 45S 100%\n1 x Heatwave 45s 100%\n1 x Ravager 60s 100%\n1 x BR 60s\n1 x Mangler 30s",
                              "3 x Kinetic Ammo Box",
                              "7 x Bandit Evos Pads\n2 x Nade Spawners\n2 x Pistols\n1 x S7 Sniper 8 shots 45s\n1 x M41 Rockets 4 shots 60s\n1 x Shotgun 45s\n1 x Blast Coil\n1 x Avenger 30s\n1 x BR 60s ",
                              "2 x Kinetix Ammo Box",
                              "2 x Mongooses\n1 x Chain hog 60s",
                              "Mcheif48"],
            "Bellevue Embassy": ["https://raw.githubusercontent.com/Willleeson/Discord-Bot/6548a8fc44b11a5daa24767ed0ceae25855b8d4c/optimisedMapScreenshots/bellevueEmbassy-min.png",
                              "1 x Red gun 30s\n1 x Ravager 45s\n1 x Vestige Carbine\n1 x BR\n2 x Commandos",
                              "1 x Shroud\n1 x Threat sensor\n1 x Thruster\n2 x Kinetic Ammo Box",
                              "1 x Sniper 2 clips 30s\n1 x Rockets 2 clips 45s\n1 x Hydra\n1 x Shotgun\n1 x BR\n2 x Commandos\n4 x ARs",
                              "2 x Kintec Ammo Box",
                              "1 x Rocket Hog\n1 x Razorback\n1 x Gungoose\n1 x mongoose",
                              "DontGetMadUrBad\ndeaddealer95\nMr NotTzG\nTinsilverwolf22"]
                              }
        try:
            return maps[map]
        except KeyError as e:
            print(f"Error Occured: {e}")
            return None
        
class raidMaps(Maps):
    def __init__(self, size: int, gameMode = "raid") -> None:
        super().__init__(size, gameMode)

    def raidMapPool(self, size) -> dict[int, str]:
        if size == 8:
            return {
                1: "Site Kronos", #DONE
                2: "Firebase Meridian",
                3: "Caladrius Nest", #Need more
                4: "Outpost Illustria",
                5: "FOB: Hope",
                6: "Facility Nightfall",
                7: "Outpost Paragon",
                8: "Fort Frosthollow",
                9: "Griffins Nest"}
        elif size == 10:
            return {
                1: "Firebase Theia", #Need more
                2: "Firebase Meridian", 
                3: "Caladrius Nest", #Need more
                4: "Fort Greenhorn", 
                5: "Outpost Illustria", 
                6: "FOB: Hope",
                7: "Interpeak Outpost", 
                8: "Archipelago Ruins", 
                9: "Facility Nightfall",
                10: "Outpost Paragon", 
                11: "Facility Perdition", 
                12: "Fort Frosthollow",
                13: "Firebase Sierra", 
                14: "Griffins Nest",
                15: "Bellevue Embassy",
                16: "Outpost Jupiter"}
        elif size == 12:
            return {
                1: "Firebase Theia", #Need more
                2: "Firebase Meridian", 
                3: "Caladrius Nest", #Need more
                4: "Fort Greenhorn", 
                5: "Griffins Nest", 
                6: "Interpeak Outpost",
                7: "Archipelago Ruins", 
                8: "Facility Nightfall", 
                9: "Outpost Paragon",
                10: "Facility Perdition", 
                11: "Fort Frosthollow", 
                12: "Firebase Sierra",
                13: "Bellevue Embassy"}
        return {}
    
    def getMap(self, randomNumber: int, size = 12) -> str:
        maps = self.raidMapPool(size)
        return maps.get(randomNumber, "Unkown Map")
    
    def getMapCount(self, size = 12) -> int:
        maps = self.raidMapPool(size)
        return len(maps)