from contextlib import contextmanager
from filecmp import cmp
from info import download_info, get_info_path, playlist_info, write_info, read_info
from os import path, remove, getcwd, chdir
from parameterized import parameterized
from unittest import main, TestCase


@contextmanager
def change_working_directory(new_dir):
	current_dir = getcwd()
	chdir(new_dir)
	try:
		yield
	finally:
		chdir(current_dir)


class CoverTestCase(TestCase):
	@parameterized.expand(
		[
			(
				"single",
				"https://music.youtube.com/watch?v=4TLFaQWcqH8",
				"Shufu No Michi.database",
				"Shufu No Michi.playlist",
				"Shufu No Michi_single_expected.database",
				"Shufu No Michi_single_expected.playlist",
			),
			(
				"multiple",
				"https://music.youtube.com/playlist?list=OLAK5uy_lN9u5OOPNcOJtKWUm5ts7gIixbBnDvagQ",
				"Shufu No Michi.database",
				"Shufu No Michi.playlist",
				"Shufu No Michi_multiple_expected.database",
				"Shufu No Michi_multiple_expected.playlist",
			),
		]
	)
	def test_cases(
		self,
		name,
		url,
		database_path,
		playlist_path,
		database_path_expected,
		playlist_path_expected,
	):
		with change_working_directory("test"):
			for file_path in [database_path, playlist_path]:
				if path.exists(file_path):
					remove(file_path)

			info = download_info(url)
			playlist_path, database_path = get_info_path(info)

			# Test playlist info
			playlist_path_test = playlist_info(info, playlist_path=playlist_path)
			self.assertTrue(
				cmp(playlist_path_test, playlist_path_expected, shallow=False)
			)

			# Test write info
			database_path_test = write_info(info, database_path=database_path)
			self.assertTrue(
				cmp(database_path_test, database_path_expected, shallow=False)
			)

			info_list = read_info(database_path)


if __name__ == "__main__":
	main()
