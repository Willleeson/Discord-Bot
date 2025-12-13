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

bot = MyBot()

@bot.tree.command(name="servers", description="Aims to show which servers the user is in.")
@app.commands.describe(user="Mention user with @ to find servers")
async def servers(interaction: discord.Interaction, user: discord.Member = None):
    """
    TODO 
    if len > 1 then 
        display server with roles in it and nick
    """
    target_user = user or interaction.user
    shared_guilds = target_user.mutual_guilds
    if shared_guilds:
        server_names = ",".join([guild.name for guild in shared_guilds])
        await interaction.response.send_message(f"Shared guilds with user: {target_user.mention} \nServers:\n {server_names}")
    else:
        await interaction.response.send_message(f"Posiedon does not share any guilds with {target_user.mention}")



@bot.tree.command(name="raid", description="Random Selection of 3 Raid Maps")
@app.commands.describe(size="Size of Raid, 8 for 8v8. 10 for 10v10. 12 for 12v12")
@app.commands.choices(size=[
    app.commands.Choice(name="8v8", value=8),
    app.commands.Choice(name="10v10", value=10),
    app.commands.Choice(name="12v12", value=12)])
async def raid(interaction: discord.Interaction, size: app.commands.Choice[int]):
    selected_size = size.value
    raid = raidMaps(selected_size, "raid")
    nMaps = raid.getMapCount(selected_size)
    embedList = []
    rNumber = random.sample(range(1, nMaps + 1), min(3, nMaps))

    for index, mapIndex in enumerate(rNumber, 1):
        mapName = raid.getMap(mapIndex, selected_size)
        mapDetails = raid.getMapDetail(mapName)
        if mapDetails is None:
            errorEmbed = discord.Embed(
                title=f"Map {index}",
                description=f"Details not found. Please check code for name. {mapName}",
                color=discord.Color.red())
            embedList.append(errorEmbed)
            continue
        embed = discord.Embed(
            title=f"Map {index}",
            color=discord.Color.blue())

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


    await interaction.response.send_message(embeds=embedList)

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
    try:
        with open("token.txt", "r") as file:
            token = file.readline().strip()
            return token
    except FileNotFoundError:
        print("token.txt was not found in folder.")
        return None

bot.run(getToken())

