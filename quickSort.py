arr=[3,2,1,6,4,7]
low=0
high=len(arr)-1

def partition(arr,low,high):    #partitioning index 
	pivot=arr[high]
	i=low-1
	j=low
	while(j<=(high-1)):
		if(arr[j]<pivot):
			i=i+1
			temp=arr[i]   #swapping arr[i] and arr[j]
			arr[i]=arr[j]
			arr[j]=temp
		j=j+1
	temp=arr[i+1]         #swapping arr[i+1] and arr[high]
	arr[i+1]=arr[high] 
	arr[high]=temp
	return (i+1)

def quickSort(arr,low,high):       #main driver code
	if(low<high):
		pi=partition(arr,low,high)
		quickSort(arr,low,pi-1)
		quickSort(arr,pi+1,high)


quickSort(arr,low,high)
print(arr)