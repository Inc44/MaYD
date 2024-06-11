from audio import download_audio, container_audio
from contextlib import contextmanager
from filecmp_custom import cmp
from os import path, remove, getcwd, chdir
from parameterized import parameterized
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
                "4TLFaQWcqH8.m4a",
                "4TLFaQWcqH8_expected_audio.m4a",
                "4TLFaQWcqH8_expected_audio.m4a",
                "141",
            ),
            (
                "opus",
                "4TLFaQWcqH8.webm",
                "4TLFaQWcqH8.opus",
                "4TLFaQWcqH8_expected_audio.webm",
                "4TLFaQWcqH8_expected_audio.opus",
                "774",
            ),
        ]
    )
    def test_cases(
        self,
        name,
        audio_path_audio,
        audio_path,
        audio_path_expected_audio,
        audio_path_expected,
        format,
    ):
        with change_working_directory("test"):
            for file_path in [audio_path_audio, audio_path]:
                if path.exists(file_path):
                    remove(file_path)

            # Test download audio
            audio_path_test = download_audio(url, format=format)
            self.assertTrue(
                cmp(audio_path_test, audio_path_expected_audio, shallow=False)
            )

            # Test container audio
            audio_path_test = container_audio(audio_path_test)
            self.assertTrue(cmp(audio_path_test, audio_path_expected, shallow=False))


if __name__ == "__main__":
    main()
