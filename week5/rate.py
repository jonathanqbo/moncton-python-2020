def rate_v1(test_score, homework_score):
    score = test_score * 0.5 + homework_score * 0.5

    if score >= 90:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 60 and score < 70:
        return 'D'
    else:
        return 'E'


def rate_v2(test_score, homework_score):
    """ the usage of interval comparison """
    score = test_score * 0.5 + homework_score * 0.5

    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'E'


print(rate_v1(100, 100))
print(rate_v1(90, 90))
print(rate_v1(89, 89))
print(rate_v1(60, 60))
print(rate_v1(59, 59))
print(rate_v1(100, 50))

print(rate_v2(100, 100))
print(rate_v2(90, 90))
print(rate_v2(89, 89))
print(rate_v2(60, 60))
print(rate_v2(59, 59))
print(rate_v2(100, 50))
