import unittest
from pydoc import classname, classify_class_attrs

from six import class_types


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        #print(finishers)
        return finishers


class TournamentTest(unittest.TestCase):
    def setUp(self):
        a = Runner("Усэйн", 10)
        b = Runner("Андрей", 9)
        c = Runner("Ник", 3)
        o = [a, b, c]
        return o
    @classmethod
    def setUpClass(cls):
        all_results = {}

    @classmethod
    def tearDownClass(cls):
        s2 = Tournament(90, )
        i = s2.start()
        cls.assertTrue(s2, "Ник")
        print(i)

