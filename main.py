import discord
from discord import Embed, Color
import random

import BLACKLIST
import SECRETS

client = discord.Client()
developer = SECRETS.DEVID
admin = SECRETS.ADMINID

@client.event
async def on_ready():
    print("==============================================================================================")
    print("                                          MAIN                                                ")
    print("==============================================================================================")
    print("Eingeloggr als: " + client.user.name + "                                                      ")
    print("==============================================================================================")
    print("Client ID: " + SECRETS.CLIENTID + "                                                           ")
    print("Token: " + SECRETS.TOKEN + "                                                                  ")
    print("==============================================================================================")
    print('          _________ _______          _________ _______  _______    ______   _______ _________ ')
    print(' |\     /|\__   __/(  ____ \|\     /|\__   __/(  ____ \(  ____ )  (  ___ \ (  ___  )\__   __/ ')
    print(' | )   ( |   ) (   | (    \/| )   ( |   ) (   | (    \/| (    )|  | (   ) )| (   ) |   ) (    ')
    print(' | (___) |   | |   | |      | (___) |   | |   | (__    | (____)|  | (__/ / | |   | |   | |    ')
    print(' |  ___  |   | |   | | ____ |  ___  |   | |   |  __)   |     __)  |  __ (  | |   | |   | |    ')
    print(' | (   ) |   | |   | | \_  )| (   ) |   | |   | (      | (\ (     | (  \ \ | |   | |   | |    ')
    print(' | )   ( |___) (___| (___) || )   ( |   | |   | (____/\| ) \ \__  | )___) )| (___) |   | |    ')
    print(' |/     \|\_______/(_______)|/     \|   )_(   (_______/|/   \__/  |/ \___/ (_______)   )_(    ')
    print('                                                                                              ')
    print('                                       __      ______                                         ')
    print('                                      /  |    / __   |                                        ')
    print('                               _   _ /_/ |   | | //| |                                        ')
    print('                              | | | |  | |   | |// | |                                        ')
    print('                               \ V /   | | _ |  /__| |                                        ')
    print('                                \_/    |_|(_) \_____/                                         ')
    print('                                                                                              ')
    print('==============================================================================================')
    print('                                                                                              ')
    print('                                Developed by HighterLAB                                       ')
    print('                            Copyright by https://highter.de                                   ')
    print('                                                                                              ')
    print('==============================================================================================')
    print('Bot is logged in successfully! Running on servers:\n                                          ')
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id)                                                              )
    print('==============================================================================================')
    print('                                       CONSOLE                                                ')
    print('                                                                                              ')
    await client.change_presence(game=discord.Game(name=SECRETS.GAME, type=2, url="https://highter.de"))


