import nextcord
from nextcord.ui import Button, View 
from nextcord.utils import get
from nextcord.ext import commands
import os
from dotenv import load_dotenv
import wikipedia
import smtplib
import datetime
import webbrowser
import youtube_dl
import humanfriendly
import time
import random
import asyncio
import asyncpraw

reddit = asyncpraw.Reddit(client_id= "rlxZ8ONX4K12gG28bslAQw",
                     client_secret = "SeclhK30B2TG7ndn7V4gRB6yQs5bmg",
                     username = "Advanced_Daikon756",
                     password = "#noobpookveduki1234",
                     user_agent = "scrbot")

intents=nextcord.Intents(messages = True, message_content=True, guilds = True, voice_states = True)
client = commands.Bot(command_prefix="!", help_command=None, intents=intents)
gameOver = True
cricket_p1 = ""
cricket_p2 = ""

@client.event
async def on_ready():
    print("Bot just landed on the server!")
    
@client.command()
async def private(ctx):
    myEmbed = nextcord.Embed(title = "YURI'S PLAYGROUND", description=f"Hello there In Private!{ctx.author}\nHow may I help you?", color=0xffff00)
    myEmbed.set_author(name="Yuri's Moderation#2333")
    await ctx.author.send(embed=myEmbed)
    
@client.command()
async def wiki(ctx, *, arg):
    mes_1 = await ctx.reply("Searching Google!")
    try:
        results = wikipedia.page(arg)
        url = results.url
        content = results.content
        await mes_1.edit(content=f"According to Yuri, {url}")
    except Exception as e:
        await mes_1.edit(content="Could not get what you were looking for!")
        
@client.command()
async def meme(ctx):
    all_subs = []
    subreddit = await reddit.subreddit("memes")
    top_red = subreddit.top("day", limit=50)
    async for top_hot in top_red:
        all_subs.append(top_hot)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    memEmbed = nextcord.Embed(title= name)
    memEmbed.set_thumbnail(url = "https://static-prod.adweek.com/wp-content/uploads/2021/06/Reddit-Avatar-Builder-Hero-1280x680.png")
    memEmbed.set_image(url = url)
    ctx_mem = await ctx.send(embed = memEmbed)
    await meme_but(ctx,ctx_mem)
        
async def meme_but(ctx,ctx_mem):
    button = Button(label="Another One!", style=nextcord.ButtonStyle.blurple, emoji="🤚")
    view = View(timeout=100)
    view.add_item(button)
    async def button_callback(interaction):
        await mem_rep(ctx,ctx_mem)
    button.callback = button_callback 
    await ctx.reply(view = view)
        
async def mem_rep(ctx,ctx_mem):
    all_subs = []
    subreddit = await reddit.subreddit("memes")
    top_red = subreddit.top("day", limit=50)
    async for top_hot in top_red:
        all_subs.append(top_hot)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    memEmbed = nextcord.Embed(title= name)
    memEmbed.set_thumbnail(url = "https://static-prod.adweek.com/wp-content/uploads/2021/06/Reddit-Avatar-Builder-Hero-1280x680.png")
    memEmbed.set_image(url = url)
    await ctx_mem.edit(embed = memEmbed)
            
@client.command()
async def help(ctx):
    help_embed = nextcord.Embed(title = "**YURI'S PLAPYGROUND**", description = "Here are the various cmds to help you out!", color=0xffff00)
    help_embed.add_field(name="**🤖COMMANDS🤖**", value=f"1.**\$private**: Opens a dm with the user. \n2.**\$wiki [subject]**: Gives Information about the concerned subject. \n3.**\$luckyroles [role_id]**: Makes a giveaway of the mentioned role if the user has suitable permissions.\n4.**\$admin [password] [channel_id] [content]**: Sends the content matter to the described channel through the bot.\n5.**\$selfrole**: Send various options available for roles in the server.\n6.**\$meme**:Gives memes from reddit.",inline = True)
    help_embed.set_author(name = "Yuri's Moderation#2333")
    await ctx.reply(embed = help_embed)
            
