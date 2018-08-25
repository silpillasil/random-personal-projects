"""This bot detects sad faces in the comments of sad Reddit users and replies
with a link to a cat picture. STILL WORK IN PROGRESS"""


import praw

bot = praw.Reddit(user_agent='HappyCatsBot v0.1',
                  client_id='F-oTuwAI9tT-sA',
                  client_secret='3FOXetgizhShi_EO1XRrlb4Xi3k',
                  username='happycatsbot',
                  password='happykitty')

subreddit = bot.subreddit('test')
comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if ' :( ' in text.lower():
        # Generate a message
        message = "Sad? Here's a cute cat to help you feel better, u/{0}! [will put cat pic later]".format(author)

        comment.reply(message) # Send message
