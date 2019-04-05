import sys

def mergeSort(alist):
	print("Splitting ",alist)
	if len(alist)>1:
		mid = len(alist)//2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k]=lefthalf[i]
				i=i+1
			else:
				alist[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1
	print("Merging ",alist)


#----------------------------------------------------
#print "params:%s" % sys.argv
#theList = []
# If we pass a list separated by commas with the numbers we are going to sort ...
if len(sys.argv) > 1:
	alist = [int(i) for i in sys.argv[1].split(',')]
else:
	#if no list is passed then we use this one
	alist = [54,26,93,17,77,31,44,55,20]

#print "alist: %s" % alist
#----------------------------------------------------

#alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