@client.event
async def on_message(message):
    warning = discord.Embed(
        title=":warning: KEINE BERECHTIGUNG",
        color=Color.red(),
        description="Tut uns leid aber du hast keine berechtigung den Befehl `" + message.content + "` auszuführen!"
    )

    if message.author.id in developer:
        if message.content.lower().startswith(SECRETS.PREFIX + 'game'):
            if message.author.id in developer:
                game = message.content[7:]
                await client.change_presence(game=discord.Game(name=game, type=2, url="https://highter.de"))
                await client.send_message(message.channel, "Ich habe meinen Status zu `" + message.content[7:] + "` geändert!")
                print(">> The developer {0} changed the game to {1} [{2}]".format(message.author, message.content[7:], message.id))
            else:
                await client.send_message(message.channel, embed=warning)
                print(">> User {0} try´s to use the command {1} but he has no permissions, WARNING! [{2}]".format(message.author, message.content, message.id))

        if message.author.id in admin:
            if message.content.lower().startswith(SECRETS.PREFIX + "log"):
                log = message.content[6:]
                await client.send_message(message.channel, log)
                print("Admin {0} added a log: {1}".format(message.author, log))

        if message.content.lower().startswith(SECRETS.PREFIX + 'ping'):
            if message.author.id in developer:
                embed = discord.Embed(
                    title= ":chart_with_upwards_trend: PING",
                    color=0xe67e22,
                    description="This is the Ping:",
                )
                await client.send_message(message.channel, embed=embed)
            else:
                await client.send_message(message.channel, embed=warning)
                print(">> User {0} try´s to use the command {1} but he has no permissions, WARNING! [{2}]".format(message.author, message.content, message.id))

        if message.content.lower().startswith(SECRETS.PREFIX + 'invite'):
            embed = discord.Embed(
                title="Hier der Link um den Bot einzuladen :wink:\n\n",
                color=Color.green(),
                description="`" + SECRETS.INVITE + "`",
            )
            embed.set_author(
                name="Highter Music - Invite Link",
                icon_url=SECRETS.ICON,
                url=SECRETS.URL,
            )
            await client.send_message(message.channel, embed=embed)
            print(">> User {0} asked for a invite link! [{1}]".format(message.author, message.id))

        if message.content.lower().startswith(SECRETS.PREFIX + 'help'):
            if message.content[7:] == "highter":
                embed = discord.Embed(
                    title=":boom: **Was ist Highter?**\n",
                    color=Color.green(),
                    description="Highter ist kostenloser online Musik streaming Dienst welcher dir ermöglicht, Millionen von Songs ohne Werbeunterbrechung abzuspielen. "
                                "Highter sowie HighterFM.club gehören zur Gorded Group Ltd."
                )
                embed.set_author(
                    name="Highter Music - Was ist Highter?",
                    icon_url=SECRETS.ICON,
                    url=SECRETS.URL,
                )
                await client.send_message(message.channel, embed=embed)
                print(">> User {0} used the command {1} [{2}]".format(message.author, message.content, message.id))

            if message.content[2:] == 'help':
                embed = discord.Embed(
                    title=":boom: **This is HighterBot v1.0!**\n",
                    color=0x2ecc71,
                    description="__**Hier ein paar Funktionen zum HighterBot**__\n\n"
                                "- Bitte benutze `h!help` wenn du Hilfe brauchst oder wende dich an einem Admin.\n"
                                "- Benutze `h!coin` um mit dem Coinflipper spielen zu können.\n"
                                "- Mit `h!uptime` erfährst du wie lange der Bot schon online ist.\n"
                                "- Über `h!joke` erzählt dir HighterBot verschiede Arten von Witzen.\n"
                                "- Mit `h!invite` erhälst du den InviteLink um HighterBot auf deinem Server einzuladen.\n"
                                "- Mit schreiben erhältst du pro Kommentar 2 XP Punkte.\n\n"
                                "__**NEW! :tada: **__\n\n"
                                "- Mit deinen XP´s kannst du auf verschiedenen Leveln aufsteigen!\n"
                                "- Du erfährst mit `h!xp` und `h!level` deinen Stand.\n"
                                "- Über den Command `h!user [SPIELER]` erfährst du alles über den eingetragenen Spieler!\n"
                )
                embed.set_author(
                    name="Highter Music - Help",
                    icon_url=SECRETS.ICON,
                    url=SECRETS.URL,
                )
                embed.add_field(
                    name=":keyboard: __**Commands:**__\n\n",
                    value="`1` **!help**\n"
                          "`2` **!coin**\n"
                          "`3` **!uptime**\n"
                          "`4` **!joke**\n"
                          "`5` **!invite**\n"
                          "`6` **!xp**\n"
                          "`7` **!level**\n"
                          "`8` **!user [SPIELER]**\n"
                )
                await client.send_message(message.channel, embed=embed)
                print(">> User {0} used the command {1} [{2}]".format(message.author, message.content, message.id))
            else:
                return 0

        if message.content.lower().startswith(SECRETS.PREFIX + 'user'):
            if message.author.id in developer:
                try:
                    user = message.mentions[0]
                    userjoinedat = str(user.joined_at).split('.', 1)[0]
                    usercreatedat = str(user.created_at).split('.', 1)[0]

                    userembed = discord.Embed(
                        title="__Username:__",
                        description=user.name,
                        color=0xe67e22
                    )
                    userembed.set_author(
                        name="User Info:"
                    )
                    userembed.add_field(
                        name="__Joined at:__",
                        value=userjoinedat
                    )
                    userembed.add_field(
                        name="__User created at:__",
                        value=usercreatedat
                    )
                    userembed.add_field(
                        name="__Discrimintor:__",
                        value="`" + user.name + "#`" + user.discriminator
                    )
                    userembed.add_field(
                        name="__User ID:__",
                        value=user.id
                    )

                    print(">> User {0} was searched from {1} [{2}]".format(user.name, message.author, message.id))
                    await client.send_message(message.channel, embed=userembed)
                except IndexError:
                    await client.send_message(message.channel, "Ich konnte den User nicht finden!")
                    print(">> {0} tries to find {1} but there was no result. [{2}}".format(message.author, message.content, message.id))

        if message.content.lower().startswith(SECRETS.PREFIX + 'joke'):
            choice = random.randint(1, 4)  # choose a number from 1 - 4
            title = "Ich erzähl mal einen Witz :smile:"  # the title for the embed messages
            if choice == 1:
                await client.send_message(message.channel, embed=Embed(color=Color.red(), title=title,
                                                                       description="Zahnarzt zum Patienten: „Das kann jetzt ein bisschen weh tun.“\n\n"
                                                                                   "Patient: „Kein Problem“\n\n"
                                                                                   "Zahnarzt: „Ich habe seit 3 Jahren ein Verhältnis mit Ihrer Frau.“"))
            if choice == 2:
                await client.send_message(message.channel, embed=Embed(color=Color.red(), title=title,
                                                                       description="Was machen zwei wütende Schafe?\n\n"
                                                                                   "Sie kriegen sich in die Wolle."))
            if choice == 3:
                await client.send_message(message.channel, embed=Embed(color=Color.red(), title=title,
                                                                       description="Vater: „Sohn, ich habe all dein Spielzeug dem Kinderheim gespendet.“\n\n"
                                                                                   "Sohn: „Warum hast du das gemacht?“\n\n"
                                                                                   "Vater: „Damit es dir dort nicht zu langweilig wird.“"))
            if choice == 4:
                await client.send_message(message.channel, embed=Embed(color=Color.red(), title=title,
                                                                       description="Im Gefängnis zur After-Party zu gehen, war nicht die allerbeste Idee."))
            print(">> User {0} used the command {1} [{2}]".format(message.author, message.content, message.id))

        if message.content.lower().startswith(SECRETS.PREFIX + 'coin'):
            choice = random.randint(1, 2)  # choose a number from 1 - 2
            if choice == 1:
                await client.send_message(message.channel, '🌑')
            if choice == 2:
                await client.send_message(message.channel, '🌕')
            print(">> User {0} used the command {1} [{2}]".format(message.author, message.content, message.id))


@client.event
async def on_message(message):
    if BLACKLIST.WORDS in message.content.lower():
        await client.send_message(message.channel, "VERWARNUNG")


client.run(SECRETS.TOKEN)