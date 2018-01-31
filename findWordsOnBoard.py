def build_trie(word_list):
    trie = {}
    for word in word_list:
        t = trie
        for letter in word:
            if letter not in t:
                t[letter] = {}
            t = t[letter]
        t["#"] = "The End"
    return trie


def find_words(word_list, board):
    trie = build_trie(word_list)
    result = set()
    for y in range(len(board)):
        for x in range(len(board[0])):
            find_recursion(trie, board, x, y, '', result)
    print("result ---", result)
    return result


def find_recursion(trie, board, x, y, path, result):
    if "#" in trie:
        result.add(path)
    if y not in range(len(board)) or x not in range(len(board[0])) or board[y][x] not in trie:
        return
    current_letter = board[y][x]
    board[y][x] = "whatever"
    find_recursion(trie[current_letter], board, x + 1, y, path + current_letter, result)
    find_recursion(trie[current_letter], board, x - 1, y, path + current_letter, result)
    find_recursion(trie[current_letter], board, x, y + 1, path + current_letter, result)
    find_recursion(trie[current_letter], board, x, y - 1, path + current_letter, result)
    board[y][x] = current_letter


words_list = ["oath", "pea", "eat", "rain"]
board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]

find_words(words_list, board)
