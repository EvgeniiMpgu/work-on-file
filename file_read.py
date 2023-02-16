def main():
    file_employee = open('employee.rtf', 'r')

    name = file_employee.readline()

    while name != '':
        id = file_employee.readline()
        department = file_employee.readline()

        name = name.rstrip('\n')
        id = id.rstrip('\n')
        department = department.rstrip('\n')

        print(f'Имя : {name}')
        print(f'Номер : {id}')
        print(f'Отдел : {department}')
        print()

        name=file_employee.readline()
    file_employee.close()
main()