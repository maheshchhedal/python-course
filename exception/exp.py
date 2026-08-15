try:
    nm=int(input('Enter You Age : '))
    if nm>18:
        print('You Can Drive')
    else:
        print('You Cannot Drive ')
except Exception as e:
    print(e)
finally:
    print('program clean up .............')
    