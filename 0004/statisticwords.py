f=open('article.txt','r')

dic = {};
line = f.readline()
while line != '':
    words = line.split(' ')
    for word in words:
        if word.lower() in dic:
            dic[word.lower()]+=1
        else:
            dic[word.lower()]=1
    line = f.readline()

for i in dic:
    print i, ":", dic[i]
