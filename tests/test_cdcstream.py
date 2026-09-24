import json
import threading
import unittest
import urllib.error
import urllib.request

from journallog import Journal

class TestJournal(unittest.TestCase):
    def test_seq_advances(self):
        journal = Journal()
        first = journal.append("a", "1")
        second = journal.append("b", "2")
        self.assertEqual(second, first + 1)

    def test_latest_kept(self):
        journal = Journal()
        journal.append("a", "1")
        self.assertEqual(journal.latest["a"], "1")

    def test_stats_shape(self):
        self.assertIn("seq", Journal().stats())

    def test_since_empty_at_start(self):
        self.assertEqual(Journal().since(0), [])

    def test_dump_load_stub(self):
        journal = Journal()
        journal.append("a", "1")
        self.assertEqual(journal.dump(), b"")
