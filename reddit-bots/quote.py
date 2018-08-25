"""This bot detects when someone says ** Don't quote me on that ** and replies
with their entire comment formatted as a quote and their username credited
beside it. """


import praw

bot = praw.Reddit(user_agent='QuoteBot v0.1',
                  client_id='bjrWn-fxCtiLAg',
                  client_secret='7tHmKGZb_DDSbmHEOrsbw98WK3s',
                  username='quotemeonthat-bot',
                  password='quoquoquo')

subreddit = bot.subreddit("all")
comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if "don't quote me on that" in text.lower() or "dont quote me on that" in text.lower():
        # Generate a message
        message = '"' + text + '"' + "\n\t-u/{0}".format(author)

        comment.reply(message) # Send message
