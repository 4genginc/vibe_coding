# YouTube Video Downloader Guide

This guide explains how to use the enhanced YouTube video downloader that combines both `pytube` and `yt-dlp` for maximum reliability.

## Setup

1. Install required packages:
```bash
pip install --upgrade pytube yt-dlp
```

2. Make sure you have these files in your `codebase` directory:
- `youtube_downloader.py` (main script)
- `requirements.txt` (dependencies)

## Basic Usage

### Simple Download
To download a video in best quality to current directory:
```bash
python youtube_downloader.py "YOUR_YOUTUBE_URL"
```

Example:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=cHTHYzQ8ErU"
```

### Download to Specific Folder
To download to a specific directory:
```bash
python youtube_downloader.py "YOUR_YOUTUBE_URL" "output_directory"
```

Example:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=cHTHYzQ8ErU" "./downloads"
```

## How It Works

The script uses two download methods:
1. First tries `pytube` (faster for simple downloads)
2. If `pytube` fails, automatically falls back to `yt-dlp` (more reliable)

## Troubleshooting

### Common Issues and Solutions

1. **HTTP 400 Error**
   - The script will automatically try the alternative download method
   - Make sure your URL is correct and video is available

2. **Permission Error**
   - Make sure you have write permissions in the output directory
   - Try running with appropriate permissions

3. **Download Failed**
   - Check your internet connection
   - Update the packages:
     ```bash
     pip install --upgrade pytube yt-dlp
     ```
   - Make sure the video is available in your region

### Tips
- Always enclose the YouTube URL in quotes
- Keep both `pytube` and `yt-dlp` updated
- For private or age-restricted videos, the script will automatically handle authentication

## Examples

1. Download to current directory:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=cHTHYzQ8ErU"
```

2. Download to Downloads folder:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=cHTHYzQ8ErU" "~/Downloads"
```

3. Download to a new folder:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=cHTHYzQ8ErU" "./my_videos"
```

## Expected Output

When running the script, you'll see progress information like:
