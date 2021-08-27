import praw
import discord

import random

from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '!')
token = 'token'

channel_id = 0
hours_post = 0
loop_sub = ''

reddit = praw.Reddit(
                    client_id = '_-ejRHCzo21uZ4kSBxswNg', 
                    client_secret = 'VvgMAA9mGx0n5nxFj-W7ayxGRYvR4Q', 
                    username = 'RedditScrapingAlt', 
                    password = 'scrapingredditalt', 
                    user_agent = 'DiscordScraper')

# subreddit = reddit.subreddit('okbuddyguardian')

# hot = subreddit.hot(limit = 1)

# for submission in hot:
#    print(submission.title)

@client.event
async def on_ready():
    await client.change_presence(activity= discord.Game('The bot cannot send posts longer than 6000 characters. If a post is not sent, try again'))
    print('Bot Online')

@client.command()
async def hot(ctx, *, subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    
    #subreddit = reddit.subreddit('okbuddyguardian')

    all_submissions = []

    hot = subreddit.hot(limit = 50)
    
    for submission in hot:
        all_submissions.append(submission)

    random_submission = random.choice(all_submissions)

    name = random_submission.title
    submission_url = random_submission.url
    submission_desc = random_submission.selftext
    link = 'https://www.reddit.com' + random_submission.permalink

    post_embed = discord.Embed(title = name, description = submission_desc, url = link, color = discord.Color.blue())

    post_embed.set_image(url = submission_url)

    await ctx.send(embed = post_embed)

@client.command()
async def top(ctx, *, subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    
    #subreddit = reddit.subreddit('okbuddyguardian')

    all_submissions = []

    top = subreddit.top(limit = 50)
    
    for submission in top:
        all_submissions.append(submission)

    random_submission = random.choice(all_submissions)

    name = random_submission.title
    submission_url = random_submission.url
    submission_desc = random_submission.selftext
    link = 'https://www.reddit.com' + random_submission.permalink 

    post_embed = discord.Embed(title = name, description = submission_desc, url = link, color = discord.Color.blue())

    post_embed.set_image(url = submission_url)

    await ctx.send(embed = post_embed)

client.run(token)
