# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
from anytree import Node, RenderTree
from operator import attrgetter


def findLadders(self, beginWord, endWord, wordList):
    root = Node(beginWord)
    print(root._name)
    createTree(root, endWord, wordList)
    path_to_end = []
    for x in root.descendants:
        if x.is_leaf:
            if x._name == endWord:
                path_to_end.append(x)
    min_height = min(path_to_end, key=attrgetter('depth')).depth
    result = []
    for x in path_to_end:
        if x.depth == min_height:
            result.append([n._name for n in x.path])
    print(result)


def createTree(beginWord, endWord, wordList):
    if not wordList:
        return
    for w1 in wordList:
        if diff_words(beginWord._name, w1) == 1:
            w1_node = Node(w1, parent=beginWord)
            if w1 == endWord:
                return
            iter_list = list(wordList)
            iter_list.remove(w1)
            createTree(w1_node, endWord, iter_list)


def diff_words(word1, word2):
    diff = 0
    for x, y in zip(word1, word2):
        if x != y:
            diff += 1
    return diff


findLadders(0, "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
