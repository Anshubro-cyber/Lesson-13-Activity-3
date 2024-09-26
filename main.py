file = open("Abcd.txt","r")
Counter = 0

Content = file.read()

CoList = Content.split("\n")

for i in CoList:
    if i:
                Counter += 1

print("This is the number of lines in the files.")
print(Counter)