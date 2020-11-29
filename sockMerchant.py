def sockMerchant(n, ar):
    ar = [x for x in ar]

    pairs = 0
    
    for sock_color in ar :
        # count the number of socks of one color in the pile
        color_sock_count = ar.count(sock_color)
        
        # find the number of complete pairs of that color
        color_pairs = color_sock_count // 2
        
        # increment the number of pairs found
        pairs += color_pairs
        
        # remove socks of that color from the list
        ar = [x for x in ar if x != sock_color]
            
    return pairs
