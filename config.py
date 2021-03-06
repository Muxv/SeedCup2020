HOST = '127.0.0.1'
PORT = 23333

SEED_LIST = [2020, 623500535]

emoji_table = {
    0 : "⬜",
    1 : "🍄",
    2 : "🛹",
    3 : "🔭",
    
    4 : "💚",
    5 : "❤️",
    6 : "💞",
    
    # body
    8 : "🐍",
    9 : "🐅",
    10: "🐇",
    11: "🐈",
    
    # head
    12: "🐉", 
    13: "🐯",
    14: "🐰",
    15: "😾",
}

dir_xy = {
    'w' : (-1, 0),
    'a' : (0, -1),
    's' : (1,  0),
    'd' : (0,  1),
}

HEAD = 12
DEATH = [1, 8, 9, 10, 11, 13, 14, 15]
BENEFIT = [2, 3]
SCORE_1 = 5
SCORE_5 = 6
DANGER = [4]


def set_add(s1, s2):
    return(s1[0] + s2[0], s1[1] + s2[1])

