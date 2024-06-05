import allure


class TestsSimple:

    @allure.title('test 1')
    def test_number_1_passed(self):
        assert 1 + 1 == 2

    @allure.title('test 2')
    def test_number_2_passed(self):
        assert 1 + 1 == 2

    @allure.title('test 3')
    def test_number_3_passed(self):
        assert 1 + 1 == 2

    @allure.title('test 4')
    def test_number_4_passed(self):
        assert 1 + 1 == 2

    @allure.title('test 5')
    def test_number_5_failed(self):
        assert 1 + 1 == 3

    @allure.title('test 6')
    def test_number_6_failed(self):
        assert 1 + 1 == 3