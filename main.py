import requests
import asyncio
import random
import discord
from datetime import datetime
from discord.ext import commands

#  from keep_alive import keep_alive

# setup intent
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# bot token
token = "MTAyODc5MzI3NzkzNzM1NjkzMQ.GQmMk_.7bdXijHmfS2QzGEg8asSg1X4AHlmuiYnjyYd6o"

# List of donuts
donutList = [
    'LongJohn - With cream',
    'Original Glazed ',
    "Vegan Original  ",
    "Personalised OG ",
    "Sprinkles ",
    "Devil's Food",
    "Mini Original Glazed ",
    "Mini Chocolate ",
    "Cookies and Kreme ",
    "Lemmon Meringue pie ",
    "Apple Cinnamon ",
    "Chocolate Sprinkles ",
    "Maple Iced ",
    "Glazed Cruller ",
    "Millionaire Shortbread",
    "Chocolate DreamCake ",
    "Plain Cake ",
    "Glazed Twist ",
    "Chocolate glazed twist",
    "Glazed Buttermilk ",
    "Plain Buttermilk ",
    "Chocolate Long John w/cream",
    "Maple Long w/cream",
    "Choco Long John ",
    "Maple Long John ",
    "Raspberry Jelly ",
    "Apple Crepe ",
    "Cinamamon Roll",
    "Deanut Special-Free Of Charge, on the house "
]

# donut image list
donutImage = ['https://i.redd.it/ivz2pesrcpg11.jpg',
              'https://media.discordapp.net/attachments/520881988844912645/1029034105444237362/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029060697553911938/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029060561759117433/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029060561759117433/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029060383157260358/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029060183000879144/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029060065270960198/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029060013039308920/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029059816846532661/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029059681873842186/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029056965529309234/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029057435287171072/unknown.png',
              'https://cdn.discordapp.com/attachments/1029589995192864798/1029764293425647686/unknown.png',
              'https://cdn.discordapp.com/attachments/1029589995192864798/1029752446102286410/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029057435287171072/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029056965529309234/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029056825494085722/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029056344998813906/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029056427333001226/unknown.png',
              'https://media.discordapp.net/attachments/1028821108570468405/1029055252999192617/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029055546420101190/unknown.png',
              'https://media.discordapp.net/attachments/520881988844912645/1029034105444237362/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029055546420101190/unknown.png',
              'https://media.discordapp.net/attachments/1028821108570468405/1029055686480494662/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029056000143138887/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029055933558562887/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029055252999192617/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029054764501188748/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029054565242380359/unknown.png',
              'https://media.discordapp.net/attachments/520881988844912645/1029035566605553804/unknown.png',
              'https://cdn.discordapp.com/attachments/1028821108570468405/1029053557946732585/unknown.png'
              ]

# waffle list
waffle = [
    'https://tenor.com/view/waffles-waffle-syrup-food-yummy-gif-16668016',
    'https://tenor.com/view/waffle-wednesday-donkey-shrek-diet-fail-gif-11559312',
    'https://tenor.com/view/waffle-gif-24469753'
]

# Donut words to listen for
donutCatcher = [
    "donut", "Donut", "DONUT", "DONUTS", "Donuts", "donuts", "Doughnuts"
]

# Names of people that can get a donut
nameList = [
    'deano', 'zero', 'camo', 'Tchapz', 'Newb', 'Daha', 'Jeff', 'Tony', 'Cleo',
    'Doddy'
]

# empty arrays for each user to hold each keep track of each user's donut
deano = []
zero = []
newb = []
tchapz = []
daha = []
jeff = []
tony = []
cleo = []
camo = []
doddy = []
bigdog = []
leaderboard = {'**Newb**': 0,
               '**Zero**': 0,
               '**BigDog**': 0,
               '**Camo**': 0,
               '**Deano**': 0,
               '**Tchapz**': 0}


# return connection success to console on connection
@client.event
async def on_ready():
    print("Waking up bot........Successfully connected!")


