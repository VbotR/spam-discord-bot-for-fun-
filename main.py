import discord

bot = discord.Client()

token = input("Токен бота:  ")
server = input("ID: ")

spamchan = []

@bot.event
async def on_ready():
    print("Адский разгон")
    while True:
        sev = bot.get_guild(int(server))
        c = await sev.create_text_channel("Текст")
        spamchan.append(c)
        for i in spamchan:
            await i.send("@everyone")

bot.run(token)
