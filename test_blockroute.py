# test_blockroute.py
"""
Tests for BlockRoute module.
"""

import unittest
from blockroute import BlockRoute

class TestBlockRoute(unittest.TestCase):
    """Test cases for BlockRoute class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockRoute()
        self.assertIsInstance(instance, BlockRoute)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockRoute()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
