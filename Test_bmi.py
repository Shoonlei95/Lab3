import Lab2.bmi as ABC

def test_CalculateBMI_underweight():
    expected = -1
    result = ABC.calculate_bmi(1.73,37)
    assert(result == expected)


def test_CalculateBMI_Overweight():
    expected = 1
    result = ABC.calculate_bmi(1.73,77)
    assert(result == expected)


def test_CalculateBMI_Normalweight():
    expected = 0
    result = ABC.calculate_bmi(1.73,60)
    assert(result == expected)