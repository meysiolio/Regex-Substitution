import re
strings = []
for _ in range(int(input())):
    strings.append(input())
    
string = re.sub(r'(?<= )[&][&] ','and ','\n'.join(strings))
print(re.sub(r'(?<= )[|][|] ','or ',string))