sum_lesson = {}
with open('lesson.txt', 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        subject, lecture, practice, lab = line.split()
        sum_lesson[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {sum_lesson}')

