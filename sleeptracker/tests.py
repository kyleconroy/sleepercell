"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from sleeptracker.views import timeslices
from datetime import datetime, time

class TimeSliceTest(TestCase):

    def test_one_slice(self):
        start = datetime(2011, 2, 22, 9)
        end = datetime(2011, 2, 22, 22)
        t = time(8)
        slices = timeslices(start, end, t)
        self.assertEquals(len(slices), 1)
        self.assertEquals(slices[0][0], start)
        self.assertEquals(slices[0][1], end)

    def test_one_slice_early(self):
        start = datetime(2011, 2, 22, 9)
        end = datetime(2011, 2, 22, 22)
        t = time(23)
        slices = timeslices(start, end, t)
        self.assertEquals(len(slices), 1)
        self.assertEquals(slices[0][0], start)
        self.assertEquals(slices[0][1], end)

    def test_one_slice_endexact(self):
        start = datetime(2011, 2, 22, 9)
        end = datetime(2011, 2, 22, 22)
        t = time(22)
        slices = timeslices(start, end, t)
        self.assertEquals(len(slices), 1)
        self.assertEquals(slices[0][0], start)
        self.assertEquals(slices[0][1], end)

    def test_one_slice_startexact(self):
        start = datetime(2011, 2, 22, 9)
        end = datetime(2011, 2, 22, 22)
        t = time(9)
        slices = timeslices(start, end, t)
        self.assertEquals(len(slices), 1)
        self.assertEquals(slices[0][0], start)
        self.assertEquals(slices[0][1], end)

    def test_two_slice(self):
        start = datetime(2011, 2, 22, 7)
        end = datetime(2011, 2, 22, 22)
        t = time(8)
        mid = datetime(2011, 2, 22, 8)
        slices = timeslices(start, end, t)
        self.assertEquals(len(slices), 2)
        self.assertEquals(slices[0][0], start)
        self.assertEquals(slices[0][1], mid)
        self.assertEquals(slices[1][0], mid)
        self.assertEquals(slices[1][1], end)

    def test_three_slice(self):
        start = datetime(2011, 2, 22, 7)
        end = datetime(2011, 2, 23, 22)
        t = time(8)
        midf = datetime(2011, 2, 22, 8)
        mids = datetime(2011, 2, 23, 8)
        slices = timeslices(start, end, t)
        self.assertEquals(len(slices), 3)
        self.assertEquals(slices[0][0], start)
        self.assertEquals(slices[0][1], midf)
        self.assertEquals(slices[1][0], midf)
        self.assertEquals(slices[1][1], mids)
        self.assertEquals(slices[2][0], mids)
        self.assertEquals(slices[2][1], end)
