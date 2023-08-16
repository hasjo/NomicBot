import os
import discord
import json
import rules
from discord.ext import commands
from discord import Client

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
datafile = 'data.json'
if os.path.isfile(datafile):
    with open(datafile) as readfile:
        datadict = json.loads(readfile.read())
else:
    datadict = {"playernumber": 1}

def save_dict():
    with open(datafile, 'w') as writefile:
        writefile.write(json.dumps(datadict, sort_keys=True, indent=4))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def debug(ctx):
    print(datadict)
    save_dict()
    await ctx.message.delete()

@bot.command()
async def initguild(ctx):
    guildid = ctx.guild.id
    datadict['guildid'] = guildid
    save_dict()
    await ctx.message.delete()

@bot.command()
async def initrules(ctx):
    channelid = ctx.channel.id
    datadict['ruleschannel'] = channelid
    print(f"CHANNEL ID: {channelid}")
    await ctx.message.delete()
    for rule in rules.base_rules:
        ruledict = rules.base_rules[rule]
        ruletext = ruledict["text"]
        sendembed = discord.Embed(title=rule)
        sendembed.add_field(name="Text", value=ruledict["text"], inline=True)
        sendembed.add_field(name="Mutable", value=ruledict["mutable"], inline=False)
        messageid = await ctx.send(embed=sendembed)
        if 'rules' not in datadict:
            datadict['rules'] = {}
        if rule not in datadict['rules']:
            datadict['rules'][rule] = {}
        datadict['rules'][rule]["messageid"] = messageid.id
        datadict['nextrule'] = 301
        print(messageid)
    save_dict()

@bot.command()
async def initproposal(ctx):
    channelid=ctx.channel.id
    datadict['proposalchannel'] = channelid
    await ctx.message.delete()
    print(f"CHANNEL ID: {channelid}")
    save_dict()

@bot.command()
async def initmoney(ctx):
    channelid=ctx.channel.id
    datadict['moneychannel'] = channelid
    datadict['money'] = {}
    await ctx.message.delete()
    print(f"CHANNEL ID: {channelid}")
    save_dict()

@bot.command()
async def initcontrol(ctx):
    channelid=ctx.channel.id
    datadict['controlchannel'] = channelid
    await ctx.message.delete()
    print(f"CHANNEL ID: {channelid}")
    save_dict()

@bot.command()
async def initdeny(ctx):
    channelid=ctx.channel.id
    datadict['denychannel'] = channelid
    await ctx.message.delete()
    print(f"CHANNEL ID: {channelid}")
    save_dict()

@bot.command()
async def initlog(ctx):
    channelid=ctx.channel.id
    datadict['logchannel'] = channelid
    await ctx.message.delete()
    print(f"CHANNEL ID: {channelid}")
    save_dict()

@bot.command()
async def initplayers(ctx):
    channelid=ctx.channel.id
    datadict['playerchannel'] = channelid
    await ctx.message.delete()
    print(f"CHANNEL ID: {channelid}")
    save_dict()