@client.command()
async def cricket(ctx, p1:nextcord.Member, p2:nextcord.Member):
    global gameOver
    if gameOver:
        global cricket_p1
        global cricket_p2
        global runs1
        global runs2
        global wicket1
        global score1
        global balls1        
        global cricketp1_but
        global cricketp2_but
        global target
        global ingl
        global score_msg
        cricket_p1 = p1
        cricket_p2 = p2
        gameOver = False
        ingl = False
        runs1 = ""
        runs2 = ""
        score1 = 0
        score2 = 0
        target = 0
        wicket1 = 0
        wicket2 = 0
        balls1 = 0
        balls2 = 0
        toss = random.randint(1,2)
        if toss==1:
            cricket_p1 = p1
            cricket_p2 = p2
        else:
            cricket_p1 = p2
            cricket_p2 = p1
        wel_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} goes against {cricket_p2.mention} in Cricket!🏏", color = 0xffff00)
        wel_emb.add_field(name="RULES AND REGULATIONS", value=f"1.**{cricket_p1}** will bat first.\n2.**{cricket_p2.mention}** will ball now.\n3.Don't cry for cheating!Accept your own luck!")
        wel_emb.set_thumbnail(url = "https://www.ballebaazi.com/blog/wp-content/uploads/2019/02/wc-history-e1550046374686.jpg")
        await ctx.send(embed = wel_emb)
        view = player1()
        cricketp1_but = await ctx.send(f"For **{cricket_p1}**!",view = view)
        score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} ⚔ {cricket_p2.mention}", color=0xffff00)
        score_emb.add_field(name="SCORECARD📟", value=f"{score1}/{wicket1} ({balls1} balls) \nCurrent Run Rate:0 \t Predicted Score:0")
        score_emb.set_thumbnail(url = cricket_p1.display_avatar)
        score_msg = await ctx.send(embed = score_emb)
        view = player2()
        cricketp2_but = await ctx.send(f"For **{cricket_p2}**!",view = view)
        await time(ctx)
        
async def time(ctx):
    global balls1
    balls1+=1
    await asyncio.sleep(7)
    await match(ctx)
    
class player1(View):
    @nextcord.ui.button(label="One", style=nextcord.ButtonStyle.green, emoji="1️⃣", custom_id="run_1")
    async def one_button_callback(self, button, interaction):
        global cricket_p1
        global runs1
        global score1
        if interaction.user == cricket_p1:
            runs1 = "One"
            score1+=1
            buttons = [x for x in self.children]
            for v in buttons:
                v.disabled = True
            await interaction.response.edit_message(view = self)
            
    @nextcord.ui.button(label="Two", style=nextcord.ButtonStyle.green, emoji="2️⃣", custom_id="run_2")
    async def Two_button_callback(self, button, interaction):
        global cricket_p1
        global runs1
        global score1
        if interaction.user == cricket_p1:
            runs1 = "Two"
            score1+=2
            buttons = [x for x in self.children]
            for v in buttons:
                v.disabled = True
            await interaction.response.edit_message(view = self)
            
    @nextcord.ui.button(label="Three", style=nextcord.ButtonStyle.blurple, emoji="3️⃣", custom_id="run_3")
    async def Three_button_callback(self, button, interaction):
        global cricket_p1
        global runs1
        global score1
        if interaction.user == cricket_p1:
            runs1 = "Three"
            score1+=3
            buttons = [x for x in self.children]
            for v in buttons:
                v.disabled = True
            await interaction.response.edit_message(view = self)
            
    @nextcord.ui.button(label="Four", style=nextcord.ButtonStyle.blurple, emoji="4️⃣", custom_id="run_4")
    async def Four_button_callback(self, button, interaction):
        global cricket_p1
        global runs1
        global score1
        if interaction.user == cricket_p1:
            runs1 = "Four"
            score1+=4
            buttons = [x for x in self.children]
            for v in buttons:
                v.disabled = True
            await interaction.response.edit_message(view = self)
     
    @nextcord.ui.button(label="Six", style=nextcord.ButtonStyle.danger, emoji="6️⃣", custom_id="run_6")
    async def Six_button_callback(self, button, interaction):
        global cricket_p1
        global runs1
        global score1
        if interaction.user == cricket_p1:
            runs1 = "Six"
            score1+=6
            buttons = [x for x in self.children]
            for v in buttons:
                v.disabled = True
            await interaction.response.edit_message(view = self)

