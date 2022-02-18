class Shape():
  def __init__(self):
    pass
  def area(self):
    return 0
class Rectangle(Shape):
  def __init__(self,length,width):
    self.length=length
    self.width=width
    super().__init__()
  def area(self):
    return self.length*self.width
a=list(map(int,input().split()))
s=Rectangle(a[0],a[1])
print(s.area())