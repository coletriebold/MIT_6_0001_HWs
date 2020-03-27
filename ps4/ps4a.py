# Problem Set 4A
# Name: Cole Triebold
# Collaborators:
# Time Spent: too much

def get_permutations(sequence):
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
    #index_interest1 = 0
    #index_interest2 = 1
    list_sequence = []
    returnList = []

    if len(sequence) <= 1:  
       return sequence
    for i in range(len(sequence)):
        bigLetter = sequence[i]
        next_seq = sequence.replace(sequence[i],"")
        list_sequence = (get_permutations(next_seq))
        for j in range(0,len(list_sequence)):
             listlist = list(list_sequence[j])
             listlist.insert(0,bigLetter)
             doneZo = "".join(listlist)
             returnList.append(doneZo)
    return returnList

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

