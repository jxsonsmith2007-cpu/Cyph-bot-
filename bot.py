import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
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

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="📖 Commands",
        color=discord.Color.blue()
    )

    embed.add_field(
    name="ℹ️ Info",
    value=(
        "`!ping` — Bot latency\n"
        "`!avatar [@user]` — Show avatar\n"
        "`!userinfo [@user]` — User info\n"
        "`!serverinfo` — Server info\n"
        "`!socials` — Cyph's TikTok & YouTube"
    ),
    inline=False
    )
    embed.add_field(
    name="🎮 Games",
    value=(
        "`!coinflip` — Flip a coin\n"
        "`!dice` — Roll a die\n"
        "`!8ball <question>` — Magic 8-ball\n"
        "`!rps <rock/paper/scissors>` — Play vs the bot\n"
        "`!guess` — Guess a number"
    ),
    inline=False
    )
    embed.add_field(
    name="📊 Stats",
    value=(
        "`!iq [@user]` — IQ test (1-300)\n"
        "`!love @user1 @user2` — Love meter\n"
        "`!ship @user1 @user2` — Compatibility\n"
        "`!sus @user` — Sus level\n"
        "`!clown @user` — Clown level\n"
        "`!simp @user` — Simp level\n"
        "`!rate <thing>` — Rate anything"
    ),
    inline=False
    )
    embed.add_field(
    name="😂 Fun",
    value=(
        "`!roast @user` — Roast someone\n"
        "`!compliment @user` — Compliment someone\n"
        "`!fight @user1 @user2` — Simulate a fight\n"
        "`!hack @user` — Hack someone (fake)\n"
        "`!joke` — Random joke\n"
        "`!fact` — Random fact\n"
        "`!meme` — Random meme"
    ),
    inline=False
    )
    
    embed.set_footer(text="Prefix: ! • Bot made by Sofflyze")
    await ctx.send(embed=embed)
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()
    if content in ["sens", "sensitivity"]:
        await message.channel.send(
        "🎯 You can check out Cyph's sensitivity here:\nhttps://discord.com/channels/1277694157481185320/1471329658254393374/1505281063180701736"
    )
    elif content in ["settings", "game settings"]:
        await message.channel.send(
        "⚙️ You can check out Cyph's settings here:\nhttps://discord.com/channels/1277694157481185320/1471329658254393374"
    )
    elif content in [
    "fleasion",
    "flea",
    "fleasion settings",
    "fleasion sens",
    "fleasion sensitivity",
    "fleasion hitsounds"
]:
        await message.channel.send(
        "🎧 You can check out Fleasion's settings, sensitivity and hit sounds here:\nhttps://discord.com/channels/1277694157481185320/1490445210948472842"
    )
    await bot.process_commands(message)

bot.run(TOKEN)