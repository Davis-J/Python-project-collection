#Caesar Cipher
Normal=input("Type the text you want to be encrypted: ")
Moved=int(input("Type the amount it's shifting(Value should be less than 26 and more than -26): "))
Shifted=''
l='abcdefghijklmnopqrstuvwxyz'
L='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in Normal:
  if x in L:
    if (len(L)-1)>(L.index(x)+Moved):
      Shifted+=L[(L.index(x)+Moved)]
    if (len(L)-1)<(L.index(x)+Moved):
      Shifted+=L[((L.index(x)+Moved)-26)]
  elif x in l:
    if (len(l)-1)>(l.index(x)+Moved):
      Shifted+=l[(l.index(x)+Moved)]
    if (len(l)-1)<(l.index(x)+Moved):
      Shifted+=l[((l.index(x)+Moved)-26)]
  else:
    Shifted+=x
print(Shifted)