# Python Programs

This directory contains two Python programs:

## 1. Hello World Program
A simple Hello World program that prints "Hello, World!" to the console.

To run:
```bash
python hello_world.py
```

## 2. YouTube Video Downloader
A program that downloads videos from YouTube using the pytube library.

### Setup
First, install the required dependencies:
```bash
pip install -r requirements.txt
```

### Usage
To download a YouTube video:
```bash
python youtube_downloader.py <youtube_url> [output_path]
```

Parameters:
- `youtube_url`: The URL of the YouTube video you want to download (required)
- `output_path`: The directory where you want to save the video (optional, defaults to current directory)

Example:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=example" "./downloads"
```

The program will download the video in the highest available resolution. 

### New Script

#### 2.1. yt_downloader.py

This script uses yt-dlp instead of pytube.

To use this new script:

1. Make sure yt-dlp is installed:
```bash
pip install yt-dlp
```

2. Run the script:
```bash
python codebase/yt_downloader.py "YOUR_YOUTUBE_URL"
```

For example:
```bash
python codebase/yt_downloader.py "https://www.youtube.com/watch?v=cHTHYzQ8ErU"
```

To download to a specific folder:
```bash
python codebase/yt_downloader.py "https://www.youtube.com/watch?v=cHTHYzQ8ErU" "./downloads"
```

Would you like me to explain any part of this code or help you set it up? 