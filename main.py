import discord
import os
import requests
import json
# import MySQLdb
from decouple  config


client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

	if message.content.startswith('$vander'):
		await message.channel.send("Vander, or Ivan der Hard and Toe, is a well known character from top seller book \"Tax Fugitive\". The young adult aspiring towards vast greatness, when suddenly a hard-hitting fact about money and worldy-possession wakes him up from reality. Having a hard time realizing the truth, he made the worst possible choice, RUN! While being chased, he fought his way up to greatness with his friend that he made along the way. The man swore that one day he will soar high above the heavens and overcome this past vicissitude.")

token = config('TOKEN')

client.run(token)