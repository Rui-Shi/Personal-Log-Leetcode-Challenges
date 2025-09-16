# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

# Constraints:

# 1 <= s.length <= 20
# s consists of digits only.

from typing import List

class Solution:
  def restoreIpAddresses(self, s: str) -> List[str]:
    result = []
    n = len(s)

    # An IP address must be formed from 4 to 12 digits.
    if not 4 <= n <= 12:
        return []

    def backtrack(start_index: int, parts: List[str]):
      """
      Recursively finds valid IP address partitions.
      :param start_index: The starting index in 's' for the next part.
      :param parts: The list of valid parts found so far.
      """
      
      # --- Base Case: A valid solution is found ---
      # If we have 4 parts and have used all digits, we found a valid IP.
      if len(parts) == 4 and start_index == n:
        result.append(".".join(parts))
        return
      
      # --- Base Case: Stop if a solution is not possible ---
      # If we have 4 parts but haven't used all digits, or vice-versa.
      if len(parts) == 4 or start_index == n:
        return

      # --- Recursive Step: Explore the next segment ---
      # An IP address part can be 1, 2, or 3 digits long.
      for length in range(1, 4):
        # Ensure the segment does not go beyond the string's length
        if start_index + length > n:
          break
        
        segment = s[start_index : start_index + length]

        # --- Validation Checks for the segment ---
        # 1. No leading zeros, unless the number is just "0".
        if len(segment) > 1 and segment.startswith('0'):
          continue # Invalid segment, try the next length
        
        # 2. The integer value must be between 0 and 255.
        if not (0 <= int(segment) <= 255):
          continue # Invalid segment, try the next length

        # If the segment is valid, add it and recurse
        parts.append(segment)
        backtrack(start_index + length, parts)
        
        # Backtrack: remove the last part to explore other possibilities
        parts.pop()

    backtrack(0, [])
    return result
        