@bot.command()
async def initinfo(ctx):
    msg1 = '''
What you're looking at:

This is the section for a game called Nomic. It is a game about legislation. Playing the game is making, amending, or repealing laws - or in this case, rules.
    '''
    msg2 = '''
CHANNELS:

I have organized this game over a bunch of channels to keep things organized, here's what they are for.

#rules - THE RULES OF THE GAME - This is where the rules of the game live.
#log - Action log - this tracks actions performed. If you're interested in what has happened, look here.
#proposal - Rules Proposals - When it's your turn, make the proposal here
#control - Where the game runner controls the game
#repeal-deny - Repealed and denied rules end up here
#players - The list of players in the game
#chat - Where to discuss the proposals and votes and such
#points - Where points are logged
    '''
    msg3 = '''
TO JOIN THE GAME:

type "$join" in the chat channel, you will get two pings, one in the log and the other in the players channel.

WHEN IT'S YOUR TURN TO PROPOSE:

to make a proposal, the command structure is as follows:

"$propose [new, amend, repeal, trasmute] <CONTENT>"

The content changes based on which action you choose,

DO NOT INCLUDE THE <> IN THE PROPOSAL MESSAGE, THEY JUST INDICATE VARIABLE TEXT

- NEW - "$propose new <RULE TEXT>"

- AMEND - "$propose amend <OLD RULE NUMBER> <NEW VERBATIM TEXT>"

- REPEAL - "$propose repeal <RULE NUMBER>"

- TRANSMUTE - "$propose transmute <RULE NUMBER>"
    '''
    msg4 = '''
TO EDIT A PROPOSAL:

If you made a proposal of a new rule or an amendment and you need to make a change to the wording of the rule, if you are the user who proposed the change, just type

"$edit <NEW CONTENT>" where new content is the new text you want the proposal to be

VOTING:

Every proposal will have a check mark for yes and an X for no. Vote by clicking the appropriate reaction. If voting gets weird, votes will be counted by other means as necessary. When the appropriate number of people have voted, the proposal will be approved or denied by the game runner based on the result of the vote.

WHAT IS THE OBJECTIVE:

To win the game. Have fun!

TO LEAVE THE GAME:

type "$leave" in a channel, and you will be removed from the game
    '''
    await ctx.send(msg1)
    await ctx.send(msg2)
    await ctx.send(msg3)
    await ctx.send(msg4)
    await ctx.message.delete()

@bot.command()
async def usertest(ctx):
    await ctx.send(ctx.author.mention)
    print(ctx.author.display_name)

@bot.command()
async def initrole(ctx):
    role_id = ctx.message.role_mentions[0].id
    datadict['gamerole'] = role_id
    print(role_id)
    save_dict()

@bot.command()
async def gimme(ctx):
    role_id = datadict['gamerole']
    game_role = ctx.guild.get_role(role_id)
    if not ctx.author.get_role(role_id):
        await ctx.author.add_roles(game_role)

@bot.command()
async def moneyname(ctx):
    if ctx.channel.id == datadict['controlchannel']:
        message = ctx.message.content
        cmd, name = message.split(' ', 1)
        datadict['money']['name'] = name
        save_dict()

@bot.command()
async def mint(ctx):
    if ctx.channel.id == datadict['controlchannel']:
        message = ctx.message.content
        cmd, target, amount = message.split(' ', 2)
        amount = int(amount)
        mentioned = ctx.message.mentions[0]
        player_id = str(mentioned.id)
        log_channel = datadict['logchannel']
        logchannelobj = await ctx.guild.fetch_channel(log_channel)
        money_channel = datadict['moneychannel']
        moneychannelobj = await ctx.guild.fetch_channel(money_channel)
        moneyname = datadict['money']['name']
        if player_id not in datadict['money']:
            datadict['money'][player_id] = {}
            datadict['money'][player_id]['money'] = amount
            moneymsg = await moneychannelobj.send(f"{mentioned.mention} - {amount} {moneyname}(s)")
            datadict['money'][player_id]['messageid'] = moneymsg.id
        else:
            datadict['money'][player_id]['money'] += amount
            moneycount = datadict['money'][player_id]['money']
            moneymsg = datadict['money'][player_id]['messageid']
            playermsg = await moneychannelobj.fetch_message(moneymsg)
            await playermsg.edit(content=f"{mentioned.mention} - {moneycount} {moneyname}(s)")
        await logchannelobj.send(f"{mentioned.mention} has received {amount} NEW {moneyname}(s)")
        save_dict()

