import os
import unittest


class TestMain(unittest.TestCase):
    def test_screenshot_is_present(self):
        exts = ('.png', '.jpg', '.jpeg', '.bmp')
        self.assertTrue(any((
            fn.lower().endswith(ext)
            for fn in os.listdir(os.getcwd())
            for ext in exts
        )))
