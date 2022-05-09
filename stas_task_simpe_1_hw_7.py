# List comprehentions
list_1 = [i ** 0.5 for i in range(4, 10)]  # Just a simple list of sqrts of some range
list_for_tests = ['monday', 'tuesday', 'wednesday', 'thirsday', 'friday', 'saturday', 'sunday']
list_2 = [i[:3] for i in list_for_tests]  # I want just first 3 letters from list
list_3 = ["Such a beautiful day " + i for i in list_for_tests]  # Add some text
list_4 = [str(list_for_tests.index(i) + 1) + ' day of the week is ' + i for i in
          list_for_tests]  # Add index and some text
list_5 = [i.replace('day', '') for i in list_for_tests]  # Remove day from words
print(list_1, list_2, list_3, list_4, list_5, sep='\n')

# Dict comprehentions
dict_for_test = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh'}
list_of_values_dict_for_test = [k for k in dict_for_test.values()]
dict_1 = {k: v.upper() for k, v in dict_for_test.items()}  # Lets pump our values
dict_2 = {k: v for k, v in zip(dict_for_test.keys(), list_for_tests)}  # Give some numbers for our days with zip help
dict_3 = {k: v for k, v in zip(list_of_values_dict_for_test, list_for_tests)}  # Another help of zip
dict_4 = {k: float(k / 2) for k in range(50, 60)}  # Lets make half from range
dict_5 = {k: v / 2 for k, v in zip(range(1, 10), range(50, 60))}  # Grant a key number for our halfs
print(dict_1, dict_2, dict_3, dict_4, dict_5, sep='\n')

# Set comprehentions
list_for_tests_2 = [8, 9, 67, 4, 4, 5, 21, 8, 9]
set_1 = {i for i in list_for_tests_2}  # Just unique numbers from list
list_for_tests_2 = list_for_tests_2 + [i for i in range(0, 5)]  # Our list got update
set_2 = {i for i in list_for_tests_2}  # Renew our unique numbers
set_3 = {k for k in list_for_tests_2 + [i for i in range(10, 21)]}  # Lets combine some comprehentions
set_4 = {k ** 3 for k in list_for_tests_2}  # Some serious unique cubes here
set_5 = {k % 4 for k in list_for_tests_2}  # How many elements here?
print(set_1, set_2, set_3, set_4, set_5, sep='\n')
