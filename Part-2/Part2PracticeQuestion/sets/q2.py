text = "python is easy and python is powerful"
print(f"total words:{len(text.split(" "))}")
print(f"Total unique words: {len(set(text.split(" ")))}")
print(f"Total number of repeated words: {len(text.split(" "))- len(set(text.split(" ")))}")
