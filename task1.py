import re 
from collections import Counter

text = "The quick brown fox jumps over the lazy dog the fox"

words = re.findall(r"[A-za-z]+(?:'[A-Za-z]+)?", text.lower())
length_counts = Counter(len(word) for word in words)

for n,freq in sorted(length_counts.items()):
    print("%d -> %d" % (n,freq))