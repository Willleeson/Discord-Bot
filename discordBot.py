"""Discord Bot Posiedon Main Function"""
from maps import raidMaps
import discord
from discord.ext import commands
from discord import app_commands as app
import random

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



    async def on_message(self, message):
        # This line is crucial! It allows !commands to work alongside on_message
        await self.process_commands(message) 
        print(f'Message from {message.author}: {message.content} ({message.channel}, {message.channel.category}, {message.channel.mention})')

bot = MyBot()


@bot.tree.command(name="repeat",description="Repeats what you feed it.")
@app.commands.describe(repeat_message="Message to repeat")
async def repeat(interaction: discord.Interaction, repeat_message: str):
    await interaction.response.send_message(repeat_message)


@bot.tree.command(name="average",description="Gives you the average of a certain number of inputs where input is an integer")
@app.commands.describe(num1="First Number",
                       num2="Second Number",
                       num3="Third Number",
                       num4="Fourth Number"
)
async def average(interaction: discord.Interaction, num1: int, num2: int, num3: int, num4: int):
    print(type(num1))
    sum = int(num1) + int(num2) + int(num3) + int(num4)
    avg = sum / 4
    await interaction.response.send_message(avg)


@bot.tree.command(name="servers", description="Aims to show which servers the user is in.")
@app.commands.describe(user="Mention user with @ to find servers")
async def servers(interaction: discord.Interaction, user: discord.Member = None):
    target_user = user or interaction.user
    shared_guilds = target_user.mutual_guilds
    if shared_guilds:
        server_names = ",".join([guild.name for guild in shared_guilds])
        await interaction.response.send_message(f"Shared guilds with user: {target_user.mention} \nServers:\n {server_names}")
    else:
        await interaction.response.send_message(f"Posiedon does not share any guilds with {target_user.mention}")



"""
TODO
Write a function that checks mutual servers with the bot, 
if len > 1 then 
    display server with roles in it and nick


"""

# MADE GEMINI CREATE A COMMAND TO CLEAR UP CONFUSION FROM THE DOCUMENTATION TO UNDERSTAND HOW TO MAKE EMBEDS IN DISCORD
#CONSIDER MAKING A DICTIONARYU THAT PULLS A NAME ON A RANDOM NUMBER THEN REFERENCES THAT NAME IN A SEPERATE DICTIONARY WHICH POINTS TO A LIST OF DATA AND THEN USE "info[elemnt]" to pull specific data ;ike screenshot or attacking weapon details etc. 
@bot.tree.command(name="maps", description="Show 3 randomly selected maps based on size category and such.")
async def games(interaction: discord.Interaction):
    # 1. Define your data (This mimics the data in your screenshot)
    # You would normally fetch this from your text file or database/API
    match_data = [
        {"title": "Map 1", "map": "Site Kronos", "size": "8v8", "color": discord.Color.green(), "image": "https://raw.githubusercontent.com/Willleeson/Discord-Bot/429d41843b31ff18d16eb8ab58a53b4e7dfa5fe0/mapScreenShots/siteKronos.png"},
        {"title": "Map 2", "map": "Solitude", "size": "Slayer", "color": discord.Color.green(), "image": ""},
        {"title": "Map 3", "map": "Recharge", "size": "Strongholds", "color": discord.Color.green(), "image": ""}]
    # 2. Create a list to hold the embeds
    # Discord allows up to 10 embeds in a single message
    embed_list = []

    for match in match_data:
        # Create the embed object
        embed = discord.Embed(
            title=match["title"],
            color=match["color"] # This sets the sidebar color
        )

        # Add the "Map" field
        embed.add_field(name="Map", value=match["map"], inline=True)
        
        # Add the "Mode" field
        # inline=True makes them sit next to each other
        embed.add_field(name="Size", value=match["size"], inline=True)

        # Set the image on the right side
        # NOTE: You must use a valid URL (http/https) for images
        embed.set_thumbnail(url=match["image"])

        # Add to our list
        embed_list.append(embed)

    # 3. Send the list of embeds
    # Note the parameter is 'embeds=' (plural) and takes a list
    await interaction.response.send_message(embeds=embed_list)



bot.run("")