def outer():
    num = 10

    def inner():
        nonlocal num
        print(num+1)

    inner()

outer()
