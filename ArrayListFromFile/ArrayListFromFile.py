
text_file = open('ArrayListFromFile\ListEntry.csv', "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
text_file.close()