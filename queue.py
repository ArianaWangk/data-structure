class Queue():
    #普通队列只能在队尾添加，队头弹出。(最左边是队头)
    def __init__(self, array = None):
        self.array = array

    def length(self):
        if not self.array:
            return 0
        else:
            return len(self.array)

    def is_Empty(self):
        return self.array == None

    def push(self, value):
        self.array.append(value)

    def pop(self):
        self.array.pop(0)

    def top(self):
        return self.array[0]

    def travel(self):
        print(self.array)

q=Queue([1,2,3])

q.push(4) #变成[1,2,3,4]
q.pop() #变成[2,3,4]
