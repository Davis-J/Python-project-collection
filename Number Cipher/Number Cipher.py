#Number Cipher
def EncryptNumberCipher():
  Normal=input("Type the text you want to be encrypted: ")
  Normal= Normal.upper()
  Encrypted=''
  Alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  l=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
  for x in Normal:
    if x in Alphabets:
      Encrypted+=l[(ord(x)-65)]
      Encrypted+=' '
    else:
      Encrypted+=x
  Encrypted=Encrypted.replace('  ','||')
  print(Encrypted)
def DecoderNumberCipher():
  Encrypted1=input("Type the numbers you want to be decoded: ")
  q=0
  Normal=''
  Encrypted=''
  for y in Encrypted1:
    if y=='|':
      Encrypted+=' '
    else:
      Encrypted+=y
  Encrypted=Encrypted.split(' ')
  Count=Encrypted.count('')
  for Repeat in range(Count):
    Encrypted.insert(Encrypted.index(''),' ')
    Encrypted.remove('')
  print(Encrypted)
  Alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  l=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
  for x in Encrypted:
    if x in l:
      Normal+=Alphabets[int(x)-1]
    else:
      Normal+=x
  print(Normal)
EncryptNumberCipher()