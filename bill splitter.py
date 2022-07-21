from itertools import combinations
import numpy as np

def read_book(book,arr,share):
	arr =[]
	share=[]
	for j in range(len(book)):
		arr.append(np.array([book[j]['name'],[book[j]['amt']]]))
		share.append(book[j]['amt']/len(book))
	return arr,share

def share_map(arr,r,share):
	nam=[]
	name=[]
	t_diff=[]
	for i in range(len(arr)):
		nam.append(arr[i][0])
	name=list(combinations(nam,2))
	for i in range(len(name)):
		t_diff.append(list(combinations(share,2))[i][0]-list(combinations(share,2))[i][1])
		if(t_diff[i]>0):
			name[i]=name[i][::-1]
		else:
			t_diff[i]=t_diff[i]*-1
	return name,t_diff

if __name__=="__main__":
	book=[]
	no = int(input("number of people: "))
	print("enter name and amount")
	for x in range(no):
		book.append({"name":input("name: "),"amt":int(input("amount: "))})
	arr=[]
	share=[]
	name=[]
	t_diff=[]
	arr,share=read_book(book,arr,share)
	name,t_diff=share_map(arr,2,share)
	for i in range(len(name)):
		print(name[i])
		print(t_diff[i])