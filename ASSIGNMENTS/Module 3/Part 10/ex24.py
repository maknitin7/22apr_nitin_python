import re

str=" No one can defeat me !"

m=re.match("defeat",str)
if m:
    print("Match found")
else:
    print("Match does not found")