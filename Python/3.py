def count_even_numbers(start, end):

    list = []

    while start < end:
        if start % 2 == 0:
            list.append(start)
        start += 1

    count = len(list) 
    print(count)



    
count_even_numbers(27, 100)
