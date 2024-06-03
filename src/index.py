import os
import discord
import ollama
import datetime
from ollamabot import Ollamabot
from discord.ext import commands
from dotenv import load_dotenv


# INITIALIZE MAIN OBJECTS
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix="+", intents=intents)

ollama.chat(model='llama2', messages=[
    {
    'role': 'user',
    'content': 'Necesito que hables en español.',
    }
])

player = Ollamabot(bot, ollama)


"""Information about the bot usage."""
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title=f"DisMusic",
        description="Im a music player bot",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.purple()
    )

    embed.add_field(name="Bot Owner",      value="xabierprg",                                   inline=False)
    embed.add_field(name="GitHub",         value="https://github.com/xabierprg/DisMusic",       inline=False)
    embed.add_field(name="Commands",       value="paste '-commands' to see all my commands",    inline=False)

    await ctx.send(embed=embed)
    
    
"""Launch event when the bot is ready."""
@bot.event
async def on_ready():
    print("Logged in as:\n{0.user.name}\n{0.user.id}".format(bot))
    
    
"""Ask command."""
@bot.command()
async def ask(ctx, *, msg):
    await player.ask(ctx, msg)



# MAIN THREAD
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(DISCORD_TOKEN)

