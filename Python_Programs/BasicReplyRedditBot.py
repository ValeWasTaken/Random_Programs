import praw
import time

r = praw.Reddit(user_agent = "Basic Reply Bot for learning PRAW.")
username, password = [line.rstrip('\n') for line in open('user_info.txt')]
r.login(username, password)
words_to_match = ['apple pie','pumpkin pie', 'cherry pie']

def run_bot():
    #Check existing comment ids.
    with open('cache.txt','r') as cache:
        existing = cache.read().splitlines()
        
    subreddit = r.get_subreddit("test")
    print("Grabbing comments..")
    comments = subreddit.get_comments(limit=40)


    with open('cache.txt', 'a+') as cache:
        for comment in comments:
            comment_text = comment.body.lower()
            
            #Defines the check to see if the comment meets the criteria the bot is looking for.
            isMatch = any(string in comment_text for string in words_to_match)

            #Check that comment hasn't been seen before and that it meets the desired critera.
            if comment.id not in existing and isMatch:
                    existing.append(comment.id)
                    cache.write(comment.id + '\n')
                    comment.reply("That's one of my favorite types of pie!")
                    print("I found a new comment! The ID is: " + comment.id)
            
    print("Comment loop finished.")

while True:
    run_bot()
    time.sleep(1200)
