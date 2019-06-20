a=input()
b=[]
for i in a:
  if i not in b:
    b.append(i)
  else:
    break
if len(b)>4:
  print("4")
else:
  print(len(b))
