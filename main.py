from sub1 import mean
from folder.sub2 import Apple

apple1 = Apple(value=100)
apple2 = Apple(value=200)

result = mean(apple1.value, apple2.value)
print(result)