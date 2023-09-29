##################################################################################

# Developer = Tryhardrip 
# DiscordID = tryhardrip
# Discord Server = https://discord.gg/4VgGnZfKA2
##################################################################################

import datetime
import discord
import asyncio
import json
from discord.ui import *
from discord.ext import commands
from discord.ext.commands import has_permissions
from pytz import timezone

with open("config.json", mode="r") as config_file:
    config = json.load(config_file)

BOT_TOKEN = config["token"]  
BOT_PREFIX = config["prefix"]
TIMEZONE = config["timezone"]
MESSAGE_1 = config["message_1"]
MESSAGE_2 = config["message_2"]
ACTIVITY = config["activity"]
GUILD_ID = config["guild_id"]
TICKET_CHANNEL = config["ticket_channel_id"]
CATEGORY_ID1 = config["category_id_1"]
CATEGORY_ID2 = config["category_id_2"]
CATEGORY_ID3 = config["category_id_3"]
CATEGORY_ID4 = config["category_id_4"]
TEAM_ROLE1 = config["team_role_id_1"] 
LOG_CHANNEL = config["log_channel_id"]


bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    bot.add_view(MyView())
    bot.add_view(delete())
    print(f"Login in as {bot.user.name}")
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Game(name=ACTIVITY))
    print(f"Activity on {bot.user.name}")


