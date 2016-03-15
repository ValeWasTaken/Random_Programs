# Python 3.4
# For usage on phpBB forums.
# Using Comic Sans font, make a post multi-colored to mess with other users. (I'm so sorry..)
import random

post = input()

def annoying_post(post):
    annoying_post = []
    
    for word in post.split():
        color = "[color=#%06x]" % random.randint(0, 0xFFFFFF)
        annoying_post.append("{0}{1}[/color]".format(color, word))

    words = ' '.join(annoying_post)
    result = "[font=Comics Sans MS]{0}[/font]".format(words)
    print(result)
    
annoying_post(post)
