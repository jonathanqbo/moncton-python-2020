"""
variable scope
"""

score = 0


def get_score():
    return score


def set_score(points):
    global score
    score = points


def set_score2(points):
    score = points


set_score2(100)
print(get_score())

set_score(100)
print(get_score())
