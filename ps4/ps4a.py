# Problem Set 4A
# Name: Kevin DeAngeles
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence, step = 0):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    permutations = []
    
    if len(sequence) == 1:
        permutations.append(sequence)

    else:
        first_letter = sequence[0]
        
        for item in get_permutations(sequence[1:]):
            for i in range(len(item) + 1):
                working_item = list(item)
                working_item.insert(i, first_letter)
                permutations.append(''.join(working_item))
                
    return permutations


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations("a"))
    print(get_permutations("abc"))
    print(get_permutations("kev"))
    print(get_permutations("and"))