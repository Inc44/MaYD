# MaYD

MaYD is a project currently in development for downloading music from YouTube.

## 🔧 Usage

1. **URL**:
    - Description: Enter the URL of the playlist or media you wish to download. To ensure the highest quality audio, use HTTPS over HTTP and prefer music.youtube.com.
    - Examples: `youtu.be/QrhcfjPFaEk`, `youtu.be/WAyN4mQgl-4`, `https://music.youtube.com/playlist?list=OLAK5uy_lN9u5OOPNcOJtKWUm5ts7gIixbBnDvagQ`
    - Usage: Provide the URL immediately following the script name in the command line.

2. **Cookie File (Optional)**:
    - Description: Path to the cookie file in the Netscape format for authentication. It can be obtained via [Get Cookies.txt Locally](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc) or [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm). This is optional, and if not provided, the script defaults to using `cookies.txt` located within the script directory.
    - Default: `cookies.txt`
    - Usage: Use the `--cookiefile` option followed by the path to your cookie file if you need to use a different file than the default.

## 🚀 Getting Started

### Installation Steps

1. **Set up a Conda environment**:
    ```bash
    conda create --name MaYD python=3.10
    conda activate MaYD
    ```

2. **Clone the Repository**:
    ```bash
    git clone https://github.com/Inc44/MaYD.git
    ```

3. **Navigate into Project Directory**:
    ```bash
    cd MaYD
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Important Links

- [Anaconda](https://www.anaconda.com/download) - Conda GUI or [Miniconda](https://docs.conda.io/projects/miniconda/en/latest) - Conda CLI
- [Efficient Compression Tool](https://github.com/fhanau/Efficient-Compression-Tool.git) - Photo Compressor
- [FFmpeg](https://www.gyan.dev/ffmpeg/builds/) - Media
- [yt-dlp](https://github.com/yt-dlp/yt-dlp.git) - Media downloader

### System Requirements

Ensure these binaries are in your system's PATH:

- `ect.exe` - Version 0.9.4 tested
- `ffmpeg.exe` - Version 7.0.1 tested
- `yt-dlp.exe` - Version 2024.05.27 tested

#### Adding Binaries to System Path

1. Download the necessary binaries.
2. Include them in your system's PATH, e.g., `C:\Windows\`.

Check their presence:

```bash
ect.exe --version
ffmpeg.exe -version
yt-dlp.exe --version
```

## 🤝 Contribution

Contributions are heartily welcomed! If you're considering significant modifications, please initiate an issue for discussions before submitting a pull request.

## 📜 License

This software is under the GNU General Public License v3.0 (GPL-3.0). For comprehensive details, refer to [LICENSE](LICENSE).