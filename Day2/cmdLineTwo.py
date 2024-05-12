if '__main__' == __name__ :
    from sys import argv

    if len(argv) > 1:
        print('Good args are passed.... ' , *argv)
        sum = 0
        for i in argv[1:]:
            sum+= int(i)
        print(f'sum: {sum}')
    else:
        print('Not Good args are not passed')
