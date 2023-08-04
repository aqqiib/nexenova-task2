import pyshorteners

link=input("kindly enter the link you want to shorten:")

shortener=pyshorteners.Shortener()

y=shortener.tinyurl.short(link)

print(y)

