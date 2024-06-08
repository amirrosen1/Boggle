#############################################################
# FILE: ex12_utils.py
# WRITERS: 1.Amir Rosengarten, amir.rosen15, 207942285,
# 2. Avital Harel, avital.harel, 211743381
# EXERCISE: intro2cs2 ex12 2022
# DESCRIPTION:In this exercise we implement a version of the "boggle"
# game.
# In this file, we implement the auxiliary functions.
#############################################################

POSSIBLE_DIRECTION_DICT = {"l": [0, -1], "r": [0, 1], "u": [-1, 0],
                           "d": [1, 0], "ul": [-1, -1], "ur": [-1, 1],
                           "dl": [1, -1], "dr": [1, 1]}
BOARD_COL_SIZE = 4
BOARD_ROW_SIZE = 4


def find_all_sequences(board_in_1D, word_len, all_seq_lst):

    """
    The function returns with the help of an auxiliary function a list
     that contains all the possible combinations for the letters that
      appear on the game board.
    :param board_in_1D: A game board represented in one list.
    :param word_len: The length of the word
    :param all_seq_lst: A list that contains all the phrases that can be
     created from the game board.
    """

    if word_len == 0:
        return ""
    return _help_find_all_sequences(board_in_1D, "", word_len, [])


def _help_find_all_sequences(board_in_1D, current_seq, word_len,
                             all_seq_lst):

    """
        The function returns a list that contains all the possible
         combinations for the letters that appear on the game board.
        :param board_in_1D: A game board represented in one list.
        :param current_seq: Current sequence for certain letters from the
         board.
        :param word_len: The length of the word
        :param all_seq_lst: A list that contains all the phrases that can
         be created from the game board.
    """

    if word_len == 0:
        all_seq_lst.append(current_seq)
        return all_seq_lst
    for letter in board_in_1D:
        _help_find_all_sequences(board_in_1D, current_seq + letter,
                                 word_len - 1, all_seq_lst)
    return all_seq_lst


def create_1d_board(board, path):

    """
        The function creates a one-dimensional list that contains all the
        letters on the board.
        :param board: The board game.
        :param path: Track on the game board.
    """

    board_in_1d = []
    for row, col in path:
        board_in_1d.append(board[row][col])
    return board_in_1d


def is_valid_path(board, path, words):

    """
        The function checks if a track is a valid track that describes
         a word that exists in the word collection. If a trace is indeed
          found, the function returns the word, otherwise the function
           returns None.
        :param board: The board game.
        :param path: Track on the game board.
        :param words: The words list.
    """

    visited = set()

    for i, location in enumerate(path):
        if (location[0] >= BOARD_COL_SIZE) or (location[0] < 0) or \
                (location[1] >= BOARD_ROW_SIZE) or (location[1] < 0):
            return None
        if location in visited:
            return None
        if i < len(path) - 1:
            flag = False
            for dir in POSSIBLE_DIRECTION_DICT.values():
                if (location[0] + dir[0], location[1] + dir[1]) == path[i + 1]:
                    flag = True
                    break
            if not flag:
                return None
            visited.add(location)

    word_from_path = ""
    for location in path:
        word_from_path += board[location[0]][location[1]]
    if word_from_path in words:
        return word_from_path
    return None


def check_if_duplicates(listOfElems):

    """
        The function checks if there are duplicates in a particular list.
    """

    for elem in listOfElems:
        if listOfElems.count(elem) > 1:
            return True
    return False


def check_if_word_has_meaning(temp_coords_lst, board, words):

    """
        The function checks if a particular word has a meaning, that is,
         if a word is in the word list.
        :param temp_coords_lst: List of coordinates of the current word.
        :param board: The board game.
        :param words: List of words.
    """

    if check_if_duplicates(temp_coords_lst):
        return False
    temp_word = ""
    for coord in temp_coords_lst:
        row, col = coord
        current_letter = board[row][col]
        temp_word += current_letter
    if temp_word not in words:
        return False
    return str(temp_word)


def _help_find_length_n_paths(n, board, words, row, col,
                              temp_coord_lst, n_paths_lst):

    """
    Auxiliary function, which returns the list of tracks of length n that
     describe words in the word collection.
    :param n: The length of the routes to be found.
    :param board: The board game.
    :param words: The word list.
    :param row: The index of the row.
    :param col: The index of the column.
    :param temp_coord_lst: A list that contains the coordinates for
     a particular word.
    :param n_paths_lst: The final list of routes.
    """

    # Base case.
    if len(temp_coord_lst) == n:
        if check_if_word_has_meaning(temp_coord_lst, board, words) and \
                (temp_coord_lst not in n_paths_lst):
            n_paths_lst.append(temp_coord_lst)
        return
    # Going all the way, for every value.
    for direction in POSSIBLE_DIRECTION_DICT.values():
        new_row = row + direction[0]
        new_col = col + direction[1]
        if 0 <= new_row < BOARD_ROW_SIZE and 0 <= new_col < BOARD_COL_SIZE:
            _help_find_length_n_paths(n, board, words, new_row, new_col,
                                      temp_coord_lst + [(row, col)],
                                      n_paths_lst)


