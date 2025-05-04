# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.

from collections import deque

class MyStack:

    def __init__(self):
        """
        Initializes two empty deques (q1 and q2) to represent the stack.
        """
        self.q1 = deque()  # Primary queue for stack operations
        self.q2 = deque()  # Auxiliary queue for temporary storage during pop and top

    def push(self, x: int) -> None:
        """
        Pushes element x onto the top of the stack (represented by q1).
        """
        self.q1.append(x)  # Add x to the rear of q1 (like pushing onto a stack)

    def pop(self) -> int:
        """
        Removes and returns the element at the top of the stack.
        """
        while len(self.q1) > 1:  # Move all elements except the last one from q1 to q2
            self.q2.append(self.q1.popleft())  # Pop from front of q1 and append to rear of q2

        top_element = self.q1.popleft()  # The last element in q1 is the top of the stack
        self.q1, self.q2 = self.q2, self.q1  # Swap q1 and q2 (q2 now becomes the main queue)
        return top_element

    def top(self) -> int:
        """
        Returns the element at the top of the stack without removing it.
        """
        while len(self.q1) > 1:  # Move all elements except the last one from q1 to q2
            self.q2.append(self.q1.popleft())

        top_element = self.q1[0]  # Peek at the front element of q1 (top of the stack)
        self.q2.append(self.q1.popleft()) #Move the top element to q2
        self.q1, self.q2 = self.q2, self.q1  # Swap q1 and q2 
        return top_element

    def empty(self) -> bool:
        """
        Returns True if the stack is empty, False otherwise.
        """
        return not self.q1  # Stack is empty if q1 is empty


# Example usage (with comments):
# myStack = MyStack()
# myStack.push(1)
# myStack.push(2)
# top_element = myStack.top()  # top_element will be 2
# popped_element = myStack.pop()  # popped_element will be 2
# is_empty = myStack.empty()  # is_empty will be False