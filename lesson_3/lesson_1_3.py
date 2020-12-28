def sum(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 >= arg_2 and arg_3 >= arg_1:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3


print(sum(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))))