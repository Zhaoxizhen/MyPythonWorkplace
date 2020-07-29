import sys, shelve


def store_person(db):
    unique_id = input('Please enter the unique id:')
    person = dict()
    person['name'] = input('please enter your name:')
    person['phone'] = input('please enter your phone number:')
    person['age'] = input('please enter your age:')
    db[unique_id] = person


def show_info(db):
    unique_id = input('please enter your unique id:')
    field = input('please enter what information do you want(name, phone, age):')
    field.strip().lower()
    try:
        print('The {field} you choose is: '.format(field=field), db[unique_id][field])
    except KeyError:
        print('The param you enter is invalid!')


def main():
    db = shelve.open('D:\\python workplace\\person_db.dat')
    try:
        while True:
            cmd = input('please enter the command(store, show, exit):')
            if cmd == 'store':
                store_person(db)
            if cmd == 'show':
                show_info(db)
            if cmd == 'exit':
                return
    finally:
        db.close()


if __name__ == '__main__':
    main()
