def display_hash(hashtable):
    for i in range(len(hashtable)):
        print(i,end=" ")
        for j in hashtable[i]:
            print("-->",end=" ")
            print(j,end=" ")
        print()
hashtable=[[]for i in range(10)]
def hashing(keyvalue):
    return keyvalue%len(hashtable)
def insert(hashtable,keyvalue,value):
    hash_key=hashing(keyvalue)
    hashtable[hash_key].append(value)
insert(hashtable,10,'allahabad')
insert(hashtable,25,'mumbai')
insert(hashtable,20,'mathura')
insert(hashtable,9,'delhi')
insert(hashtable,21,'punjab')
display_hash(hashtable)