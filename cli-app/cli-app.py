#!/usr/bin/env python3
import requests


base_url = 'http://localhost:8080/'


def get_attrition():
    response = requests.get(base_url + 'attrition')
    print(f'Percentage of attrition: {response.json()["attrition"] * 100 :.2f}%')

def get_percentage_of_attrition_that_worked_overtime():
    response = requests.get(base_url + 'attrition-overtime')
    print(f'Percentage of people with attrition, who also worked overtime: {response.json()["attritionOvertime"] * 100 :.2f}%')

def add_employee():
    employee_number = int(input('Please enter employee number: '))
    attrition = input('Please enter if employee had attrition [y/n]: ').lower()
    if not (attrition == 'y' or attrition == 'n'):
        print('Invalid input for attrition!')
        return

    response = requests.post(base_url + 'add-row',
                             json={ 'employeeNumber': employee_number,
                                    'attrition': attrition == 'y'
                                  })

    print()
    if response.status_code == 200:
        print(f'Employee {employee_number} added successfully!')
    else:
        print(f'{response.json()["reason"]}')


if __name__ == '__main__':
    while True:
        try:
            print('\nPlease enter an option:')
            print('-----------------------')
            print('[1] Get the percentage of attrition')
            print('[2] Get the percentage of people with attrition, who also worked overtime')
            print('[3] Add an employee to the database')
            print('[x] Exit')
            option = input('Enter: ').strip().lower()
            print()

            if option == '1':
                get_attrition()
            elif option == '2':
                get_percentage_of_attrition_that_worked_overtime()
            elif option == '3':
                add_employee()
            elif option == 'x':
                print('Exiting...')
                break
            else:
                print(f'Invalid option {option} entered')
        except ValueError:
            print('\nUnexpected error occurred!')
            print('This is probably a problem on the server')
