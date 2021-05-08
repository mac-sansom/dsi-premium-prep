'''
You're sitting on a park bench.
There is a 0.2 probability that any given 
person walking by is wearing a red hat. What
is the probability that the first person you
see wearing a red hat is the 4th person who 
walks by?
'''
p = 0.2
k_incl = 4
# k_excl = 3

def geometric_pmf(p, k):
    return p * (1-p)**(k-1)

# print(geometric_pmf(p, k_incl))

'''
You are flipping a fair coin. What is the probability that you get your first heads on the 7th flip?
'''
p = 0.5
k_incl = 7

print(geometric_pmf(p, k_incl))