class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(
        custom_id="support",
        placeholder="Select",
        options=[
            discord.SelectOption(
                label="Staff Application",
                emoji="🤝",
                value="support1"
            ),
            discord.SelectOption(
                label="Player Report",
                emoji="🕵️‍♂️",
                value="support2"
            ),
            discord.SelectOption(
                label="Others",
                emoji="📩",
                value="support3"
            ),
            discord.SelectOption(
                label="Buy Rank",
                emoji="🛒",
                value="support4"
            )
        ]
    )
    async def callback(self, select, interaction):
        if "support1" in interaction.data['values']:
            if interaction.channel.id == TICKET_CHANNEL:
                guild = bot.get_guild(GUILD_ID)
                for ticket in guild.channels:
                    if str(interaction.user.id) in ticket.name:
                        embed = discord.Embed(title=f"You can only open one Ticket!", description=f"Here is your opend Ticket {ticket.mention}", color=0xff0000)
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        await asyncio.sleep(3)
                        embed = discord.Embed(title="**Ticket Selector**", description=MESSAGE_1, color=0x00ff00)
                        await interaction.message.edit(embed=embed, view=MyView())
                        return
                category = bot.get_channel(CATEGORY_ID1)
                ticket_channel = await guild.create_text_channel(f"Staff-Apply-{interaction.user}-{interaction.user.id}", category=category,
                                                                topic=f"Ticket from {interaction.user} \nUser-ID: {interaction.user.id}")

                await ticket_channel.set_permissions(guild.get_role(TEAM_ROLE1), send_messages=True, read_messages=True, add_reactions=False,
                                                    embed_links=True, attach_files=True, read_message_history=True,
                                                    external_emojis=True)
                await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=False,
                                                    embed_links=True, attach_files=True, read_message_history=True,
                                                    external_emojis=True)
                await ticket_channel.set_permissions(guild.default_role, send_messages=False, read_messages=False, view_channel=False)
                embed = discord.Embed(description=f'{MESSAGE_2}',
                                                color=0x00ff00)
                await ticket_channel.send(embed=embed, view=delete())

                embed = discord.Embed(description=f'Ticket was Created! Look here {ticket_channel.mention}',
                                        color=discord.colour.Color.green())
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await asyncio.sleep(3)
                embed = discord.Embed(title="**Ticket Selector**", description=MESSAGE_1, color=0x00ff00)
                await interaction.message.edit(embed=embed, view=MyView())
                return
        if "support2" in interaction.data['values']:
            if interaction.channel.id == TICKET_CHANNEL:
                guild = bot.get_guild(GUILD_ID)
                for ticket in guild.channels:
                    if str(interaction.user.id) in ticket.name:
                        embed = discord.Embed(title=f"You can only open one Ticket!", description=f"Here is your opend Ticket {ticket.mention}", color=0xff0000)
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        await asyncio.sleep(3)
                        embed = discord.Embed(title="**Ticket Selector**", description=MESSAGE_1, color=0x00ff00)
                        await interaction.message.edit(embed=embed, view=MyView())
                        return
                category = bot.get_channel(CATEGORY_ID2)
                ticket_channel = await guild.create_text_channel(f"Player-Report-{interaction.user}-{interaction.user.id}", category=category,
                                                                topic=f"Ticket from {interaction.user} \nUser-ID: {interaction.user.id}")

                await ticket_channel.set_permissions(guild.get_role(TEAM_ROLE1), send_messages=True, read_messages=True, add_reactions=False,
                                                    embed_links=True, attach_files=True, read_message_history=True,
                                                    external_emojis=True)
                await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=False,
                                                    embed_links=True, attach_files=True, read_message_history=True,
                                                    external_emojis=True)
                await ticket_channel.set_permissions(guild.default_role, send_messages=False, read_messages=False, view_channel=False)
                embed = discord.Embed(description=f'{MESSAGE_2}',
                                                color=0x00ff00)
                await ticket_channel.send(embed=embed, view=delete())

                embed = discord.Embed(description=f'Ticket was Created! Look here {ticket_channel.mention}',
                                        color=discord.colour.Color.green())
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await asyncio.sleep(3)
                embed = discord.Embed(title="**Ticket Selector**", description=MESSAGE_1, color=0x00ff00)
                await interaction.message.edit(embed=embed, view=MyView())
                return
        if "support3" in interaction.data['values']:
            if interaction.channel.id == TICKET_CHANNEL:
                guild = bot.get_guild(GUILD_ID)
                for ticket in guild.channels:
                    if str(interaction.user.id) in ticket.name:
                        embed = discord.Embed(title=f"You can only open one Ticket", description=f"Here is your opend Ticket {ticket.mention}", color=0xff0000)
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        await asyncio.sleep(3)
                        embed = discord.Embed(title="**Ticket Selector**", description=MESSAGE_1, color=0x00ff00)
                        await interaction.message.edit(embed=embed, view=MyView())
                        return 
                category = bot.get_channel(CATEGORY_ID3)
                ticket_channel = await guild.create_text_channel(f"Ticket-Others-{interaction.user}-{interaction.user.id}", category=category,
                                                                    topic=f"Ticket from {interaction.user} \nUser-ID: {interaction.user.id}")
                await ticket_channel.set_permissions(guild.get_role(TEAM_ROLE1), send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(guild.default_role, send_messages=False, read_messages=False, view_channel=False)
                embed = discord.Embed(description=f'{MESSAGE_2}',
                                                    color=0x00ff00)
                await ticket_channel.send(embed=embed, view=delete())

                embed = discord.Embed(description=f'Ticket was Created! Look here {ticket_channel.mention}',
                                        color=discord.colour.Color.green())
                await interaction.response.send_message(embed=embed, ephemeral=True)

                await asyncio.sleep(3)
                embed = discord.Embed(title="**Ticket Selector**", description=MESSAGE_1, color=0x00ff00)
                await interaction.message.edit(embed=embed, view=MyView())
                return
        if "support4" in interaction.data['values']:
            if interaction.channel.id == TICKET_CHANNEL:
                guild = bot.get_guild(GUILD_ID)
                for ticket in guild.channels:
                    if str(interaction.user.id) in ticket.name:
                        embed = discord.Embed(title=f"You can only open one Ticket", description=f"Here is your opend Ticket {ticket.mention}", color=0xff0000)
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        await asyncio.sleep(3)
                        embed = discord.Embed(title="**Ticket Selector**", description=MESSAGE_1, color=0x00ff00)
                        await interaction.message.edit(embed=embed, view=MyView())
                        return 
                category = bot.get_channel(CATEGORY_ID4)
                ticket_channel = await guild.create_text_channel(f"Ticket-Buy-Rank-{interaction.user}-{interaction.user.id}", category=category,
                                                                    topic=f"Ticket from {interaction.user} \nUser-ID: {interaction.user.id}")
                await ticket_channel.set_permissions(guild.get_role(TEAM_ROLE1), send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(guild.default_role, send_messages=False, read_messages=False, view_channel=False)
                embed = discord.Embed(description=f'{MESSAGE_2}',
                                                    color=0x00ff00)
                await ticket_channel.send(embed=embed, view=delete())

                embed = discord.Embed(description=f'Ticket was Created! Look here {ticket_channel.mention}',
                                        color=discord.colour.Color.green())
                await interaction.response.send_message(embed=embed, ephemeral=True)

                await asyncio.sleep(3)
                embed = discord.Embed(title="**Ticket Selector**", description=MESSAGE_1, color=0x00ff00)
                await interaction.message.edit(embed=embed, view=MyView())
        return

class delete(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🔒 Close Ticket", style = discord.ButtonStyle.red, custom_id="close")
    async def close(self, button: discord.ui.Button, interaction: discord.Interaction):
        channel = bot.get_channel(LOG_CHANNEL)

        fileName = f"Transcript/{interaction.channel.name}.html"
        with open(fileName, "w", encoding='utf-8') as file:
            async for msg in interaction.channel.history(limit=None, oldest_first=True):
                time = msg.created_at.replace(tzinfo=timezone('UTC')).astimezone(timezone(TIMEZONE))
                file.write(f"(TIME: {time}) (USER: {msg.author.display_name}) (MSG: {msg.clean_content})<br>\n")

        embed = discord.Embed(
                description=f'Ticket is Closing in 5 Second.',
                color=0xff0000)
        embed2 = discord.Embed(title="Ticket Closed!", description=f"Ticket-Name: {interaction.channel.name}\n Closed-From: {interaction.user.name}\n Transcript: ", color=0x00ff00)
        file = discord.File(fileName)
        await interaction.response.send_message(embed=embed)
        await channel.send(embed=embed2)
        await asyncio.sleep(1)
        await channel.send(file=file)
        with open(f"Transcript/{interaction.channel.name}.html", "rb") as file:
           await interaction.user.send(embed=embed2)
           await interaction.user.send(file=discord.File(file, f"Transcript/{interaction.channel.name}.html"))
        await asyncio.sleep(5)
        await interaction.channel.delete(reason="Ticket closed by user")

@bot.command()
@has_permissions(administrator=True)
async def ticket(ctx):
    channel = bot.get_channel(TICKET_CHANNEL)
    embed = discord.Embed(title="**Ticket Selector**", description=MESSAGE_1, color=0x00ff00)
    await channel.send(embed=embed, view=MyView())

@bot.command()
async def close(ctx):
    channel = bot.get_channel(LOG_CHANNEL)

    fileName = f"Transcript/{ctx.channel.name}.html"
    with open(fileName, "w", encoding='utf-8') as file:
        async for msg in ctx.channel.history(limit=None, oldest_first=True):
            time = msg.created_at.replace(tzinfo=timezone('UTC')).astimezone(timezone(TIMEZONE))
            file.write(f"(TIME: {time}) (USER: {msg.author.display_name}) (MSG: {msg.clean_content})<br>\n")

    embed = discord.Embed(description=f'Ticket is Closing in 5 Second.',color=0xff0000)
    embed2 = discord.Embed(title="Ticket Closed!", description=f"Ticket-Name: {ctx.channel.name}\n Closed-From: {ctx.author.name}\n Transcript: ", color=0x00ff00)
    file = discord.File(fileName)
    await ctx.reply(embed=embed)
    await channel.send(embed=embed2)
    await asyncio.sleep(1)
    await channel.send(file=file)
    with open(f"Transcript/{ctx.channel.name}.html", "rb") as file:
        await ctx.author.send(embed=embed2)
        await ctx.author.send(file=discord.File(file, f"Transcript/{ctx.channel.name}.html"))
    await asyncio.sleep(5)
    await ctx.channel.delete(reason="Ticket closed by user")

bot.run(BOT_TOKEN)
