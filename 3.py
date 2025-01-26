def func(List, length):
    if length == 0:  # Base case to stop recursion
        return
    print(List[length - 1], end="")
    func(List, length - 1)

func([4, 3, 2, 1], 4)


#1234

