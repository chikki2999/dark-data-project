import os
from collections import Counter

print("SCRIPT STARTED")

ticket_path = "data/tickets"
files = os.listdir(ticket_path)

print("FILES FOUND:", files)

words = []

for file in files:
    with open(ticket_path + "/" + file, encoding="utf-8") as f:
        words += f.read().lower().split()

counts = Counter(words)

print("TOP WORDS:")
for word, count in counts.most_common(10):
    print(word, count)
import pandas as pd

df = pd.DataFrame(counts.most_common(10), columns=["word", "count"])

df.to_excel("excel/keywords.xlsx", index=False)

print("Excel file created: excel/keywords.xlsx")


