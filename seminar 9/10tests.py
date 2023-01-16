import unittest


def calculator(a, b):
    return a / b


def my_func(x, y):
    res = x ** y
    return res


def salary_calculation(time, salary, bonus):
    try:
        result = time * salary + bonus
        return result
    except ValueError:
        return print('введите числовое значение')

def int_func():
    wrd = "слово"
    return wrd.title()



class TestDivideFunction(unittest.TestCase):
    def testdivide(self):
        """test1"""
        self.assertEqual(calculator(4, 2), 2)

    def testdivide2(self):
        self.assertNotEqual(calculator(4, 2), 3)


class TestSquareFunction(unittest.TestCase):
    def testsquare(self):
        self.assertEqual(my_func(3, 3), 27)

    def testsquare2(self):
        self.assertNotEqual(my_func(2, 2), 1)


class TestSalaryCalc(unittest.TestCase):
    def testresult(self):
        self.assertEqual(salary_calculation(5, 5, 5), 30)


class FirstLetter(unittest.TestCase):
    def testletterone(self):
        """test1"""
        self.assertEqual(int_func(), "Слово")

    def testpartofword(self):
        self.assertIn(int_func(), "грамотноеСлово")

    def testwordnotin(self):
        self.assertNotIn(int_func(), "слова")

    def testnoteq(self):
        self.assertNotEqual(int_func(), "словечки")

    def testalmosteq(self):
        self.assertIn(int_func(), "Слово русское")


if __name__ == '__main__':
    unittest.main()
