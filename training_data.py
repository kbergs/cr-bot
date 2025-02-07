import yt_dlp

def download_all_videos_from_channel(channel_url, output_path='videos/'):
    # Set up download options
    ydl_opts = {
        'format': 'best',  # Download the best available video quality
        'outtmpl': f'{output_path}%(title)s.%(ext)s',  # Specify output folder and naming convention
        'quiet': False,  # Display download progress
        'noplaylist': False,  # Ensure playlists are also downloaded if the channel has them
    }

    # Download videos from the channel
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])
        print(f"Downloaded all videos from {channel_url}")

# Example usage
channel_url = 'https://www.youtube.com/@eragon1/videos'  # Replace with the actual channel URL
download_all_videos_from_channel(channel_url)
