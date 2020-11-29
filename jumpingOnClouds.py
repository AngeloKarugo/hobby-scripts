def jumpingOnClouds(c):
    c = [int(x) for x in c.split(' ')]
    steps = 0

    for position, _ in enumerate(c[:-2]):

        if c[position] != 's':
            step_1_cloud = c[position+1]
            step_2_cloud = c[position+2]

            if step_2_cloud == 0:
                steps += 1

                c[position] = c[position+1] = 's'
            elif step_1_cloud == 0:
                steps += 1

                c[position] = 's'
        elif len(c) % 2 == 0 and c[position + 1] == 0 and position + 3 == len(c):
            steps += 1
            
    return steps