import discord
from discord.ext import commands
from ping3 import ping

print("Starting bot...")

TOKEN = open("token.txt","r").readline()
client = commands.Bot(command_prefix = 'ith')
sea = ping('8.8.8.8')
eu = ping('ping.eu')

#We delete default help command
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot Ready!')
    await client.change_presence(activity=discord.Game('Finding The Lost Vario'))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Finding The Lost Vario 1250cc'))
    #await client.change_presence(activity=discord.Streaming(name='Sea of Thieves', url='https://www.twitch.tv/your_channel_here'))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Ciomean Vibes'))

#answers with the ms latency
@client.command()
async def ping(ctx):
    embed = discord.Embed(colour = discord.Colour.green())
    embed.set_image(url="https://cdn.discordapp.com/attachments/702868514750332959/776723557464014868/ping2.png")
    #embed.set_author(name="ANDA NGELAG")
    embed.add_field(name='SEA', value=f'{round(sea * 1000)}ms', inline=False)
    embed.add_field(name='EU', value=f'{round(eu * 1000)}ms', inline=False)
    embed.add_field(name='US', value=f'{round (client.latency * 1000)}ms', inline=False)
    await ctx.send(embed=embed)
    print('Ping Sent!')


#Embeded help with list and details of commands
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.green())
    embed.set_author(name='Syntax yang tersedia')
    embed.add_field(name='ithping', value='Ngetest PING Lurr', inline=False)
    await ctx.send(embed=embed)
    print('Help Sent!')

@client.command(pass_context=True)
async def algi(ctx):
    await ctx.send('**User Vario 1250cc**')
    print('Ciomean Sent!')

@client.command(pass_context=True)
async def manzip(ctx):
    await ctx.send('**CEO of InTheHouse**')
    print('Manzip Sent!')

#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Salah Lurr. Coba ithhelp ({error})')
    print('Salah Sent!')


print("Bot is ready!")
client.run(TOKEN)