@bot.command()
async def give(ctx):
    message = ctx.message.content
    cmd, target, amount = message.split(' ', 2)
    amount = int(amount)
    mentioned = ctx.message.mentions[0]
    senderobj = ctx.message.author
    sender_id = str(senderobj.id)
    recipient_id = str(mentioned.id)
    log_channel = datadict['logchannel']
    logchannelobj = await ctx.guild.fetch_channel(log_channel)
    money_channel = datadict['moneychannel']
    moneychannelobj = await ctx.guild.fetch_channel(money_channel)
    moneyname = datadict['money']['name']
    sendertotal = datadict['money'][sender_id]['money']
    if amount > sendertotal:
        await ctx.send(f"YOU DONT HAVE ENOUGH {moneyname}s YA GOOFBALL")
    else:
        datadict['money'][recipient_id]['money'] += amount
        datadict['money'][sender_id]['money'] -= amount
        recipient_money = datadict['money'][recipient_id]['money']
        sender_money = datadict['money'][sender_id]['money']
        recipient_msg_id = datadict['money'][recipient_id]['messageid']
        sender_msg_id = datadict['money'][sender_id]['messageid']
        recipientmsg = await moneychannelobj.fetch_message(recipient_msg_id)
        await recipientmsg.edit(content=f"{mentioned.mention} - {recipient_money} {moneyname}(s)")
        sendermsg = await moneychannelobj.fetch_message(sender_msg_id)
        await sendermsg.edit(content=f"{senderobj.mention} - {sender_money} {moneyname}(s)")

        await logchannelobj.send(f"{senderobj.mention} has sent {amount} {moneyname}(s) to {mentioned.mention}")
        save_dict()
        

@bot.command()
async def yes(ctx):
    if datadict['activeproposal']:
        if 'votes' not in datadict:
            datadict['votes'] = {}
            datadict['votes']['yes'] = 0
            datadict['votes']['no'] = 0
        auth_id = str(ctx.author.id)
        if 'players' not in datadict['votes']:
            datadict['votes']['players'] = {}
        if auth_id in datadict['votes']['players']:
            prev_vote = datadict['votes']['players'][auth_id]
            datadict['votes'][prev_vote] = datadict['votes'][prev_vote] - 1
        datadict['votes']['players'][auth_id] = "yes"
        datadict['votes']['yes'] = datadict['votes']['yes'] + 1
        guild_id = datadict['guildid']
        guild_obj = bot.get_guild(guild_id)
        log_channel = datadict['logchannel']
        logchannelobj = await guild_obj.fetch_channel(log_channel)
        save_dict()
        await logchannelobj.send(f"A PLAYER HAS VOTED")
    else:
        await ctx.send("There is no active proposal")

@bot.command()
async def no(ctx):
    if datadict['activeproposal']:
        if 'votes' not in datadict:
            datadict['votes'] = {}
            datadict['votes']['yes'] = 0
            datadict['votes']['no'] = 0
        auth_id = str(ctx.author.id)
        if 'players' not in datadict['votes']:
            datadict['votes']['players'] = {}
        if auth_id in datadict['votes']['players']:
            prev_vote = datadict['votes']['players'][auth_id]
            datadict['votes'][prev_vote] = datadict['votes'][prev_vote] - 1
        datadict['votes']['players'][auth_id] = "no"
        datadict['votes']['no'] = datadict['votes']['no'] + 1
        guild_id = datadict['guildid']
        guild_obj = bot.get_guild(guild_id)
        log_channel = datadict['logchannel']
        logchannelobj = await guild_obj.fetch_channel(log_channel)
        save_dict()
        await logchannelobj.send(f"A PLAYER HAS VOTED")
    else:
        await ctx.send("There is no active proposal")

@bot.command()
async def join(ctx):
    player_channel = datadict['playerchannel']
    playerchannelobj = await ctx.guild.fetch_channel(player_channel)
    log_channel = datadict['logchannel']
    logchannelobj = await ctx.guild.fetch_channel(log_channel)
    await logchannelobj.send(f"{ctx.author.mention} HAS JOINED THE GAME")
    playernumber = datadict['playernumber']
    playermsg = await playerchannelobj.send(f"{ctx.author.mention} - {playernumber}")
    datadict['playernumber'] = playernumber + 1
    if 'players' not in datadict:
        datadict['players'] = {}
    auth_id = str(ctx.author.id)
    if auth_id not in datadict['players']:
        datadict['players'][auth_id] = {}
    datadict['players'][auth_id]['messageid'] = playermsg.id
    role_id = datadict['gamerole']
    game_role = ctx.guild.get_role(role_id)
    if not ctx.author.get_role(role_id):
        await ctx.author.add_roles(game_role)
    print(ctx.author.display_name)
    save_dict()
    await ctx.message.delete()