class player2(View):
    @nextcord.ui.button(label="One", style=nextcord.ButtonStyle.green, emoji="1️⃣", custom_id="run_1")
    async def one_button_callback(self, button, interaction):
        global cricket_p2
        global runs2
        if interaction.user == cricket_p2:
            runs2 = "One"
            buttons = [x for x in self.children]
            for v in buttons:
                v.disabled = True
            await interaction.response.edit_message(view = self)
            
    @nextcord.ui.button(label="Two", style=nextcord.ButtonStyle.green, emoji="2️⃣", custom_id="run_2")
    async def Two_button_callback(self, button, interaction):
        global cricket_p2
        global runs2
        if interaction.user == cricket_p2:
            runs2 = "Two"
            buttons = [x for x in self.children]
            for v in buttons:
                v.disabled = True
            await interaction.response.edit_message(view = self)
            
    @nextcord.ui.button(label="Three", style=nextcord.ButtonStyle.blurple, emoji="3️⃣", custom_id="run_3")
    async def Three_button_callback(self, button, interaction):
        global cricket_p2
        global runs2
        if interaction.user == cricket_p2:
            runs2 = "Three"
            buttons = [x for x in self.children]
            for v in buttons:
                v.disabled = True
            await interaction.response.edit_message(view = self)
            
    @nextcord.ui.button(label="Four", style=nextcord.ButtonStyle.blurple, emoji="4️⃣", custom_id="run_4")
    async def Four_button_callback(self, button, interaction):
        global cricket_p2
        global runs2
        if interaction.user == cricket_p2:
            runs2 = "Four"
            buttons = [x for x in self.children]
            for v in buttons:
                v.disabled = True
            await interaction.response.edit_message(view = self)
            
    @nextcord.ui.button(label="Six", style=nextcord.ButtonStyle.danger, emoji="6️⃣", custom_id="run_6")
    async def Six_button_callback(self, button, interaction):
        global cricket_p2
        global runs2
        if interaction.user == cricket_p2:
            runs2 = "Six"
            buttons = [x for x in self.children]
            for v in buttons:
                v.disabled = True
            await interaction.response.edit_message(view = self)

