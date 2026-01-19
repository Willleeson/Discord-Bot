"""Discord Bot Posiedon Main Function"""
from maps import raidMaps
from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
from discord import app_commands as app
import random
import os



alive = Flask('')

@alive.route('/')
def home():
    return "Bot is Online!" 

def run_flask():
    port = int(os.environ.get("WEBSITE_PORT", 8080))
    alive.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.daemon = True # Ensures the thread dies when the main script stops
    t.start()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True



class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        """Initialises the commands with the server, Pushing all available commands to the server.

        Args :
            None
        
        Returns :
            self.tree.sync: Synced commands to the server

        Raises :
            ERROR: When tree commands failed to sync with discord API

        Examples:
        >>> "Synced 2 commands to the server."
        >>> "Failed to sync"
        """
        myGuild = discord.Object(id=809078759944749158)
        self.tree.copy_global_to(guild=myGuild)
        try:
            synced = await self.tree.sync(guild=myGuild)
            print(f"Synced {len(synced)} Commands to the server.")
        except Exception as e:
            print(f"ERROR: {e}")

bot = MyBot()


@bot.tree.command(name="raid", description="Random Selection of 3 Raid Maps")
@app.commands.describe(size="Size of Raid, 8 for 8v8. 10 for 10v10. 12 for 12v12")
@app.commands.choices(size=[
    app.commands.Choice(name="8v8", value=8),
    app.commands.Choice(name="10v10", value=10),
    app.commands.Choice(name="12v12", value=12)])
async def raid(interaction: discord.Interaction, size: app.commands.Choice[int]):
    """A discord APP Comand that displays a random pooling of 3 maps based on the size given.

    Args :
        size (int): choice of 8, 10, 12 respectively representing 8v8, 10v10, 12v12 in the maps folder
    
    Returns :
        Embed (discord.Interaction): 3 Discord Embeds of each different map showcasing: Image, weapons/equipment for both attack and defense. As well as vehicles and builders.
        
    Example :
        >>> /raid 8v8
        >>> Embed_1: Site Kronos.....
        >>> Embed_2: Firebase Meridian.....
        >>> Embed_3: Caladrius Nest.....
\
    """
    await interaction.response.defer()
    try:
        selected_size = size.value
        raid_instance = raidMaps(selected_size, "raid")
        nMaps = raid_instance.getMapCount(selected_size)
        embedList = []
        
        # Select 3 random maps
        rNumber = random.sample(range(1, nMaps + 1), min(3, nMaps))
        
        for index, mapIndex in enumerate(rNumber, 1):
            mapName = raid_instance.getMap(mapIndex, selected_size)
            mapDetails = raid_instance.getMapDetail(mapName)
            
            if mapDetails is None:
                errorEmbed = discord.Embed(
                    title=f"Map {index}",
                    description=f"Details not found for {mapName}.",
                    color=discord.Color.red())
                embedList.append(errorEmbed)
                continue
                
            embed = discord.Embed(title=f"Map {index}", color=discord.Color.blue())
            embed.add_field(name="Map", value=mapName, inline=False)
            embed.add_field(name="Builders", value=mapDetails[6], inline=True)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="Attacking Weapons", value=mapDetails[1], inline=True)
            embed.add_field(name="Attacking Equipment", value=mapDetails[2], inline=True)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="Defending Weapons", value=mapDetails[3], inline=True)
            embed.add_field(name="Defending Equipment", value=mapDetails[4], inline=True)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.add_field(name="Vehicles", value=mapDetails[5], inline=True)
            image_url = mapDetails[0]
            if image_url and image_url.startswith("http"):
                embed.set_image(url=image_url)
            embedList.append(embed)

        # 2. SEND THE FINAL EMBEDS
        # Since we used defer(), we must use interaction.followup.send instead.
        await interaction.followup.send(embeds=embedList)

    except Exception as e:
        # If any error occurs during processing, report it to the user.
        await interaction.followup.send(f"An error occurred: {e}", ephemeral=True)

@bot.tree.command(name="purge", description="Purge the last x messages from current channel")
@app.commands.describe(amount="Amount of messages to delete")
async def purge(interaction: discord.Interaction, amount: int):
        await interaction.response.send_message(f"Deleting {amount} messages", ephemeral=True)
        await interaction.channel.purge(limit=amount)

@purge.error
async def clear_error(interaction: discord.Interaction, error):
    if isinstance(error, app.commands.MissingPermissions):
        await interaction.response.send_message("You do not have permission to delete messages.", ephemeral=True)



def getToken():
    token = os.environ.get("DISCORD_TOKEN")
    if token is None:
        print("ERROR: DISCORD_TOKEN environment variable not found")
    return token

bot.run(getToken)    
