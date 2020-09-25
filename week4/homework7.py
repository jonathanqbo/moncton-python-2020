# version 1
def can_i_do_it(learn_hard, practice_hard):
    if learn_hard and practice_hard:
        return True
    else:
        return False


learn_hard = True
practice_hard = True
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it(learn_hard, practice_hard))

learn_hard = True
practice_hard = False
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it(learn_hard, practice_hard))


# version 2
def can_i_do_it_v2(learn_hard, practice_hard):
    return learn_hard and practice_hard


learn_hard = True
practice_hard = True
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it_v2(learn_hard, practice_hard))

learn_hard = True
practice_hard = False
print('if i learn hard', learn_hard, 'and practice hard', practice_hard, ', then I can do it', can_i_do_it_v2(learn_hard, practice_hard))