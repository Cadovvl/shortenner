from django.test import TestCase

# Create your tests here.

from links.tools import id_to_link, link_to_id, MAX_IDX

class AnimalTestCase(TestCase):

    def test_tools(self):
        """Animals that can speak are correctly identified"""
        t = 0
        for i in range(100000):
            t += 17 + i
            t %= MAX_IDX
            link = id_to_link(t)
            # print(link)
            self.assertEqual(link, id_to_link(t))
            self.assertEqual(t, link_to_id(link))


