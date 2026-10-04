class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.d={}
        self.stack=[]

    def get(self, key: int) -> int:
        print("checking for ",key)
        if key in self.d:#key arelady present, flag as used and return the value
            self.stack.remove(key)
            self.stack.append(key)
            print("status of stack",self.stack)

            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:  #already exists just update
            self.d[key]=value
            self.stack.remove(key)
            self.stack.append(key)
        elif self.capacity>len(self.d):#we have enough capacity put it in and flag as used
            self.d[key]=value
            self.stack.append(key)
        else: #kick the least used one out
            print("successfully removing least used key: ", self.stack[0])
            self.d.pop(self.stack[0],None) #kicked the least one out
            self.stack.remove(self.stack[0])
            self.d[key]=value #add the new key to the capacity
            self.stack.append(key)
        print("status of the stack",self.stack)
        
            

        
