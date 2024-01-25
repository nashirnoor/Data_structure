# class Cookie:
#    def __init__(self,color):
#      self.color = color
    
#    def getColor(self):
#      return self.color
   
#    def setColor(self, color):
#      self.color = color

# CookieOne = Cookie("yellow")
# CookieTwo = Cookie("Red")
# print("first:",CookieOne.getColor())
# print(f"Second {CookieTwo.getColor()}")


# num1 = 11
# num2 = num1
# print(num1, num2)
# print(id(num1),id(num2))
# num2 = 12
# print(id(num1),id(num2))


dict1 = {
    'Age':11
    }
dict2 = dict1
dict2['Age'] = 200
print(dict1)
print(dict2)
print(id(dict1))
print(id(dict2))

dict3 = { 'address':'hai'}
print("dict3 is:",dict3)
dict3 = dict2
print(dict3)






