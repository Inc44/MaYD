# MaYD

MaYD is a project currently in development for downloading music from YouTube.

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