name={}
with open('l.txt','r',encoding='utf-8')as f:
    txt=f.read()
    txt=txt.split('\n')
for i in txt:
    if '小' in i or '中' in i:
        continue
    if '和' not in i:
        continue
    i=i.replace('获得了','')
    i=i.replace('!','')
    if name.get(i):
       name[i]+=1
    else:
        name[i]=1
print(name)
with open('name.txt','w',encoding='utf-8')as f:
    for i in name.keys():
        f.write(i+'\n')