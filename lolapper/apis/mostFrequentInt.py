#gets most frequent integer in an array a.
#assumes that if there is two elements that occur equally more frequent than the rest, return the first.
def getMostFrequent(a):
    k = max(a)
    countArray = [0] * k
    for i in a:
    	countArray[i-1] += 1
    return countArray.index(max(countArray))

def main():
	print(getMostFrequent([1,3,4,3,1,1]))

if __name__ == "__main__":
	main()