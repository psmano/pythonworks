# Collections
from collections import Counter
mylist = [1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,5,'a','a','b','b','b','b','b','c']
print(Counter(mylist))
print(Counter('Manohar'))

sentence = 'How many times does each word show up in this sentence with a word'
print(Counter(sentence.split()))