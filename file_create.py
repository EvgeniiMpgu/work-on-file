def main():
    num_employee = int(input('Какое кол-во записей вы хотите создать о сотрудника: '))
    file_employee = open('employee.rtf','w')
    print()

    for count in range(1,num_employee+1):
        print(f'Введите данные о сотруднике №{count}')
        name = input(f'Имя: ')
        id = input(f'Номер/id: ')
        department = input(f'Отдел: ')

        file_employee.write(f'{name}\n')
        file_employee.write(f'{id}\n')
        file_employee.write(f'{department}\n')
        print()


    file_employee.close()
    print('Записи о сотрудниках записаны в emplotee.rtf')
main()