async def match(ctx):
    global cricket_p1
    global cricket_p2
    global score1
    global runs1
    global runs2
    global balls1   
    global wicket1
    global score_msg
    if runs1 == "One" and runs2 == "One":
        wicket1+=1
        score1-=1
        score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} ⚔ {cricket_p2.mention}", color=0xffff00)
        score_emb.add_field(name="LAST BALL🥎", value=f"**WICKET**\n{cricket_p1.mention} got trapped in {cricket_p2.mention}'s Trap!")
        score_emb.add_field(name="SCORECARD📟", value=f"{score1}/{wicket1} ({balls1} balls) \nCurrent Run Rate:{round((score1/balls1), 2)} \t Predicted Score:{round((score1/balls1)*10, 2)}")
        score_emb.set_thumbnail(url = cricket_p1.display_avatar)
        await score_msg.edit(embed=score_emb)
    elif runs1 == "Two" and runs2 == "Two":
        wicket1+=1
        score1-=2
        score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} ⚔ {cricket_p2.mention}", color=0xffff00)
        score_emb.add_field(name="LAST BALL🥎", value=f"**WICKET**\n{cricket_p1.mention} got trapped in {cricket_p2.mention}'s Trap!")
        score_emb.add_field(name="SCORECARD📟", value=f"{score1}/{wicket1} ({balls1} balls) \nCurrent Run Rate:{round((score1/balls1), 2)} \t Predicted Score:{round((score1/balls1)*10, 2)}")
        score_emb.set_thumbnail(url = cricket_p1.display_avatar)
        await score_msg.edit(embed=score_emb)
    elif runs1 == "Three" and runs2 == "Three":
        wicket1+=1
        score1-=3
        score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} ⚔ {cricket_p2.mention}", color=0xffff00)
        score_emb.add_field(name="LAST BALL🥎", value=f"**WICKET**\n{cricket_p1.mention} got trapped in {cricket_p2.mention}'s Trap!")
        score_emb.add_field(name="SCORECARD📟", value=f"{score1}/{wicket1} ({balls1} balls) \nCurrent Run Rate:{round((score1/balls1), 2)} \t Predicted Score:{round((score1/balls1)*10, 2)}")
        score_emb.set_thumbnail(url = cricket_p1.display_avatar)
        await score_msg.edit(embed=score_emb)
    elif runs1 == "Four" and runs2 == "Four":
        wicket1+=1
        score1-=4
        score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} ⚔ {cricket_p2.mention}", color=0xffff00)
        score_emb.add_field(name="LAST BALL🥎", value=f"**WICKET**\n{cricket_p1.mention} got trapped in {cricket_p2.mention}'s Trap!")
        score_emb.add_field(name="SCORECARD📟", value=f"{score1}/{wicket1} ({balls1} balls) \nCurrent Run Rate:{round((score1/balls1), 2)} \t Predicted Score:{round((score1/balls1)*10, 2)}")
        score_emb.set_thumbnail(url = cricket_p1.display_avatar)
        await score_msg.edit(embed=score_emb)
    elif runs1 == "Six" and runs2 == "Six":
        wicket1+=1
        score1-=6
        score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} ⚔ {cricket_p2.mention}", color=0xffff00)
        score_emb.add_field(name="LAST BALL🥎", value=f"**WICKET**\n{cricket_p1.mention} got trapped in {cricket_p2.mention}'s Trap!")
        score_emb.add_field(name="SCORECARD📟", value=f"{score1}/{wicket1} ({balls1} balls) \nCurrent Run Rate:{round((score1/balls1), 2)} \t Predicted Score:{round((score1/balls1)*10, 2)}")
        score_emb.set_thumbnail(url = cricket_p1.display_avatar)
        await score_msg.edit(embed=score_emb)
    elif runs2 == "" or runs1 == "":
        score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} ⚔ {cricket_p2.mention}", color=0xffff00)
        score_emb.add_field(name="MISSED❌", value="Anyone one player didn't respond!")
        score_emb.add_field(name="SCORECARD📟", value=f"{score1}/{wicket1} ({balls1} balls) \nCurrent Run Rate:{round((score1/balls1), 2)} \t Predicted Score:{round((score1/balls1)*10, 2)}")
        score_emb.set_thumbnail(url = cricket_p1.display_avatar)
        await score_msg.edit(embed=score_emb)
    elif runs1 != runs2:
        score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} ⚔ {cricket_p2.mention}", color=0xffff00)
        score_emb.add_field(name="LAST BALL🥎", value=f"{cricket_p1.mention} did a **{runs1}** while {cricket_p2.mention} did a **{runs2}**")
        score_emb.add_field(name="SCORECARD📟", value=f"{score1}/{wicket1} ({balls1} balls) \nCurrent Run Rate:{round((score1/balls1), 2)} \t Predicted Score:{round((score1/balls1)*10, 2)}")
        score_emb.set_thumbnail(url = cricket_p1.display_avatar)
        await score_msg.edit(embed=score_emb)
    runs1 = ""
    runs2 = ""
    await pointcount(ctx)
  
