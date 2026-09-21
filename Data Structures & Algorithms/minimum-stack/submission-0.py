class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if len(self.items) == 0:
            self.items.append((val,val))
        else:
            if val > self.items[-1][-1]:
                self.items.append((val,self.items[-1][-1]))
            else:
                self.items.append((val,val))

    def pop(self) -> None:
        temp = self.items.pop(-1)[0]
        return temp

    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][-1]
