import glob
import re
categories = ["projects", "seminars", "implementation"]

for cat in categories:
    print(cat)
    posts = sorted(glob.glob("_posts/%s/*.md" % cat))
    for post in posts:
        with open(post) as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("title:"):
                    print("[" + line.strip().replace("title: ", "") + "]", end='')
                if line.startswith("permalink:"):
                    print("(http://localhost:4000/" + line.strip().replace("permalink: ", "") + ")")
    print("")
    