# message events listener
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    count = 0
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    startReset = '00:00:00'
    endReset = '00:00:10'
    msg = message.content
    randomDonut = random.choice(donutList)
    randomImage = random.choice(donutImage)

    # send a random donut if the user uses command
    if msg == ("!donut"):
        await message.channel.send(randomDonut)

    # donut king
    if msg == ('!dk'):
        await message.channel.send(
            f'https://cdn.discordapp.com/attachments/520881988844912645/1030939530037035108/IMG_9339.png')

    # not that old chestnut
    if msg == ("!toc"):
        await message.channel.send(
            'https://tenor.com/view/not-that-old-chesnut-stale-joke-repeated-joke-old-joke-not-funny-anymore-gif-25841198')

    # who asked
    if msg == ("!whoasked"):
        await message.channel.send(
            'https://media.discordapp.net/attachments/520881988844912645/1019349743438143570/IMG_9022.png?width=702&height=702'
        )

    # mute your mic
    if msg == ('!mm'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/1028821108570468405/1029172223744934019/unknown.png'
        )
    # refer to pinned images
    if msg == ('!refer'):
        await message.channel.send(
            f"*please refer to pinned images section 5.2 subsection 3*")

    # waffle
    if msg == ('!waffle'):
        await message.channel.send(random.choice(waffle))

    # names of all who can get a donut
    if msg == ('!names'):
        await message.channel.send(nameList)

    # give donut
    if msg == ("!gdonut"):
        await message.channel.send(f"*Who would you like to give donut(s) to?*"
                                   )
        await message.channel.send(
            f"*reply with '!names' to see who can receive a donut or !(name of the person) to give them a donut*"
        )

    # show contract
    if msg == ('!contract'):
        await message.channel.send(f'https://media.discordapp.net/attachments/520881988844912645/1031690831859560448/Donut_3.PNG?width=541&height=702')
        await message.channel.send(f'https://media.discordapp.net/attachments/520881988844912645/1031690832237056061/Donut_4.PNG?width=544&height=702')

    # Give donuts to users on the discord
    if msg == '!deano'.lower():
        author = message.author.roles
        for i in author:
            if i.name == 'No Perms':
                await message.channel.send('No acess!')
                return
        else:
            await message.channel.send(f'{randomDonut} **Was given to Deano**')
            await message.channel.send(f'{randomImage}')
            deano.append(randomDonut)
        for i in deano:
            count += 1
            leaderboard['**Deano**'] = count
        pass
    if msg == ('!Zero').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'No Perms':
                await message.channel.send('No access!')
                return
        else:
            await message.channel.send(f'{randomDonut} **Was given to Zero**')
            await message.channel.send(f'{randomImage}')
            zero.append(randomDonut)
        for i in zero:
            count += 1
            leaderboard['**Zero**'] = count
        pass
    if msg == ('!camo').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'No Perms':
                await message.channel.send('No access!')
                return
        else:
            await message.channel.send(f'{randomDonut} **Was given to Camo**')
            await message.channel.send(f'{randomImage}')
            camo.append(randomDonut)
        for i in camo:
            count += 1
            leaderboard['**Camo**'] = count
        pass
    if msg == ('!Newb').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'No Perms':
                await message.channel.send('No access!')
                return
        else:
            await message.channel.send(f'{randomDonut} **Was given to Newb**')
            await message.channel.send(f'{randomImage}')
            newb.append(randomDonut)
        for i in newb:
            count += 1
            leaderboard['**Newb**'] = count
        pass
    if msg == ('!tchapz').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'No Perms':
                await message.channel.send('No access!')
                return
        else:
            await message.channel.send(f'{randomDonut} **Was given to Tchapz**')
            await message.channel.send(f'{randomImage}')
            tchapz.append(randomDonut)
        for i in tchapz:
            count += 1
            leaderboard['**Tchapz**'] = count
        pass
    if msg == ('!Doddy').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'No Perms':
                await message.channel.send('No access!')
                return
        else:
            await message.channel.send(f'{randomDonut} **Was given to Doddy**')
            await message.channel.send(f'{randomImage}')
            doddy.append(randomDonut)
        for i in doddy:
            count += 1
            leaderboard['**Doddy**'] = count
        pass
    if msg == ('!bigdog').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'No Perms':
                await message.channel.send('No access!')
                return
        else:
            await message.channel.send(f'{randomDonut} **Was given to BigDog**')
            await message.channel.send(f'{randomImage}')
            bigdog.append(randomDonut)
        for i in bigdog:
            count += 1
            leaderboard['**BigDog**'] = count
        pass

    # to check the list of donuts owned
    if msg == ('!newblist').lower():
        for i in newb:
            await message.channel.send(f'**{i}**')
    if msg == ('!camolist').lower():
        for i in camo:
            await message.channel.send(f'**{i}**')
    if msg == ('!deanolist').lower():
        for i in deano:
            await message.channel.send(f'**{i}**')
    if msg == ('!tchapzlist').lower():
        for i in tchapz:
            await message.channel.send(f'**{i}**')
    if msg == ('!zerolist').lower():
        for i in zero:
            await message.channel.send(f'**{i}**')
    if msg == ('!doddylist').lower():
        for i in doddy:
            await message.channel.send(f'**{i}**')
    if msg == ('!bigdoglist').lower():
        for i in bigdog:
            await message.channel.send(f'**{i}**')

    # check daily donut count for users
    if msg == ('!newbd').lower():
        for x in (newb):
            count += 1
        await message.channel.send(f'{count}')
    if msg == ('!deanod').lower():
        for x in (deano):
            count += 1
        await message.channel.send(f'{count}')
    if msg == ('!zerod').lower():
        for x in (zero):
            count += 1
        await message.channel.send(f'{count}')
    if msg == ('!camod').lower():
        for x in (camo):
            count += 1
        await message.channel.send(f'{count}')
    if msg == ('!doddyd').lower():
        for x in (newb):
            count += 1
        await message.channel.send(f'{count}')
    if msg == ('!tchapzd').lower():
        for x in (tchapz):
            count += 1
        await message.channel.send(f'{count}')
    if msg == ('!dahad').lower():
        for x in (daha):
            count += 1
        await message.channel.send(f'{count}')
    if msg == ('!bigdogd').lower():
        for x in (bigdog):
            count += 1
        await message.channel.send(f'{count}')

    # clear donut for user
    if msg == ('!newbc').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'BOT Police':
                await message.channel.send('Access Granted!')
                newb.clear()
                count = 0
                await message.channel.send(f'Now has {count} donut(s)!')
    if msg == ('!deanoc').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'BOT Police':
                await message.channel.send('Access Granted!')
                deano.clear()
                count = 0
                await message.channel.send(f'Now has {count} donut(s)!')
    if msg == ('!tchapzc').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'BOT Police':
                await message.channel.send('Access Granted!')
                tchapz.clear()
                count = 0
                await message.channel.send(f'Now has {count} donut(s)!')
    if msg == ('!camoc').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'BOT Police':
                await message.channel.send('Access Granted!')
                camo.clear()
                count = 0
                await message.channel.send(f'Now has {count} donut(s)!')
    if msg == ('!zeroc').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'BOT Police':
                await message.channel.send('Access Granted!')
                zero.clear()
                count = 0
                await message.channel.send(f'Now has {count} donut(s)!')
    if msg == ('!doddyc').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'BOT Police':
                await message.channel.send('Access Granted!')
                doddy.clear()
                count = 0
                await message.channel.send(f'Now has {count} donut(s)!')
    if msg == ('!bigdogc').lower():
        author = message.author.roles
        for i in author:
            if i.name == 'BOT Police':
                await message.channel.send('Access Granted!')
                bigdog.clear()
                count = 0
                await message.channel.send(f'Now has {count} donut(s)!')

    # returns current time
    if msg == ('!time'):
        await message.channel.send(f'The current time is: {current_time}')

    # reset donut at midnight


    # Leaderboard
    if msg == ('!lb').lower():
        await message.channel.send(f'**-------Leaderboard--------**')
        for i in leaderboard:
            await message.channel.send(f'{i}      :             {leaderboard[i]}')

    # shows username
    if msg == ('!pn').lower():
        author = message.author
        await message.channel.send(author.name)

    # List of commands
    if msg == ('!coms').lower():
        await message.channel.send(f'**#########################################**  \n'
                                   f'**############## List Of Commands ###############** \n'
                                   f'**#########################################**  \n'
                                   f'**!lb** = leaderboard \n'
                                   f'**!time** = Show current time \n'
                                   f'**!coms** = List of commands\n'
                                   f'**![name of the user]** = to give them a donut (people with the No perms role cannot use this command)\n'
                                   f'**!pn** = print name \n'
                                   f'**![name of the user - c.. eg deanoc, newbc]** =  to clear users donut (Roles specific)\n'
                                   f'**!donut** = to see a random donut \n'
                                   f'**![name of the user -d.. eg deanod, newbd]** = to check users daily donut \n'
                                   f'**![name of the user - list.. eg newblist, deanolist, camolist]** = to see the list of donut owned by users \n'
                                   f'**!names** = to view names of people applicable to receive donuts \n'
                                   f'**!whois** = should give the details of user @ with this command (under construction.. working progress)\n'
                                   f'**!refer** = to refer to pinned images\n' 
                                   f'**!mm** = to mute your mic \n'
                                   f'**!toc** = that old chestnut \n'
                                   f'**!dk** = Donut King \n'
                                   f'**!whoasked** = Who asked\n'
                                   f'**!waffle** = Waffle\n'
                                   f'**!gdonut** = Give donuts to someone \n'
                                   f'**!contract** = Show contracts\n'
                                   )
@client.command(name="whois")
async def whois(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=user.color, timestamp=ctx.message.created_at)
    embed.set_author(nam=f'user info - {user}'),
    embed.set_thumbnail(url=user.avatar),
    embed.set_footer(text=f'Requested by - {ctx.author}',
                     icon_url=ctx.avatar_url)
    embed.add_field(name='ID', value=user.id, inline=False)
    embed.add_field(name='Name', value=user.display_name, inline=False)
    embed.add_field(name='Joined at', value=user.joined_at, inline=False)
    embed.add_field(name='Bot?', value=user.bot, inline=False)

    await ctx.send(embed=embed)


# functions

# start client
client.run(token)
