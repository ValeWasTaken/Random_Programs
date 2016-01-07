import praw
import pprint

user_agent = ("PRAW Example created by ArnoldM904 on GitHub")
r = praw.Reddit(user_agent = user_agent)
v_fixed = []

subreddit = r.get_subreddit("Bitcoin")

for submission in subreddit.get_hot(limit = 100):
    title = submission.title
    if " " in title.lower():
        v_fixed.append(title)
print "The following %d posts might contain ' ' : " % (len(v_fixed))
pprint.pprint(v_fixed)
