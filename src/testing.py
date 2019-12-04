from collections import OrderedDict
import random
import os.path
#
# com = []
# user = []
# o = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in range(5):
#     rand = random.randint(1, len(o)-1)
#     com.append(o[rand])
#     o.pop(rand)
#
# print('com (X)= ', com)
#
# for j in range(3):
#     rand = random.randint(1, len(o)-1)
#     user.append(o[rand])
#     o.pop(rand)
# user.append(o[0])
# o.pop(0)
# print('user (O)= ', user)

# a = OrderedDict()
# a["one"] = 1
# a["two"] = 2
# a["three"] = 3
# a["four"] = 4
# for x in a.keys():
#     print(x)
# a = ["one", "two", "three", "four", "five"]
# for count, i in enumerate(a):
#     print(count, " ", i)
a = ('first',)
b = ",".join(a)
print(b)