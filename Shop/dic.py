data={
    'a':'Ahmed',
    's':'Sidid',
    'b':'baba',
    'nd':{
        'z':'zzz',
        't':'ttt',

    }
}


for k in data.keys():
    print(data[k])

data['a']='MOdif'
print("************")
print(data.get('s'))
data['j']="jojo"

print("************")
for k in data.keys():
    print(data.get(str(k)))


print("******6******")

d=data.get('s')
print(d)

print("******7******")

p=data.get('nd')
print(p)
print(p.get('z'))
m={}
p=m['p']=1
l=[]
l.append("l")
print(p,l)


print("*******************comp************")
dic_1={k:k**2 for k in range(21) }
print(dic_1)
