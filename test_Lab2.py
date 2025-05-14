import Lab2.py as LAB2

def test_find_min_max():
    datalist = [7, 3, 6, 8, 1, 2, 9]
    expected_result = (1,9)
    test_result = LAB2.find_min_max(datalist)
    assert (test_result == expected_result)

def test_find_average():
    datalist = [7, 3, 6, 8, 1, 2, 9]
    expected_result = 5.1
    test_result = LAB2.calc_average(datalist)
    assert (test_result == expected_result)

def test_find_median_temp():
    datalist = [7, 3, 6, 8, 1, 2, 9]
    expected_result = 6
    test_result = LAB2.calc_average(datalist)
    assert (test_result == expected_result)