@bot.command()
async def leave(ctx):
    author_id = str(ctx.author.id)
    player_message_id = datadict['players'][author_id]['messageid']
    role_id = datadict['gamerole']
    game_role = ctx.guild.get_role(role_id)
    log_channel = datadict['logchannel']
    logchannelobj = await ctx.guild.fetch_channel(log_channel)
    await logchannelobj.send(f"{ctx.author.mention} HAS LEFT THE GAME")
    if ctx.author.get_role(role_id):
        await ctx.author.remove_roles(game_role)
    player_channel = datadict['playerchannel']
    playerchannelobj = await ctx.guild.fetch_channel(player_channel)
    player_message = await playerchannelobj.fetch_message(player_message_id)
    await player_message.delete()
    await ctx.message.delete()

@bot.command()
async def propose(ctx):
    message = ctx.message.content
    if 'activeproposal' in datadict and 'messageid' in datadict['activeproposal']:
        await ctx.send("There is already an active proposal")
        return True
    try:
        cmd, action, content = message.split(' ', 2)
    except ValueError:
        await ctx.send("improperly formatted message, try $propose [new, amend, repeal, transmute] <content>")
        return True
    print(f"{action} - {content}")
    log_channel = datadict['logchannel']
    logchannelobj = await ctx.guild.fetch_channel(log_channel)
    newrulenum = datadict['nextrule']
    oldcontent = None

    if action == 'new':
        title = f"new - {newrulenum}"
        mention_obj = ctx.author.mention
        await logchannelobj.send(f"{newrulenum} - {mention_obj} - has proposed new rule {newrulenum}")
    elif action == 'amend':
        target, content = content.split(' ', 1)
        title = f"amendment - {target} -> {datadict['nextrule']}"
        rules_channel = datadict['ruleschannel']
        ruleschannelobj = await ctx.guild.fetch_channel(rules_channel)
        target_rule = await ruleschannelobj.fetch_message(datadict['rules'][target]['messageid'])
        mention_obj = ctx.author.mention
        oldcontent = target_rule.embeds[0].fields[0].value
        await logchannelobj.send(f"{newrulenum} - {mention_obj} - has proposed an amendment to {target} ")
    elif action == 'repeal':
        target = content
        title = f"repeal - {target} -> {newrulenum}"
        rules_channel = datadict['ruleschannel']
        ruleschannelobj = await ctx.guild.fetch_channel(rules_channel)
        target_rule = await ruleschannelobj.fetch_message(datadict['rules'][target]['messageid'])
        content = target_rule.embeds[0].fields[0].value
        mention_obj = ctx.author.mention
        await logchannelobj.send(f"{newrulenum} - {mention_obj} - has proposed a repeal of rule {target}")
    elif action == 'transmute':
        target = content
        title = f"transmute - {target} -> {newrulenum}"
        rules_channel = datadict['ruleschannel']
        ruleschannelobj = await ctx.guild.fetch_channel(rules_channel)
        target_rule = await ruleschannelobj.fetch_message(datadict['rules'][target]['messageid'])
        content = target_rule.embeds[0].fields[0].value
        mutable_value = target_rule.embeds[0].fields[1].value
        if mutable_value == "False":
            mutable = False
        elif mutable_value == "True":
            mutable = True
        mention_obj = ctx.author.mention
        await logchannelobj.send(f"{newrulenum} - {mention_obj} - has proposed a transmutation of rule {target}")
    else:
        await ctx.send("improperly formatted message, try $propose [new, amend, repeal, transmute] <content>")
        return True
    datadict['nextrule'] = datadict['nextrule'] + 1
    sendembed = discord.Embed(title=title)
    sendembed.add_field(name="Text", value=content, inline=True)
    if action == 'amend':
        sendembed.add_field(name="Old Text", value=oldcontent, inline=False)
    if action == 'transmute':
        MutableString = str(not mutable)
        sendembed.add_field(name="Mutable", value=MutableString, inline=False)
    else:
        sendembed.add_field(name="Mutable", value="True", inline=False)
    messageid = await ctx.send(embed=sendembed)
    await messageid.add_reaction("✅")
    await messageid.add_reaction("❌")
    if 'activeproposal' not in datadict:
        datadict['activeproposal'] = {}
    datadict['activeproposal']['messageid'] = messageid.id
    datadict['activeproposal']['userid'] = ctx.author.id
    save_dict()

