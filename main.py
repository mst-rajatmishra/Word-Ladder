from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        # BFS initialization
        queue = deque([beginWord])
        visited = set([beginWord])
        length = 1  # Start with the first word
        
        while queue:
            current_level_size = len(queue)
            
            for _ in range(current_level_size):
                word = queue.popleft()
                
                # Check all possible transformations
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i + 1:]
                        if next_word == endWord:
                            return length + 1  # Return the length including endWord
                        if next_word in wordSet and next_word not in visited:
                            visited.add(next_word)
                            queue.append(next_word)
            
            length += 1  # Increment length for each level
            
        return 0  # No transformation sequence found

# Example usage
solution = Solution()
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# Expected Output: 5
