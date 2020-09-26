def can_i_do_it_v1(learn_hard, practice_hard):
    if learn_hard == True and practice_hard == True:
        return True
    else:
        return False


def can_i_do_it_v2(learn_hard, practice_hard):
    if learn_hard is True and practice_hard is True:
        return True
    else:
        return False


def can_i_do_it_v3(learn_hard, practice_hard):
    if learn_hard and practice_hard:
        return True
    else:
        return False


def can_i_do_it_v4(learn_hard, practice_hard):
    return learn_hard and practice_hard


learn_hard = True
practice_hard = True
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it_v1(learn_hard, practice_hard))
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it_v2(learn_hard, practice_hard))
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it_v3(learn_hard, practice_hard))
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it_v4(learn_hard, practice_hard))

learn_hard = True
practice_hard = False
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it_v1(learn_hard, practice_hard))
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it_v2(learn_hard, practice_hard))
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it_v3(learn_hard, practice_hard))
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it_v4(learn_hard, practice_hard))

