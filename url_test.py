from parameterized import parameterized
from unittest import main, TestCase
from url import get_download_domain, create_download_url


id = "4TLFaQWcqH8"


class CoverTestCase(TestCase):
    @parameterized.expand(
        [
            (
                "single",
                "https://music.youtube.com/watch?v=4TLFaQWcqH8",
                "https://music.youtube.com",
                "https://music.youtube.com/watch?v=4TLFaQWcqH8",
            ),
            (
                "multiple",
                "https://music.youtube.com/playlist?list=OLAK5uy_lN9u5OOPNcOJtKWUm5ts7gIixbBnDvagQ",
                "https://music.youtube.com",
                "https://music.youtube.com/watch?v=4TLFaQWcqH8",
            ),
        ]
    )
    def test_cases(
        self,
        name,
        url,
        download_domain,
        download_url,
    ):
        # Test get download domain
        download_domain_test = get_download_domain(url)
        self.assertTrue(download_domain_test == download_domain)

        # Test create download url
        download_url_test = create_download_url(download_domain_test, id)
        self.assertTrue(download_url_test == download_url)


if __name__ == "__main__":
    main()
