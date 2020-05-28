#Define the tests before we code the function
from factory_functions import *
# TEst 1- make_dough()

print("When make dough is called with 'water' and 'flour' it should return 'dough'")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))


#Test 2 -

print("when make_dough is called with 'water' and 'cement' it should return not dough")
print(make_dough('water', 'cement') == 'not dough')
print('got:', make_dough('water', 'cement'))


#test3 -bread to sell

print("when we have 'dough' and put it in the oven we have bread to sell")
print(sell_it('dough', 'bake') == 'bread')
print('got:', sell_it('dough', 'bake'))

#test4
print(" when we have dough and put it in the oven we have bread to sell")
print(sell_it('dough', 'salt') == 'not bread')
print('got:', sell_it('dough', 'salt'))

# TEst 5 - down time
#
print("When make_trial_bread is called with 'water' and 'wholewheatflour' it should return 'trial bread'")
print(make_trial_bread('water', 'WholeWheatFlour') == 'trial bread')
print('got:', make_trial_bread('water', 'WholeWheatFlour'))


#Test 6 -

print("When make_trial_bread is called with 'water' and 'plain flour' it should return 'trial bread'")
print(make_trial_bread('water', 'plain_flour') == 'not trial bread')
print('got:', make_trial_bread('water', 'plain_flour'))


#Test 7 - niche markets
print("When niche market is called with 'water' and 'flour' it should return 'whole wheat dough'")
print(niche_market('water', 'flour') == 'dough')
print('got:', niche_market('water', 'flour'))


#Test 8 -

print("when niche market is called with 'water' and 'powder' it should return not dough")
print(niche_market('water', 'powder') == 'not dough')
print('got:', niche_market('water', 'powder'))
