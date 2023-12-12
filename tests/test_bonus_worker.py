from tests import test_worker
from worker import Worker
from bonus_worker import BonusWorker


class TestBonusWorker(test_worker.TestWorker):

    def setUp(self):
        super().setUp()
        self.bonus = 5

    def get_worker(self):
        return BonusWorker(self.name, self.salary, self.bonus)

    def test_parent(self):
        worker = self.get_worker()
        self.assertIsInstance(worker, Worker)

    def test_salary(self):
        worker = self.get_worker()
        correct = 105.0
        self.assertAlmostEqual(worker.salary(), correct, 10)

    def test_tax(self):
        worker = self.get_worker()
        correct = 10.5
        self.assertAlmostEqual(worker.tax(), correct, 10)
