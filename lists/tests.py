"""Django Lists App Unit Tests."""

from django.test import TestCase


class SmokeTest(TestCase):
    """Smoke Test class for the Django List App."""

    def test_bad_maths(self):
        """Test test."""
        self.assertEqual(1+1, 3)
