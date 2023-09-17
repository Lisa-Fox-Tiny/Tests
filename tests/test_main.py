from unittest import TestCase

from main import get_unique_names, get_par, min_course, api_ya


class TestGET(TestCase):
    def test_1(self):
        real_result = get_unique_names()
        with open('res.txt', 'r', encoding='utf-8') as f:
            data = list(f)
        data = ' '.join(data)
        self.assertEqual(real_result, data)

    def test_2(self):
        a = 'Alex и Emma'
        b = 'Gena и Masha'
        my_list = get_par()
        self.assertIn(a, my_list)
        self.assertNotIn(b, my_list)

    def test_3(self):
        real_result = min_course()
        self.assertEqual(type(real_result), str)

    def test_4(self):
        real_result = api_ya()
        self.assertEqual(real_result, 201)


