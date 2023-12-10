class Pair: 
    def __init__(self, key, val): 
        self.key = key 
        self.val = val 
    
class HashMap: 
    def __init__(self): 
        self.size = 0               # number of keys in hash map 
        self.capacity = 2           # size of array 
        self.map = [None, None]     # array holding Pairs 
    
    def hash(self, key): 
        index = 0
        for c in key: 
            index += ord(c)
        return index % self.capacity



    def get(self, key): 
        index = self.hash(key)

        while self.map[index] != None: 
            if self.map[index].key == key: 
                return self.map[index].val
            index += 1
            index = index % self.capacity

        return None 

    def put(self, key, val): 
        index = self.hash(key)

        while True: 
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash() 
                return 
            elif self.map[index].key == key: 
                self.map[index].val = val 
                return 

            index += 1
            index = index % self.capacity


    def rehash(self): 
        self.capacity = 2 * self.capacity
        newMap = []

        for _ in range(self.capacity): 
            newMap.append(None)

        oldMap = self.map
        self.map = newMap 

        self.size = 0
        for pair in oldMap: 
            if pair: 
                self.put(pair.key, pair.val) 







