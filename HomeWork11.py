# import random
 
# list_1 = [1, 4, 5, 6, 3, 9, 31, 2]
# print ("Сначала был хаос такой: " + str(list_1))
# random.shuffle(list_1)
# print (("Потом стал хаос вот такой: " +  str(list_1))) 

from random import shuffle
x = [[i] for i in range(10)]
shuffle(x)
print(x)
# print(x)  gives  [[9], [2], [7], [0], [4], [5], [3], [1], [8], [6]]
