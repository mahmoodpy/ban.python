import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.command()
async def ban(ctx, member: discord.Member = None, *, reason: str = None):
    if member is None:
        await ctx.send(f"{ctx.author.mention},الرجاء ادخل اسم المستخدم")
        return
    # Check if the user has the ban_members permission
    if not ctx.message.author.guild_permissions.ban_members:
        await ctx.send(f"{ctx.author.mention},ليس لديك الصلاحيات الازمه")
        return
    await member.ban(reason=reason)
    await ctx.send(f"{member} تم حظره.:airplane:")

bot.run("Token.bot")