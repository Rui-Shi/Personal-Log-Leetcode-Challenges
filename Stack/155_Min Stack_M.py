# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

class MinStack:

    def __init__(self, stack):
        stack = []
        self.stack = stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.stack)
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# getMin in O(1)
class MinStack:

    def __init__(self):
        """
        Initializes two stacks: one for all values and one to track the minimum
        at each level.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Pushes a value onto the main stack. Also pushes the new current minimum
        onto the min_stack.
        Time Complexity: O(1)
        """
        self.stack.append(val)
        
        # Determine the new minimum. It's either the new value or the previous minimum.
        if self.min_stack:
            # If min_stack is not empty, the new minimum is the smaller of val 
            # and the current minimum (which is at the top of min_stack).
            new_min = min(val, self.min_stack[-1])
        else:
            # If min_stack is empty, this is the first element, so it's the new minimum.
            new_min = val
            
        self.min_stack.append(new_min)

    def pop(self) -> None:
        """
        Pops from both stacks to keep them synchronized.
        Time Complexity: O(1)
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        """
        Returns the top of the main stack.
        Time Complexity: O(1)
        """
        if self.stack:
            return self.stack[-1]
        return None # Or raise an exception, depending on requirements

    def getMin(self) -> int:
        """
        Returns the current minimum value in constant time by looking at the top
        of the min_stack.
        Time Complexity: O(1)
        """
        if self.min_stack:
            return self.min_stack[-1]
        return None # Or raise an exception
    
    

class MinStack:

    def __init__(self):
        """Initializes two stacks: one for values and one for tracking the minimum."""
        self.stack = []      # The main stack to store all elements.
        self.stack_min = []  # A secondary stack to store the current minimum at each level.

    def push(self, val: int) -> None:
        """Pushes a value to the stack and updates the minimum-tracking stack."""
        self.stack.append(val)
        
        # Check if the min_stack has any elements to compare against.
        if self.stack_min:
            # The new minimum is the smaller of the new value and the last recorded minimum.
            min_cur = min(self.stack_min[-1], val)
            self.stack_min.append(min_cur)
        else:
            # If this is the first element, it is the new minimum.
            self.stack_min.append(val)

    def pop(self) -> None:
        """Removes the top element from both stacks to keep them synchronized."""
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        """Returns the top element of the main stack."""
        return self.stack[-1]

    def getMin(self) -> int:
        """Returns the current minimum value in O(1) time."""
        # The current minimum is always the top element of the min_stack.
        return self.stack_min[-1]