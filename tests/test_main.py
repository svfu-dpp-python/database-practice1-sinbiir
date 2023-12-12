import unittest

from worker import Worker
from main import format_worker


class TestMain(unittest.TestCase):

    def test_print_table_with_worker(self):
        worker = Worker('Иван Петров', 50_000)
        res = format_worker(worker)
        correct = ("Иван Петро"
                   "в         "
                   "          "
                   "  50000.00"
                   "   5000.00"
                   "  45000.00")
        self.assertEquals(res, correct)
