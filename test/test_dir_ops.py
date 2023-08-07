import unittest

from furry_tool.io.dir_ops import get_dir_files_by_asb_filename


class Test_dir_ops(unittest.TestCase):
    def test_get_dir_files_by_asb_filename(self):
        path = r'./Kart/'
        dir_files_names = get_dir_files_by_asb_filename(path)
        self.assertIsInstance(dir_files_names, list)
        self.assertTrue(all(os.path.isabs(file) for file in dir_files_names))


unittest.main()