#%%
from user import User
from timeline import Timeline

timeline = Timeline()

elon = User("elonmusk", "I'm the owner", timeline)
pepe = User("pepe", "This is not your professor", timeline)
laszlo = User("lazy", "Lazy guy", timeline)
manel = User("manel", "anything and everything", timeline)
julian = User("donjulio", "escape while you can", timeline)

elon.follow(pepe)
elon.follow(manel)
pepe.follow_list([laszlo, manel, julian])
laszlo.follow_list([pepe, manel, julian])
manel.follow_list([elon, pepe, laszlo, julian])
julian.follow(laszlo)

elon.tweet("let's go to Space")
elon.tweet("let that sink in")
pepe.tweet("look at this potato")
laszlo.tweet("elon, tweet about Doge again")
julian.tweet("@lazy, watch your back")
manel.tweet("Python is my best friend")

timeline.show_tweets_for_user(laszlo)
# %%
