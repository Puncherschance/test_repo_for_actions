import allure

@allure.step('test 1')
def test_number_1_passed():
    assert 1 + 1 == 2

@allure.step('test 2')
def test_number_2_passed():
    assert 1 + 1 == 2

@allure.step('test 3')
def test_number_3_passed():
    assert 1 + 1 == 2

@allure.step('test 4')
def test_number_4_passed():
    assert 1 + 1 == 2

@allure.step('test 5')
def test_number_5_failed():
    assert 1 + 1 == 2

@allure.step('test 6')
def test_number_6_failed():
    assert 1 + 1 == 2