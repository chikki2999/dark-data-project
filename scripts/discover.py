import os

for root, dirs, files in os.walk("data"):
    for file in files:
        print(os.path.join(root, file))
