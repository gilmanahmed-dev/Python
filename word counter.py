paragraph = input("Enter your text :")

words = len(paragraph.split())
print(f"Total number of words = {words}")
characters = len(paragraph.replace(" ", ""))
print(f"Total number of characters = {characters}")
