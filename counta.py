# No. of times ""a"" appears in list

listOfWord = ["a", "b", "c", "d", "a", "a", "w"]

counta = 0

for x in listOfWord:
    if x == "a":
        counta += 1

print("No. of times ""a"" appears in list: ", counta)
