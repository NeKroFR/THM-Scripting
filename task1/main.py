import base64

file = open("b64.txt","r")

flag = file.read()



for i in range(50):
	flag = base64.b64decode(flag)
print(flag)