@bot.command()
async def edit(ctx):
    if datadict['activeproposal']:
        if ctx.author.id == datadict['activeproposal']['userid']:
            message = ctx.message.content
            cmd, content = message.split(' ', 1)
            active_proposal = datadict['activeproposal']['messageid']
            log_channel = datadict['logchannel']
            logchannelobj = await ctx.guild.fetch_channel(log_channel)
            proposal_channel = datadict['proposalchannel']
            proposechannelobj = await ctx.guild.fetch_channel(proposal_channel)
            proposal_message = await proposechannelobj.fetch_message(active_proposal)
            mod_embed = proposal_message.embeds[0]
            if mod_embed.title.startswith("amendment"):
                current_text = mod_embed.fields[0].value
                old_text = mod_embed.fields[1].value
                mod_embed.clear_fields()
                mod_embed.add_field(name="Text", value=content, inline=True)
                mod_embed.add_field(name="Old Text", value=old_text, inline=False)
                mod_embed.add_field(name="Mutable", value="True", inline=False)
            else:
                current_text = mod_embed.fields[0].value
                mod_embed.clear_fields()
                mod_embed.add_field(name="Text", value=content, inline=True)
                mod_embed.add_field(name="Mutable", value="True", inline=False)
            await proposal_message.edit(embed=mod_embed)
            log_message = f"Current proposal has been edited from \"{current_text}\" to \"{content}\""
            await logchannelobj.send(f"{log_message}")

@bot.command()
async def votecount(ctx):
    if datadict['activeproposal']:
        if 'votes' in datadict:
            totalvotes = 0
            totalvotes += datadict['votes']['yes']
            totalvotes += datadict['votes']['no']
            await ctx.send(f"{totalvotes} VOTE(S) HAVE BEEN CAST")

@bot.command()
async def votes(ctx):
    if ctx.channel.id == datadict['controlchannel']:
        if 'votes' in datadict:
            if 'players' in datadict['votes']:
                message_list = []
                for player in datadict['votes']['players']:
                    print(f"PLAYER: {player}")
                    playerobj = await ctx.guild.fetch_member(player)
                    print(playerobj)
                    vote = datadict['votes']['players'][player]
                    message_list.append(f"{playerobj.mention} HAS VOTED {vote}")
                yes_votes = datadict['votes']['yes']
                no_votes = datadict['votes']['no']
                log_channel = datadict['logchannel']
                logchannelobj = await ctx.guild.fetch_channel(log_channel)
                await logchannelobj.send(f"FINAL VOTES: Yes - {yes_votes}  No - {no_votes}")
                for item in message_list:
                    await logchannelobj.send(item)

