# generator.py


# Modify the following function so it return a generator instead of a list 
# get_first_n_integers(3) = [1,2,3]
def get_first_n_integers(n=1000000):
    num_list = []
    for num in range(1, n+1):
        num_list.append(num)
    return num_list