async def pointcount(ctx):
    global balls1
    global wicket1
    global score1
    global score_msg
    global ingl
    global target
    global cricketp1_but
    global cricketp2_but
    global cricket_p1
    global cricket_p2
    global gameOver
    if ingl == False:
        if balls1==10 or wicket1==3:
            score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} scored {score1} in {balls1}!", color=0xffff00)
            score_emb.add_field(name="TARGET🎯", value=f"{cricket_p2.mention} needs to score {score1+1} runs in 10 balls with 3 wickets in hand!")
            score_emb.set_thumbnail(url = cricket_p1.display_avatar)
            await score_msg.edit(embed=score_emb)
            target = score1+1
            cricket_p1,cricket_p2 = cricket_p2,cricket_p1
            wicket1 = 0
            score1 = 0
            balls1 = 0
            ingl = True
            await asyncio.sleep(5)
            view = player1()
            await cricketp1_but.edit(f"For **{cricket_p1}**!",view = view)
            view = player2()
            await cricketp2_but.edit(f"For **{cricket_p2}**!",view = view)
            await time(ctx)
        else:
            view = player1()
            await cricketp1_but.edit(view = view)
            view = player2()
            await cricketp2_but.edit(view = view)
            await time(ctx)
    else:
        if score1>=target:
            score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} crushes {cricket_p2.mention} with {10-balls1} balls to spare and {3-wicket1} wickets in hand!", color=0xffff00)
            score_emb.set_thumbnail(url = cricket_p1.display_avatar)
            await score_msg.edit(embed=score_emb)
            gameOver = True
            
        elif balls1==10 or wicket1==3:
            score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p2.mention} crushes {cricket_p1.mention} with {10-balls1} balls to spare and {3-wicket1} wickets in hand!", color=0xffff00)
            score_emb.set_thumbnail(url = cricket_p2.display_avatar)
            await score_msg.edit(embed=score_emb)
            gameOver = True
        else:
            view = player1()
            await cricketp1_but.edit(f"**{cricket_p1}** needs to score {target-score1} runs in {10-balls1} balls!",view = view)
            view = player2()
            await cricketp2_but.edit(view = view)
            await time(ctx)

@client.command()
async def gameover(ctx):
    global gameOver
    global cricket_p1
    global cricket_p2
    global cricketp1_but
    global cricketp2_but
    global score_msg
    if ctx.author==cricket_p1 or ctx.author==cricket_p2:
        gameOver = True
        await cricketp1_but.delete()
        await cricketp2_but.delete()
        winner = random.randint(1,2)
        if winner == 1:
            score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p1.mention} crushes {cricket_p2.mention} through toss!", color=0xffff00)
            score_emb.set_thumbnail(url = cricket_p1.display_avatar)
            await score_msg.edit(embed=score_emb)
        else:
            score_emb = nextcord.Embed(title="World ICC Tournament", description=f"{cricket_p2.mention} crushes {cricket_p1.mention} through toss!", color=0xffff00)
            score_emb.set_thumbnail(url = cricket_p2.display_avatar)
            await score_msg.edit(embed=score_emb)
    else:
        await ctx.reply(f"You can only end a game played by you!")
    
@client.command()
async def crickethelp(ctx):
    myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"Here are the various commands and rules in order to play this game!", color=0xffff00)
    myEmbed.add_field(name="Commands:-", value=f"1.**$cricket [player1] [player2] ** which starts the game.\n2.**$endgame** ends the current game and crowns one as the winner(Inorder to use this command, you should be the one who is playing the game).", inline=True)
    myEmbed.add_field(name="Rules:-", value=f"1.Both players should press the button only once.\n2.The one who will bat first will always get the message as interaction failed but don't worry as the response is noted.\n3.Both players should press the button within 5 seconds.\n4.If the bot gets stuck it may be an internal error and you may end the game and restart a new one.\n5.**Enjoy and have a Good Time!**", inline=False)
    myEmbed.set_author(name="Yuri's Moderation#2333")
    await ctx.send(embed=myEmbed)

client.run("*****BOT-TOKEN*****")