@bot.command()
async def approve(ctx):
    if datadict['activeproposal'] != {} and ctx.channel.id == datadict['controlchannel']:
        active_proposal = datadict['activeproposal']['messageid']
        proposal_channel = datadict['proposalchannel']
        rules_channel = datadict['ruleschannel']
        deny_channel = datadict['denychannel']
        log_channel = datadict['logchannel']
        logchannelobj = await ctx.guild.fetch_channel(log_channel)
        proposechannelobj = await ctx.guild.fetch_channel(proposal_channel)
        proposal_message = await proposechannelobj.fetch_message(active_proposal)
        action, rule = proposal_message.embeds[0].title.split(" - ")
        if action == 'new':
            ruleschannelobj = await ctx.guild.fetch_channel(rules_channel)
            print(rule)
            proposal_message.embeds[0].title = proposal_message.embeds[0].title.split(' - ')[1]
            newmessage = await ruleschannelobj.send(embed=proposal_message.embeds[0])
            if rule not in datadict['rules']:
                datadict['rules'][rule] = {}
            datadict['rules'][rule]["messageid"] = newmessage.id
        elif action == 'amendment':
            ruleschannelobj = await ctx.guild.fetch_channel(rules_channel)
            oldrule, newrule = rule.split(" -> ")
            print(oldrule, newrule)
            print(datadict['rules'][oldrule])
            target_rule = await ruleschannelobj.fetch_message(datadict['rules'][oldrule]['messageid'])
            mod_embed = target_rule.embeds[0]
            mod_embed.title = f"{mod_embed.title} -> {newrule}"
            mod_embed.clear_fields()
            mod_embed.add_field(name="Text", value=proposal_message.embeds[0].fields[0].value, inline=True)
            mod_embed.add_field(name="Mutable", value="True", inline=False)
            await target_rule.edit(embed=mod_embed)
            datadict['rules'][newrule] = {}
            datadict['rules'][newrule]['messageid'] = target_rule.id
        elif action == 'repeal':
            ruleschannelobj = await ctx.guild.fetch_channel(rules_channel)
            denychannelobj = await ctx.guild.fetch_channel(deny_channel)
            rule = rule.split(" -> ")[0]
            target_rule = await ruleschannelobj.fetch_message(datadict['rules'][rule]['messageid'])
            mod_embed = target_rule.embeds[0]
            mod_embed.title = f"REPEALED - {rule}"
            await denychannelobj.send(embed=mod_embed)
            await target_rule.delete()
            datadict['rules'][rule]["messageid"] = "REPEALED"
        elif action == 'transmute':
            ruleschannelobj = await ctx.guild.fetch_channel(rules_channel)
            rulenum, newrule = rule.split(" -> ")
            target_rule = await ruleschannelobj.fetch_message(datadict['rules'][rulenum]['messageid'])
            mod_embed = target_rule.embeds[0]
            mod_embed.clear_fields()
            mod_embed.title = rule
            mod_embed.add_field(name="Text", value=proposal_message.embeds[0].fields[0].value, inline=True)
            mod_embed.add_field(name="Mutable", value=proposal_message.embeds[0].fields[1].value, inline=False)
            await target_rule.edit(embed=mod_embed)
            datadict['rules'][newrule]['messageid'] = target_rule.id
            
        datadict['votes']['yes'] = 0
        datadict['votes']['no'] = 0
        datadict['votes']['players'] = {}
        datadict['activeproposal'] = {}
        currentrule = datadict['nextrule'] - 1
        await logchannelobj.send(f"Rule {currentrule} has been APPROVED!")    
        save_dict()

@bot.command()
async def deny(ctx):
    if datadict['activeproposal'] != {} and ctx.channel.id == datadict['controlchannel']:
        active_proposal = datadict['activeproposal']['messageid']
        proposal_channel = datadict['proposalchannel']
        deny_channel = datadict['denychannel']
        denychannelobj = await ctx.guild.fetch_channel(deny_channel)
        log_channel = datadict['logchannel']
        logchannelobj = await ctx.guild.fetch_channel(log_channel)
        proposechannelobj = await ctx.guild.fetch_channel(proposal_channel)
        proposal_message = await proposechannelobj.fetch_message(active_proposal)
        await denychannelobj.send(embed=proposal_message.embeds[0])
        currentrule = datadict['nextrule'] - 1
        await logchannelobj.send(f"Rule {currentrule} has been DENIED!")
        datadict['activeproposal'] = {}
        datadict['votes']['yes'] = 0
        datadict['votes']['no'] = 0
        datadict['votes']['players'] = {}
        save_dict()

