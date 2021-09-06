

def create_ignore_duplicate(entity, duplicate, value):
    for person in entity.select(entity):
        print(person)
        # print(person[duplicate])
