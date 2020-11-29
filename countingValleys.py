def countingValleys(steps, path):
    path = [x for x in path]
    sea_level = 0
    valleys = 0

    for altitude in path:
        if altitude == "U":
                
            sea_level += 1

            if sea_level == 0:
                valleys += 1
        else:
            sea_level -= 1

    return valleys