@bot.command()
async def admin(ctx):
    message = ctx.message.content
    cmd, action, content = message.split(' ', 2)
    if action == "modify" and ctx.channel.id == datadict['controlchannel']:
        target, content = content.split(' ', 1)
        if target == "proposal":
            if datadict['activeproposal'] != {}:
                active_proposal = datadict['activeproposal']['messageid']
                log_channel = datadict['logchannel']
                logchannelobj = await ctx.guild.fetch_channel(log_channel)
                proposal_channel = datadict['proposalchannel']
                proposechannelobj = await ctx.guild.fetch_channel(proposal_channel)
                proposal_message = await proposechannelobj.fetch_message(active_proposal)
                mod_embed = proposal_message.embeds[0]
                if mod_embed.title.startswith("amendment"):
                    current_text = mod_embed.fields[0].value
                    old_text = mod_embed.fields[1].value
                    mod_embed.clear_fields()
                    mod_embed.add_field(name="Text", value=content, inline=True)
                    mod_embed.add_field(name="Old Text", value=old_text, inline=False)
                    mod_embed.add_field(name="Mutable", value="True", inline=False)
                elif mod_embed.title.startswith("transmute"):
                    print("dont do anything")
                    return True
                else:
                    current_text = mod_embed.fields[0].value
                    mod_embed.clear_fields()
                    mod_embed.add_field(name="Text", value=content, inline=True)
                    mod_embed.add_field(name="Mutable", value="True", inline=False)
                await proposal_message.edit(embed=mod_embed)
                log_message = f"ADMIN has modified current proposal from \"{current_text}\" to \"{content}\""
                await logchannelobj.send(f"{log_message}")
            else:
                await ctx.send("No active proposal")
        elif target == "rule":
            ruleid, content = content.split(" ", 1)
            rules_channel = datadict['ruleschannel']
            log_channel = datadict['logchannel']
            logchannelobj = await ctx.guild.fetch_channel(log_channel)
            ruleschannelobj = await ctx.guild.fetch_channel(rules_channel)
            target_rule = await ruleschannelobj.fetch_message(datadict['rules'][ruleid]['messageid'])
            mod_embed = target_rule.embeds[0]
            old_text = mod_embed.fields[0].value
            current_mutable = mod_embed.fields[1].value
            mod_embed.clear_fields()
            mod_embed.add_field(name="Text", value=content, inline=True)
            mod_embed.add_field(name="Mutable", value=current_mutable, inline=False)
            await target_rule.edit(embed=mod_embed)
            log_message = f"ADMIN has modified rule {ruleid} from \"{old_text}\" to \"{content}\""
            await logchannelobj.send(f"{log_message}")
        elif target == "transmute":
            ruleid, content = content.split(" ", 1)
            rules_channel = datadict['ruleschannel']
            log_channel = datadict['logchannel']
            logchannelobj = await ctx.guild.fetch_channel(log_channel)
            ruleschannelobj = await ctx.guild.fetch_channel(rules_channel)
            target_rule = await ruleschannelobj.fetch_message(datadict['rules'][ruleid]['messageid'])
            mod_embed = target_rule.embeds[0]
            old_text = mod_embed.fields[0].value
            current_mutable = mod_embed.fields[1].value
            mod_embed.clear_fields()
            mod_embed.add_field(name="Text", value=old_text, inline=True)
            mod_embed.add_field(name="Mutable", value=content, inline=False)
            await target_rule.edit(embed=mod_embed)
            log_message = f"ADMIN has transmuted rule {ruleid} from \"{current_mutable}\" to \"{content}\""
            await logchannelobj.send(f"{log_message}")

bot.run(os.environ['nomictoken'])
