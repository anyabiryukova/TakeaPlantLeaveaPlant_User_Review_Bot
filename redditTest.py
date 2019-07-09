import praw

credentials = open(open("loc.txt", "r").readline().strip(), "r")

cid = credentials.readline().strip()
csc = credentials.readline().strip()
usn = credentials.readline().strip()
pwd = credentials.readline().strip()

reddit = praw.Reddit(client_id = cid, client_secret = csc, password = pwd, user_agent = "testscript by /u/eggpl4nt", username = usn)

print(reddit.user.me())

sub = reddit.subreddit("TakeaPlantLeaveaPlant")
redditUser = reddit.redditor("AutonomousBotanist")
#sub.flair.set(redditUser, text = "test ★★★★☆", css_class = "usergreen")

page = sub.wiki["userdirectory"]

file = open("userStuff.txt", "wb")
file.write(page.content_md.encode("utf-8"))
file.close()