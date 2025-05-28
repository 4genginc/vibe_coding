#!/usr/bin/env python3

import sys
import os
from pytube import YouTube
from pytube.innertube import _default_clients
import yt_dlp

def download_with_pytube(url, output_path=None):
    try:
        # Fix for age restriction error
        _default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]
        
        # Create a YouTube object
        yt = YouTube(
            url,
            use_oauth=True,
            allow_oauth_cache=True
        )
        
        # Get the highest resolution stream
        video = yt.streams.get_highest_resolution()
        
        # Set default output path if none provided
        if output_path is None:
            output_path = os.getcwd()
        
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Download the video
        print(f"Downloading: {yt.title}")
        print(f"Resolution: {video.resolution}")
        print(f"File size: {video.filesize / (1024*1024):.2f} MB")
        
        video.download(output_path)
        print(f"\nDownload completed! Video saved in: {output_path}")
        return True
        
    except Exception as e:
        print(f"Pytube error: {str(e)}")
        return False

def download_with_ytdlp(url, output_path=None):
    try:
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'best',  # Download best quality
            'outtmpl': '%(title)s.%(ext)s',  # Output template
        }
        
        # If output path is specified, update the output template
        if output_path:
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            ydl_opts['outtmpl'] = os.path.join(output_path, '%(title)s.%(ext)s')

        # Create yt-dlp object and download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])
            
        print("\nDownload completed!")
        return True
        
    except Exception as e:
        print(f"yt-dlp error: {str(e)}")
        return False

def download_video(url, output_path=None):
    """Try downloading with pytube first, if it fails, use yt-dlp"""
    print("Attempting download with pytube...")
    if not download_with_pytube(url, output_path):
        print("\nPytube failed, trying with yt-dlp...")
        if not download_with_ytdlp(url, output_path):
            print("\nBoth download methods failed. Please check:")
            print("1. Make sure the YouTube URL is valid")
            print("2. Check your internet connection")
            print("3. Try updating the tools:")
            print("   pip install --upgrade pytube yt-dlp")
            sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python youtube_downloader.py <youtube_url> [output_path]")
        print("\nExample:")
        print('python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"')
        print('python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" "./downloads"')
        sys.exit(1)
    
    url = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    download_video(url, output_path)

if __name__ == "__main__":
    main()