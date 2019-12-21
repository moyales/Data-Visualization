# A part of Exercise 15.6

def labels_list(L, first_val):
    '''Loop to generate hist.x labels automatically'''
    labels = []
    for i in range(L):
        labels.append(str(first_val + i))

    return labels