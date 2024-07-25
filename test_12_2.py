import unittest
from runner_and_tournament import Tournament, Runner


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            print(f"{test_name}: {result}")

    def test_tournament_usain_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results["test_tournament_usain_nik"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(list(results.values())[-1].name == "Ник")

    def test_tournament_andrey_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results["test_tournament_andrey_nik"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(list(results.values())[-1].name == "Ник")

    def test_tournament_usain_andrey_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results["test_tournament_usain_andrey_nik"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(list(results.values())[-1].name == "Ник")

if __name__ == '__main__':
    unittest.main()