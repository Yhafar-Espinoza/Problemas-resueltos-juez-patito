li = list(input())
for sweet in li:
  while(li.count(sweet) > 1):
    li.remove(sweet)
if(len(li) % 2 == 0):
  print("CHATEA CON ELLA!")
else:
  print("IGNORARLO!")