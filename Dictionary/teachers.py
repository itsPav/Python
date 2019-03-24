def num_teachers(dict):
    index = 0
    
    for key in dict:
        index += 1

    return index

def num_courses(dict):
    num_courses = 0

    for key in dict.values():
        num_courses += len(key)

    return num_courses

def courses(dict):
    courses = []

    for key in dict.values():
        courses.extend(key)

    return courses

def most_courses(dict):
    max_courses = 0
    teacher = ''

    for key in dict.keys():
        if len(dict[key]) > max_courses:
            teacher = key

    return teacher

def stats(dict):
    num_courses = []

    for item in dict.items():
        name = item[0]
        courses = len(item[1])

        teacher_info = [name, courses]

        num_courses.append(teacher_info)

    print(num_courses)
    return num_courses

stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
 'Kenneth Love': ['Python Basics', 'Python Collections']})