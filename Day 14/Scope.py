class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        maxDifference = 0
        for i in range(len(a)):
            for j in range(len(a)):
                diff = abs(a[i]-a[j])
                if diff>maxDifference:
                    maxDifference = diff 
        self.maximumDifference = maxDifference
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)