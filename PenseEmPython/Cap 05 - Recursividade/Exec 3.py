def is_triangle(a, b, c):
    if a > (b + c):
        print('No1')
    elif b > (a + c):
        print('No2')
    elif c > (b + a):
        print('No3')
    else:
        print('Yes')


is_triangle(6,5,12)

