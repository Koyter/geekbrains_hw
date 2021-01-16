with open("text.txt", 'w', encoding="utf-8") as f_obj:
    user_text = input('Введите текст \n')
    while user_text:
        f_obj.writelines(user_text)
        user_text = input('Введите текст \n')
        if not user_text:
            break
    f_obj.writelines(user_text)
