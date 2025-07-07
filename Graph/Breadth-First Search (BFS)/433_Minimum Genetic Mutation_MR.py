# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

# Example 1:

# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
# Example 2:

# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
 

# Constraints:

# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

import collections
from typing import List

# class Solution:
#     """
#     Solves the minimum gene mutation problem using Breadth-First Search (BFS).
#     """
#     def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
#         """
#         Calculates the minimum number of mutations to transform startGene to endGene
#         using only valid mutations present in the bank.

#         Args:
#             startGene: The starting gene string (8 characters, 'A', 'C', 'G', 'T').
#             endGene: The target gene string (8 characters, 'A', 'C', 'G', 'T').
#             bank: A list of valid gene strings that can be intermediate steps.

#         Returns:
#             The minimum number of mutations required, or -1 if no such transformation exists.
#         """
        
#         if startGene == endGene:
#             return 0
        
#         bankSet = set(bank)
        
#         if endGene not in bankSet:
#             return -1
        
#         queue = collections.deque([(startGene, 0)])
        
#         visited = {startGene}
        
#         chars = ['A', 'C', 'G', 'T']
#         gene_length = len(startGene)
        
#         while queue:
#             current_gene, distance = queue.popleft()
            
#             for i in range(gene_length):
#                 original_char = current_gene[i]
                
#                 for char in chars:
#                     if char == original_char:
#                         continue
                    
#                     else:
#                         newGene_list = list(current_gene)
#                         newGene_list[i] = char
#                         newGene = "".join(newGene_list)
                        
#                         if newGene == endGene:
#                             return distance + 1
                        
#                         if newGene in bankSet and newGene not in visited:
#                         # Mark it as visited.
#                             visited.add(newGene)
#                         # Enqueue it with the updated distance.
#                             queue.append((newGene, distance + 1))
            
#         return -1
                    

# # Example Usage:
# sol = Solution()

# # Example 1:
# startGene1 = "AACCGGTT"
# endGene1 = "AACCGGTA"
# bank1 = ["AACCGGTA"]
# print(f"Example 1 Input: start='{startGene1}', end='{endGene1}', bank={bank1}")
# print(f"Example 1 Output: {sol.minMutation(startGene1, endGene1, bank1)}") # Expected: 1

# print("-" * 20)

# # Example 2:
# startGene2 = "AACCGGTT"
# endGene2 = "AAACGGTA"
# bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# print(f"Example 2 Input: start='{startGene2}', end='{endGene2}', bank={bank2}")
# print(f"Example 2 Output: {sol.minMutation(startGene2, endGene2, bank2)}") # Expected: 2

# print("-" * 20)

# # Example 3 (No path):
# startGene3 = "AAAAACCC"
# endGene3 = "AACCCCCC"
# bank3 = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# print(f"Example 3 Input: start='{startGene3}', end='{endGene3}', bank={bank3}")
# # Simulate a missing link: remove "AAACCCCC"
# bank3_modified = ["AAAACCCC", "AACCCCCC"]
# print(f"Example 3 Modified Bank: {bank3_modified}")
# print(f"Example 3 Output (Modified Bank): {sol.minMutation(startGene3, endGene3, bank3_modified)}") # Expected: -1

# print("-" * 20)

# # Example 4 (End not in bank):
# startGene4 = "AACCGGTT"
# endGene4 = "AAACGGTA"
# bank4 = ["AACCGGTA", "AACCGCTA"] # endGene4 is not in bank
# print(f"Example 4 Input: start='{startGene4}', end='{endGene4}', bank={bank4}")
# print(f"Example 4 Output: {sol.minMutation(startGene4, endGene4, bank4)}") # Expected: -1

# print("-" * 20)

# # Example 5 (Start == End):
# startGene5 = "AACCGGTT"
# endGene5 = "AACCGGTT"
# bank5 = ["AACCGGTA"]
# print(f"Example 5 Input: start='{startGene5}', end='{endGene5}', bank={bank5}")
# print(f"Example 5 Output: {sol.minMutation(startGene5, endGene5, bank5)}") # Expected: 0

from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        chars = ["A", "C", "G", "T"]

        q = deque([(startGene, 0)])
        visited = set()

        if endGene not in bank:
            return -1

        if startGene == endGene:
            return 0

        while q:
            curGene, step = q.popleft()
            visited.add(curGene)

            for i in range(len(curGene)):
                for char in chars:

                    if curGene[i] == char:
                        continue

                    else:
                        newGene = list(curGene)
                        newGene[i] = char
                        newGene = "".join(newGene)

                        if newGene == endGene:
                            return step + 1

                        if newGene in bank and newGene not in visited:
                            q.append((newGene, step + 1))

        return -1
                            
startGene5 = "AACCGGTT"
endGene5 = "AACCGGTT"
bank5 = ["AACCGGTT"]
sol = Solution()
print(f"Example 5 Input: start='{startGene5}', end='{endGene5}', bank={bank5}")
print(f"Example 5 Output: {sol.minMutation(startGene5, endGene5, bank5)}") # Expected: 0                  
        
                
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        chars = ["A", "C", "G", "T"]
        
        if endGene not in bank:
            return -1
        
        if startGene == endGene:
            return 0
        
        q = deque([(startGene, 0)])
        visited = set()
        
        while q:
            GeneCur, move = q.popleft()
            visited.add(GeneCur)
            
            if GeneCur == endGene:
                return move
            
            for i in range(len(GeneCur)):
                for char in chars:
                    if char != GeneCur[i]:
                        GeneCur_list = list(GeneCur)
                        GeneCur_list[i] = char
                        newGene = ''.join(GeneCur_list)
                        if newGene in bank and newGene not in visited:
                            q.append((newGene, move + 1))
            
            return -1
                        
                            
        
        