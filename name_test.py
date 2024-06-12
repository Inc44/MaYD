from contextlib import contextmanager
from name import create_file_name, create_file_path
from os import path, remove, getcwd, chdir
from parameterized import parameterized
from shutil import copy
from unittest import main, TestCase

info_list = [
    {
        "id": "4TLFaQWcqH8",
        "title": "”Kiwami”meoto kaido",
        "upload_date": "20210407",
        "artist": "GOKUMON(UchikubiGokumonDoukoukai), 大澤敦史",
        "album": "Shufu No Michi",
        "track": "”Kiwami”meoto kaido",
        "release_year": "2021",
    }
]
info_list_item = info_list[0]
file_name_expected = "GOKUMON(UchikubiGokumonDoukoukai), 大澤敦史 - Shufu No Michi - ”Kiwami”meoto kaido - 2021 [4TLFaQWcqH8]"


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
                "4TLFaQWcqH8_expected_audio_covered.m4a",
                "GOKUMON(UchikubiGokumonDoukoukai), 大澤敦史 - Shufu No Michi - ”Kiwami”meoto kaido - 2021 [4TLFaQWcqH8].m4a",
            ),
            (
                "opus",
                "4TLFaQWcqH8.opus",
                "4TLFaQWcqH8_expected_audio_covered.opus",
                "GOKUMON(UchikubiGokumonDoukoukai), 大澤敦史 - Shufu No Michi - ”Kiwami”meoto kaido - 2021 [4TLFaQWcqH8].opus",
            ),
        ]
    )
    def test_cases(
        self,
        name,
        audio_path,
        audio_path_expected_audio_covered,
        audio_path_expected_audio_covered_renamed,
    ):
        with change_working_directory("test"):
            for file_path in [audio_path, audio_path_expected_audio_covered_renamed]:
                if path.exists(file_path):
                    remove(file_path)
            copy(audio_path_expected_audio_covered, audio_path)

            # Test create file name
            file_name = create_file_name(info_list_item)
            self.assertTrue(file_name == file_name_expected)

            # Test create file path
            file_path = create_file_path(audio_path, file_name)
            self.assertTrue(file_path == audio_path_expected_audio_covered_renamed)


if __name__ == "__main__":
    main()
