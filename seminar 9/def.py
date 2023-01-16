import unittest


def int_func():
    wrd = "слово"
    return wrd.title()





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
