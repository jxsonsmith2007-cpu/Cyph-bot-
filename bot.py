import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def socials(ctx):
    embed = discord.Embed(
        title="📱 Cyph Socials",
        color=discord.Color.blue()
    )

    embed.add_field(
    name="TikTok",
    value="https://www.tiktok.com/@7cyph?_r=1&_t=ZS-97WHJqf8Dyx",
    inline=False
)
    embed.add_field(
    name="YouTube",
    value="https://youtube.com/@7cyph?si=xKPkoINe0_EzP2NU",
    inline=False
)
    await ctx.send(embed=embed)
    embed.set_footer(text="Prefix: ! • Bot made by Sofflyze")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()
    if "cyph sens" in content or "cyph sensitivity" in content:
        await message.channel.send(
        "🎯 You can check out Cyph's sensitivity here:\nhttps://discord.com/channels/1277694157481185320/1471329658254393374/1505281063180701736"
    )
    elif "cyph settings" in content:
        await message.channel.send(
        "⚙️ You can check out Cyph's settings here:\nhttps://discord.com/channels/1277694157481185320/1471329658254393374"
    )
    elif any(phrase in content for phrase in [
    "get roles",
    "roles",
    "role menu",
    "how can i get roles",
    "where can i get roles"
]):
    elif any(word in content for word in [
    "fleasion",
    "flea",
    "hitsound",
    "fleas"
]):
        await message.channel.send(
        "🎧 You can check out Fleasion's settings, sensitivity and hit sounds here:\nhttps://discord.com/channels/1277694157481185320/1490445210948472842"
    )
    await bot.process_commands(message)

bot.run(TOKEN)