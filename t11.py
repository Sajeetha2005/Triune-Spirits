import re
from collections import Counter
import csv
def hashtag_counter(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().lower()
    hashtags = re.findall(r"#\w+", text)  
    counts = Counter(hashtags).most_common(10)  
    with open("hashtags.csv", "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["Hashtag", "Count"])
        writer.writerows(counts)
    print("Top hashtags saved to hashtags.csv")
hashtag_counter("tweets.txt")
