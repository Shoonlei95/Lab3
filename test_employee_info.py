import employee_info as EI
from employee_info import employee_data as EMPDATA


def test_get_employees_by_age_range():
    expected =[EMPDATA[0], EMPDATA[3], EMPDATA[4]  ]
    result = EI.get_employees_by_age_range(29,36)
    assert(result == expected)


def test_calculate_average_salary():
    expected = 60166.67
    result = EI.calculate_average_salary()
    assert ( result == expected)


def test_get_employees_by_dept():
    expected =[EMPDATA[1], EMPDATA[2] ]
    result = EI.get_employees_by_dept("Marketing")
    assert(result == expected)