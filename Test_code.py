import unittest
from Python_code import *
from Python_code_2 import *
from Python_code_3 import *


class MyTestCase(unittest.TestCase):
    def test_no_root(self):
        res = square_eq_solver(10, 0, 2)
        self.assertEqual(len(res), 0)

    def test_single_root(self):
        res = square_eq_solver(10, 0, 0)
        self.assertEqual(len(res), 1)
        self.assertEqual(res, [0])

    def test_multiple_root(self):
        res = square_eq_solver(2, 5, -3)
        self.assertEqual(len(res), 2)
        self.assertEqual(res, [0.5, -3])

    def test_sum_digit(self):
        self.assertEqual(sum_digit_num(-0.1789), 25)


class TestWorker(unittest.TestCase):
    def test_worker_full_name(self):
        a = Position('Сергей', 'Иванов', 'Инженер', 100000, 25000)
        self.assertEqual(a.get_full_name(), 'Сергей Иванов')

    def test_worker_full_name_2(self):
        a = Position('Сергей', 'Иванов', 'Инженер', 100000, 25000)
        self.assertEqual(a.get_full_name(), 'Иванов Сергей')

    def test_total_income(self):
        a = Position('Сергей', 'Иванов', 'Инженер', 100000, 25000)
        self.assertEqual(a.get_total_income(), 125000)


class TestCar(unittest.TestCase):
    def test_work_car(self):
        lada = WorkCar(80, 'синяя', 'Lada', True)
        self.assertEqual(lada.show_speed(
        ), 'Скорость Lada превышает разрешенную скорость для данного автомобиля', 'Текущая скорость автомобиля Lada - 80')

    def test_town_car(self):
        oka = TownCar(35, 'белая', 'Oka', False)
        self.assertEqual(oka.show_speed(
        ), 'Скорость Oka в пределах допустимой для данного автомобиля', 'Текущая скорость автомобиля Oka - 35')

    def test_town_car_2(self):
        oka = TownCar(55, 'белая', 'Oka', False)
        self.assertEqual(oka.show_speed(
        ), 'Скорость Oka превышает разрешенную скорость для данного автомобиля', 'Текущая скорость автомобиля Oka - 55')

    def test_police_car(self):
        BMW = PoliceCar(120, 'зеленая',  'BMV', True)
        self.assertTrue(BMW.police())


if __name__ == '__main__':
    unittest.main()
