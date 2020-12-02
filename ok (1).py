import discord
from discord import HTTPException
from discord.ext import commands
from discord.ext.commands import errors
from discord.utils import get


bot = commands.Bot(command_prefix="!")
bot.remove_command('help')

token = "NzgzNjAwNzkxMDI5MTUzODAz.X8dHGw.oQbf-CbLOVUC2Mnl83HX2_WY28c"

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="AMservice"))
    print("============================================")
    print(f"로그인 정보 : {bot.user.name}({bot.user.id})")
    print("환영합니다.")
    print("============================================")


@bot.command()
@commands.has_permissions(administrator=True)
async def 공지(title = str, desc = str, mention = None):
    em = discord.Embed(
        title=title,
        description=desc,
        color=0x00FF00,
    )
    channel = bot.get_channel(777666047616352286)
    await channel.send(embed=em)
    if mention == None:
        pass
    else:
        channel = bot.get_channel(777666047616352286)
        await channel.send(mention)

@bot.command()
@commands.has_permissions(administrator=True)
async def 퇴근(ctx):
        em = discord.Embed(
            title="퇴근",
            description=ctx.message.author.display_name+"님이 퇴근하셨습니다.",
            color=0x00FF00,
        )
        user = bot.get_channel(783286814630608986)
        await user.send(embed=em)

        em = discord.Embed(
            title="완료",
            description="삐빅 퇴근입니다",
            color=0x00FF00,
        )
        await ctx.send(embed=em)

@bot.command()
@commands.has_permissions(administrator=True)
async def 출근(ctx):
        em = discord.Embed(
            title="출근",
            description=ctx.message.author.display_name+"님이 출근하셨습니다.",
            color=0x00FF00,
        )
        user = bot.get_channel(783286814630608986)
        await user.send(embed=em)

        em = discord.Embed(
            title="완료",
            description="삐빅 출근입니다",
            color=0x00FF00,
        )
        await ctx.send(embed=em)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members == True:
        try:
            embed=discord.Embed(title=f"{ctx.guild.name}에서 차단되셨습니다.")
            if reason == None:
                reason = '없음'
            embed.add_filed(name="사유", value=reason)
            await bot.get_user(member.id).send(embed=embed)
        except Exception as error:
            pass
        await member.ban()
    else:
        embed=discord.Embed(title="에러", description=f"그 유저를 차단시킬 권한이 없습니다! 권한을 추가하신 후 다시 시도해주십시오.")
        await ctx.send(embed=embed)
        return

@bot.command()
async def 킥(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members == True:
        try:
            embed=discord.Embed(title=f"{ctx.guild.name}에서 추방되셨습니다.")
            if reason == None:
                reason = '없음'
            embed.add_filed(name="사유", value=reason)
            await bot.get_user(member.id).send(embed=embed)
        except Exception as error:
            pass
        await member.kick()
    else:
        embed=discord.Embed(title="에러", description=f"그 유저를 추방시킬 권한이 없습니다! 권한을 추가하신 후 다시 시도해주십시오.")
        await ctx.send(embed=embed)
        return

bot.run(token)