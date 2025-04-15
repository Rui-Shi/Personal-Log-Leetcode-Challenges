# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

# The rules of a Unix-style file system are as follows:

# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:

# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

 

# Example 1:

# Input: path = "/home/"

# Output: "/home"

# Explanation:

# The trailing slash should be removed.

# Example 2:

# Input: path = "/home//foo/"

# Output: "/home/foo"

# Explanation:

# Multiple consecutive slashes are replaced by a single one.

# Example 3:

# Input: path = "/home/user/Documents/../Pictures"

# Output: "/home/user/Pictures"

# Explanation:

# A double period ".." refers to the directory up a level (the parent directory).

# Example 4:

# Input: path = "/../"

# Output: "/"

# Explanation:

# Going one level up from the root directory is not possible.

# Example 5:

# Input: path = "/.../a/../b/c/../d/./"

# Output: "/.../b/d"

# Explanation:

# "..." is a valid name for a directory in this problem.

 

# Constraints:

# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.

import collections # Needed for deque if using BFS approach, but stack (list) is simpler here
from typing import List, Optional # Standard typing imports

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplifies a Unix-style absolute path to its canonical form.

        Args:
            path: The absolute path string.

        Returns:
            The simplified canonical path string.
        """
        # Split the path by slashes. This automatically handles multiple slashes
        # as they result in empty strings in the split list.
        # Example: "/home//foo/".split('/') -> ['', 'home', '', 'foo', '']
        components = path.split('/')

        # Use a list as a stack to keep track of valid directory names
        stack = []

        for component in components:
            if component == "" or component == ".":
                # Ignore empty components (from multiple slashes) and current directory '.'
                continue
            elif component == "..":
                # If '..', pop the last directory from the stack if it's not empty
                if stack:
                    stack.pop()
            else:
                # If it's a valid directory/file name, push it onto the stack
                stack.append(component)

        # Join the components in the stack with a single slash and prepend the root slash
        canonical_path = "/" + "/".join(stack)

        return canonical_path

# Helper function to test the solution (optional)
def run_tests():
    solution = Solution()

    # Example 1:
    path1 = "/home/"
    expected1 = "/home"
    result1 = solution.simplifyPath(path1)
    print(f"Test 1 - Input: '{path1}'")
    print(f"Result: '{result1}', Expected: '{expected1}'")
    print(f"Passed: {result1 == expected1}\n")

    # Example 2:
    path2 = "/../"
    expected2 = "/"
    result2 = solution.simplifyPath(path2)
    print(f"Test 2 - Input: '{path2}'")
    print(f"Result: '{result2}', Expected: '{expected2}'")
    print(f"Passed: {result2 == expected2}\n")

    # Example 3:
    path3 = "/home//foo/"
    expected3 = "/home/foo"
    result3 = solution.simplifyPath(path3)
    print(f"Test 3 - Input: '{path3}'")
    print(f"Result: '{result3}', Expected: '{expected3}'")
    print(f"Passed: {result3 == expected3}\n")

    # Example 4:
    path4 = "/a/./b/../../c/"
    expected4 = "/c"
    result4 = solution.simplifyPath(path4)
    print(f"Test 4 - Input: '{path4}'")
    print(f"Result: '{result4}', Expected: '{expected4}'")
    print(f"Passed: {result4 == expected4}\n")

    # Example 5: Path with '...'
    path5 = "/a/b/c/..."
    expected5 = "/a/b/c/..."
    result5 = solution.simplifyPath(path5)
    print(f"Test 5 - Input: '{path5}'")
    print(f"Result: '{result5}', Expected: '{expected5}'")
    print(f"Passed: {result5 == expected5}\n")

# Uncomment to run tests
# run_tests()
        