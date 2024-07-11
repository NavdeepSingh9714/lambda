#(1)
Slicing=lambda x:x[4:]
print(Slicing("Navdeep"))

#(2)
var = lambda x:x.rstrip()
print(var("  hello Navdeep "))

#(3)
nav = lambda a:a.lstrip()
print(nav("  hello Navdeep "))

#(4)
nav = lambda a:a.strip('#')
print(nav("###Bhakanakalan###"))

#(5)
nav = lambda a:a.strip('cmow.')
print(nav("www.example.com"))

#(6)
nav = lambda a:a.lstrip('Navdeep ')
print(nav("Navdeep Singh!"))

#(7)
nav = lambda a:a.removeprefix('Navdeep ')
print(nav("Navdeep Singh!"))

nav = lambda a:a.removesuffix('Python')
print(nav("HelloHtml"))

#(8)
nav = lambda a:a.replace('\n','')
print(nav(' \n \t hello\n'))

#(9)
nav = lambda a:a.upper()
print(nav("hey buddy how are you!"))

#(10)
nav = lambda a:a.lower()
print(nav("hey buddy how are you!"))

#(11)
nav = lambda a:a.capitalize()
print(nav("hey buddy how are you!"))

#(12)
nav = lambda a:a.islower()
print(nav("HEY BUDDY HOW ARE YOU!"))

nav = lambda a:a.islower()
print(nav("hey buddy how are you!"))

#(13)
nav = lambda a:a.isupper()
print(nav("HEY BUDDY HOW ARE YOU!"))

nav = lambda a:a.isupper()
print(nav("hey buddy how are you!"))

#(14)
nav = lambda a:a.count('o')
print(nav("i love Amritsar"))

#(15)
nav = lambda a:a.find('B')
print(nav("BHAKANA"))

nav = lambda a:a [1:]
print(nav("BHAKANA"))

#(16)
nav = lambda a:a.rfind('A')
print(nav("BHAKANA"))

#(17)
nav = lambda a:a.startswith('BHA')
print(nav("BHAKANA"))

#(18)
nav = lambda a:a.endswith('ANA')
print(nav("BHAKANA"))

#(19)
nav = lambda s:s.partition('development')
print(nav("I am expert in websites development"))

nav = lambda s:s.partition('expert')
print(nav("I am expert in websites development"))

#(20) center
nav = lambda d:d.center(30, '-')
print(nav("Website is Ossum!"))

#(21) ljust
nav = lambda d:d.ljust(30, '-')
print(nav("Website is Ossum!"))

#(22) rjust
nav = lambda d:d.rjust(30, '-')
print(nav("Website is Ossum!"))

#(23) swapcase()
Amrica = lambda h:h.swapcase()
print(Amrica("HELLO Bhaknakalan"))

#(24)) zfill()
Amrica = lambda h:h.zfill(8)
print(Amrica("600"))

Amrica = lambda h:h.zfill(6)
print(Amrica("-900"))

#(25) f-Strings 
let = 'place'
city = 'kota'
Amrica = lambda h:h.fstring()
print(f'{city} is the famous {let} in India!')

#(26)
Amrica = lambda s:s.split()
print(Amrica("Kota city is in rajasthan"))

#(27)rsplit()
Amrica = lambda h:h.rsplit()
print(Amrica("Kota city is in rajasthan"))

#(28) 
nav = lambda s:s.isalpha()
print(nav("worst"))

#(29)
nav = lambda s:s.isnumeric()
print(nav("8084"))

#(30)
shan = lambda s:s.isalnum()
print(shan("best7415"))