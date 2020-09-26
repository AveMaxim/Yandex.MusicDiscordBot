import discord
# New coment


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run('NzU4NjM1NTc3ODI5NjIxNzcx.X2x0cA.1dpN3GcF1ZEEc_JGn0f080KoY5g')
