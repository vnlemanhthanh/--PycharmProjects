import unittest
from partition_souvenirs import partition3, partition3_naive


class PartitionSouvenirs(unittest.TestCase):
    def test_small(self):
        for values in (
            (20,),
            (7, 7, 7),
            (3, 3, 3),
            (3, 3, 3, 3),
            (3, 4, 3, 4, 3, 4),
        ):
            self.assertEqual(partition3(values), partition3_naive(values))

    def test_medium(self):
        for values, answer in (
            ((3, 4, 5, 3, 4, 5, 3, 4, 5), 1),
            type here
        ):
            self.assertEqual(partition3(values), answer)


if __name__ == '__main__':
    unittest.main()
