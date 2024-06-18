message=input("Enter the text:\n")

lst=message.split(' ')

emoji={
    ':)':'😀',
    ':(':'😪',
    ':|':'😑',
    ':/':'😒',
    ';)':'😉',
}
out=""
for i in lst:
    out+=emoji.get(i,i)+' '
  
print()
print(out)