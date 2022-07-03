from time import time
import discord
import datetime
import random
from discord.ext import commands
import os
import json
import asyncio

class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def giveaway(self, ctx, *, arg):
        embed = discord.Embed(title="Giveaway", description=f"React to this message with 🎉 to enter the giveaway for **{arg}**", color=0x00ff00)
        embed.set_footer(text=f"Time started at: {datetime.datetime.now()}. Made by: {ctx.author}")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("🎉")
        await asyncio.sleep(10)
        feteched_message = await ctx.channel.fetch_message(msg.id)
        reactions = feteched_message.reactions
        for reaction in reactions:
            if reaction.emoji == "🎉":
                users = await reaction.users().flatten()
        winner = random.choice(users)
        embed = discord.Embed(title="Giveaway", description=f"**{winner}** has won the giveaway for **{arg}**", color=0x00ff00)
        await ctx.send(embed=embed)
        

                
        
       
        


        
def setup(client):
    client.add_cog(Giveaway(client)) 