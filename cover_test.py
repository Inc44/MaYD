from contextlib import contextmanager
from cover import download_video, extract_cover, compress_cover, apply_cover
from filecmp import cmp
from os import path, remove, getcwd, chdir
from parameterized import parameterized
from shutil import copy
from unittest import main, TestCase


video_path = "4TLFaQWcqH8.webm"
video_path_expected = "4TLFaQWcqH8_expected_video.webm"
cover_path = "4TLFaQWcqH8.png"
cover_path_expected = "4TLFaQWcqH8_expected.png"
cover_path_expected_compressed = "4TLFaQWcqH8_expected_compressed.png"
url = "https://music.youtube.com/watch?v=4TLFaQWcqH8"


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
				"m4a",
				"4TLFaQWcqH8.m4a",
				"4TLFaQWcqH8_expected_audio.m4a",
				"4TLFaQWcqH8_expected_audio_covered.m4a",
			),
			(
				"opus",
				"4TLFaQWcqH8.opus",
				"4TLFaQWcqH8_expected_audio.opus",
				"4TLFaQWcqH8_expected_audio_covered.opus",
			),
		]
	)
	def test_cases(
		self, name, audio_path, audio_path_expected, audio_path_expected_covered
	):
		with change_working_directory("test"):
			for file_path in [audio_path, video_path, cover_path]:
				if path.exists(file_path):
					remove(file_path)
			copy(audio_path_expected, audio_path)

			# Test download video
			video_path_test = download_video(url)
			self.assertTrue(cmp(video_path_test, video_path_expected, shallow=False))

			# Test extract cover
			cover_path_test = extract_cover(video_path_test)
			self.assertTrue(cmp(cover_path_test, cover_path_expected, shallow=False))

			# Test compress cover
			compress_cover(cover_path_test)
			self.assertTrue(
				cmp(cover_path_test, cover_path_expected_compressed, shallow=False)
			)

			# Test apply cover
			apply_cover(audio_path, cover_path_test)
			self.assertTrue(cmp(audio_path, audio_path_expected_covered, shallow=False))


if __name__ == "__main__":
	main()
