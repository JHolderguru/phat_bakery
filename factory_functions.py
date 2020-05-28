# follow TDD and separation of concerns

def make_dough(ingridient1, ingridient2):
    if ingridient1 =='water' and ingridient2 =='flour':
        return 'dough'
    else:
        return 'not dough'

def sell_it(req_1, req_2):
    if req_1 == 'dough' and req_2 == 'bake':
        return 'bread'
    else:
        return 'not bread'


def make_trial_bread(ingridient1, ingridient2):
    if ingridient1 =='water' and ingridient2 =='WholeWheatFlour':
        return 'trial bread'
    else:
        return 'not trial bread'

def niche_market(ingridient1, ingridient2):
    if ingridient1 =='water' and ingridient2 =='flour':
        return 'dough'
    else:
        return 'not dough'