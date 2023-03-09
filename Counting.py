# counting 
#asking a question

question = input("Please input any text ")
length = len(question)
if length == 0:
    print("You need to enterText, please")
else:
    print(f"Your text is '{question}' and it has '{length}' symbols")
