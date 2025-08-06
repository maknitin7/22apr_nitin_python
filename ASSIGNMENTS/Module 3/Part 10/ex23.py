import re

str=" I am the best."

n=re.search("best",str)

if n:
    print("Match found",n.group())
else:
    print("Match not found")