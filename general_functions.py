# Recap function

# define a funtion

def say_hello_name(name):
    return(f'hello {name} ' )


#BAD
def return_formatted_name(name):
    return name.title().strip()


# #print the return of the function  NOT the funtion
f_name = return_formatted_name( '     Jony   ')
# print(say_hello_name(f_name))
# test set up
# #print('Testing funtion return formated{} with '  '          jon                   ----->' '')
# print(return_formatted_name())
# know_input = '     Jon    '
# expected_out = 'Jon'

print(return_formatted_name(f_name))
#test execution


