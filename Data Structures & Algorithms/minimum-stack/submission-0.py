class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.MinStack[-1] if self.MinStack else val)
        self.MinStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]


# if self.minStack else val: This is a safety check.

# If the minStack already has numbers in it, 
# grab the top one (self.minStack[-1]).

# Else (if the stack is completely empty),
#  just use the current val because there is no top item to look at yet.