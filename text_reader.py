infile = open("Lyrics.txt", 'r')

data = infile.read()

numoflines = len(data.splitlines())

print (data)
print (numoflines)
