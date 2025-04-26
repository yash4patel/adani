from collections import deque

def word_ladder(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:# if there is not endword then return empty list
        return [] 
    
    queue = deque() #initialize queue
    queue.append((beginWord, [beginWord]))
    visited = set()
    visited.add(beginWord)
    
    #bfs travel
    while queue:
        current_word, path = queue.popleft()
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz': #try with every character
                next_word = current_word[:i] + c + current_word[i+1:]
                #generate every possible word and check if is it present in word set or no
                if next_word == endWord:
                    return path + [next_word]
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word) #mark if it is visited
                    queue.append((next_word, path + [next_word]))

    return wordList

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
'''hit" -> "hot" -> "lot" -> "log" -> "cog'''
print(word_ladder(beginWord, endWord, wordList))
