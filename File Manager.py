import os, shutil
x = input('Enter your path:-')
os.chdir(x)
y = os.listdir(x)

vid = ['mp4','mkv']
mus = ['mp3']
pht = ['png','jpg']
doc = ['xlxs','pdf','pptx','doc','zip','txt']
os.mkdir('Videos')
os.mkdir('Music')
os.mkdir('Photos')
os.mkdir('Documents')
os.mkdir('Others')
for i in y:
    name, extention = i.split('.')
    a = x + '\\' + i
    if extention in vid:
        shutil.move(a,(x + '\\Videos'))
    elif extention in mus:
        shutil.move(a,(x + '\\Music'))
    elif extention in pht:
        shutil.move(a,(x + '\\Photos'))
    elif extention in doc:
        shutil.move(a,(x + '\\Documents'))
    else:
        shutil.move(a,x + '\\Others')
print('Successfully Filtered Your File')
