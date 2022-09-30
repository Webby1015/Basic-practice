def genbs(n1,size,word):
	# print(n1,size)
	gen = str(n1)
	n=n1;
	while len(gen)<size:
		n=n+1
		gen+=str(n)
	if(word==gen):
		print("Yes , Bitch")
	else:
		print("No , Bitch")
def bs(word):
	size=len(word)
	size=size/2
	sum=0;
	for i in range(0,int(len(word))):
		sum=sum+int(word[i])
		genbs(sum,int(len(word)),word)
		sum=sum*10
		
		if(i==int(len(word)/2)):
			break
	print()

n=int(input())
for i in range(n):
	word=input()
	bs(word)
