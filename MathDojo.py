class MathDojo: 
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result+=num
        for number in nums:
            self.result+=number
        return self
    def subtract(self, num, * nums):
        self.result-=num
        for number in nums:
            self.result-=number
        return self
        
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!
#call add 3 times
md1 = MathDojo()
y = md1.add(2).add(5,1).add(6,1,2).result
print(y)
md2 = MathDojo()
z = md2.subtract(3).subtract(2,5).subtract(1,2,3).result
print(z)