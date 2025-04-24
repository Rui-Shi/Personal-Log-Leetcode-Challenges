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

class Solution:
    """
    Solves the minimum gene mutation problem using Breadth-First Search (BFS).
    """
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        """
        Calculates the minimum number of mutations to transform startGene to endGene
        using only valid mutations present in the bank.

        Args:
            startGene: The starting gene string (8 characters, 'A', 'C', 'G', 'T').
            endGene: The target gene string (8 characters, 'A', 'C', 'G', 'T').
            bank: A list of valid gene strings that can be intermediate steps.

        Returns:
            The minimum number of mutations required, or -1 if no such transformation exists.
        """

        # --- Pre-checks and Setup ---

        # 1. Trivial case: If start and end are the same, no mutations needed.
        if startGene == endGene:
            return 0

        # 2. Convert the bank list to a set for efficient O(1) average-time lookups.
        #    The set will store all valid intermediate gene states.
        bankSet = set(bank)

        # 3. If the target endGene is not in the bank, it's impossible to reach
        #    as a valid final state (unless startGene == endGene, handled above).
        if endGene not in bankSet:
            return -1

        # --- BFS Implementation ---

        # 4. Initialize a queue for BFS. Store tuples of (gene_string, distance_from_start).
        queue = collections.deque([(startGene, 0)])

        # 5. Initialize a set to keep track of visited gene strings to avoid cycles
        #    and redundant computations. Add the startGene as it's our starting point.
        visited = {startGene}

        # 6. Define the possible characters for mutation.
        chars = ['A', 'C', 'G', 'T']
        gene_length = len(startGene) # Should be 8 based on constraints

        # 7. Start the BFS loop. Continue as long as there are genes to explore.
        while queue:
            # 8. Dequeue the next gene and its distance from the start.
            current_gene, distance = queue.popleft()

            # 9. Try all possible single-character mutations for the current gene.
            for i in range(gene_length):
                original_char = current_gene[i]
                # Iterate through each possible character ('A', 'C', 'G', 'T')
                for char in chars:
                    # Skip if the character is the same as the original (not a mutation)
                    if char == original_char:
                        continue

                    # Create the potential next gene string by changing one character
                    # Converting to list for mutation is often easier than slicing/concatenating
                    next_gene_list = list(current_gene)
                    next_gene_list[i] = char
                    next_gene_str = "".join(next_gene_list)

                    # 10. Check if this mutated gene is the target endGene.
                    if next_gene_str == endGene:
                        # If yes, we've found the shortest path. Return the current distance + 1.
                        return distance + 1

                    # 11. Check if the mutated gene is valid (in the bank) and hasn't been visited yet.
                    if next_gene_str in bankSet and next_gene_str not in visited:
                        # Mark it as visited.
                        visited.add(next_gene_str)
                        # Enqueue it with the updated distance.
                        queue.append((next_gene_str, distance + 1))

        # 12. If the queue becomes empty and we haven't found the endGene,
        #     it means the endGene is unreachable from the startGene via the bank.
        return -1

# Example Usage:
sol = Solution()

# Example 1:
startGene1 = "AACCGGTT"
endGene1 = "AACCGGTA"
bank1 = ["AACCGGTA"]
print(f"Example 1 Input: start='{startGene1}', end='{endGene1}', bank={bank1}")
print(f"Example 1 Output: {sol.minMutation(startGene1, endGene1, bank1)}") # Expected: 1

print("-" * 20)

# Example 2:
startGene2 = "AACCGGTT"
endGene2 = "AAACGGTA"
bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(f"Example 2 Input: start='{startGene2}', end='{endGene2}', bank={bank2}")
print(f"Example 2 Output: {sol.minMutation(startGene2, endGene2, bank2)}") # Expected: 2

print("-" * 20)

# Example 3 (No path):
startGene3 = "AAAAACCC"
endGene3 = "AACCCCCC"
bank3 = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
print(f"Example 3 Input: start='{startGene3}', end='{endGene3}', bank={bank3}")
# Simulate a missing link: remove "AAACCCCC"
bank3_modified = ["AAAACCCC", "AACCCCCC"]
print(f"Example 3 Modified Bank: {bank3_modified}")
print(f"Example 3 Output (Modified Bank): {sol.minMutation(startGene3, endGene3, bank3_modified)}") # Expected: -1

print("-" * 20)

# Example 4 (End not in bank):
startGene4 = "AACCGGTT"
endGene4 = "AAACGGTA"
bank4 = ["AACCGGTA", "AACCGCTA"] # endGene4 is not in bank
print(f"Example 4 Input: start='{startGene4}', end='{endGene4}', bank={bank4}")
print(f"Example 4 Output: {sol.minMutation(startGene4, endGene4, bank4)}") # Expected: -1

print("-" * 20)

# Example 5 (Start == End):
startGene5 = "AACCGGTT"
endGene5 = "AACCGGTT"
bank5 = ["AACCGGTA"]
print(f"Example 5 Input: start='{startGene5}', end='{endGene5}', bank={bank5}")
print(f"Example 5 Output: {sol.minMutation(startGene5, endGene5, bank5)}") # Expected: 0
        
        
                
        