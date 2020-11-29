def minimumAbsoluteDifference(arr):
    """
    find the minimum absolute difference among integers in a list
    """

    differences = []

    for index, x in enumerate(arr):

        differences += [abs(x - i) for i in arr[index + 1:]]
        
    minimum_absolute_difference = min(differences)

    return minimum_absolute_difference