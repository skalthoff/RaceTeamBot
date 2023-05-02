import discord
from discord.ext import commands

class Attendance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='create_attendance')
    async def _create_attendance(self, ctx, *, description: str):
        embed = discord.Embed(
            title="Attendance Check",
            description=description,
            color=discord.Color.blue()
        )
        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("❌")

def setup(bot):
    bot.add_cog(Attendance(bot))