def find_length_n_paths(n, board, words):

    """
    The function returns a list of all n-length tracks that describe words
     in the word collection.
    :param n: The length of the routes to be found.
    :param board: The game board.
    :param words: The word list.
    """

    n_paths_lst = []
    temp_coords_lst = []
    for row in range(BOARD_ROW_SIZE):
        for col in range(BOARD_COL_SIZE):
            _help_find_length_n_paths(n, board, words, row, col,
                                      temp_coords_lst, n_paths_lst)
    return n_paths_lst


def find_words_in_length_range(board, length_range, words,
                               use_range=False):

    """
    An auxiliary function that returns a list of all the paths that
     describe words in the collection of words that are of length n.
    :param board: The board game.
    :param length_range: A range that represents the length of words to
     be found.
    :param words: The word list.
    :param use_range: A "flag" that represents whether the length is in
     range.
    """

    # Base case.
    if length_range[1] not in range((BOARD_COL_SIZE * BOARD_ROW_SIZE) + 1):
        return []
    n_words_coords_lst = set()
    temp_coords_lst = []
    for row in range(BOARD_ROW_SIZE):
        for col in range(BOARD_COL_SIZE):
            _help_find_length_n_words(length_range, board, words, row, col,
                                      temp_coords_lst, n_words_coords_lst,
                                      "", words.copy(), use_range)
    final_lst = []
    for tup in n_words_coords_lst:
        final_lst.append(list(tup))
    return final_lst


def _help_find_length_n_words(length_range, board, words, row, col,
                              temp_coord_lst, n_words_lst, current_word,
                              filtred_words, use_range):

    """
    Auxiliary function that filters the length of the word list.
    :param length_range: Length range.
    :param board: The board game.
    :param words: The word list.
    :param row: Index of row.
    :param col: Index of column.
    :param temp_coord_lst: Temporary coordinate list.
    :param n_words_lst: List of coordinates of all routes.
    :param current_word: Current word.
    :param filtred_words: Filtered word list.
    :param use_range: A "flag" that represents whether the length is in
     range.
    """

    # Base case.
    if len(current_word) > length_range[1]:
        return
    # Checking the conditions for the word to remain.
    if length_range[1] >= len(current_word + board[row][col]) >= \
            length_range[0]:
        if tuple(temp_coord_lst + [(row, col)]) not in n_words_lst\
                and current_word + board[row][col] in words:
            n_words_lst.add(tuple(temp_coord_lst + [(row, col)]))
        if len(current_word) == length_range[1]:
            return
    # Passing recursion and filtering words.
    for direction in POSSIBLE_DIRECTION_DICT.values():
        new_row = row + direction[0]
        new_col = col + direction[1]
        if 0 <= new_row < BOARD_ROW_SIZE and 0 <= new_col < BOARD_COL_SIZE:
            if (new_row, new_col) in temp_coord_lst:
                continue
            new_filter_words = set()
            if use_range:
                for word in filtred_words:
                    if word.startswith(current_word + board[row][col] +
                                       board[new_row][new_col]):
                        new_filter_words.add(word)
                if len(new_filter_words) == 0:
                    continue

            _help_find_length_n_words(length_range, board, words, new_row,
                                      new_col,
                                      temp_coord_lst + [(row, col)],
                                      n_words_lst,
                                      current_word + board[row][col],
                                      new_filter_words, use_range)


def find_length_n_words(n, board, words):
    """
    The function returns a list of all the paths that describe words in
     the collection of words that are of length n.
    :param n: A number that represents the length of the words to be found.
    :param board: The board game.
    :param words: The word list.
    """

    return find_words_in_length_range(board, (n, n), set(words))


def max_score_paths(board, words):

    """
    The function returns a list of tracks that provide the maximum score
     per game for the board and the collection of words given.
    :param board: The board game.
    :param words: The word list.
    """

    # Create all routes that represent words from the minimum length to
    # the maximum length.
    max_len = -1
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    paths = find_words_in_length_range(board, (0, max_len), set(words),
                                       True)
    # Create all the tracks that provide the maximum score for
    # a particular game.
    word_dict = {}
    for path in paths:
        word = ''.join(create_1d_board(board, path))
        if word not in word_dict.keys():
            word_dict[word] = path
            continue
        if len(path) > len(word_dict[word]):
            word_dict[word] = path
    return list(word_dict.values())
