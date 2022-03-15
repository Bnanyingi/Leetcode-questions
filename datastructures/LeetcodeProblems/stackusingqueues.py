class MyStack:
    

    def __init__(self):
        #initialize first 
        self.q = deque()

        
    def push(self, x: int) -> None:
        #adding a value to the stack on the right side by using append function

        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()
        
        
        

    def top(self) -> int:
        """"
        return the top most value which is the value on the right
        """
        return self.q[-1]
    def empty(self) -> bool:
        # return true if it is empty then return false if it is not empty
        return len(self.q) == 0
        


#Your MyStack object will be instantiated and called as such:
#obj = MyStack()
#obj.push(x)
#param_2 = obj.pop()
#param_3 = obj.top()
#param_4 = obj.empty()

