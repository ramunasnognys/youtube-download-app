import os
import yt_dlp

def get_available_resolutions(url):
    """
    Gets the available resolutions for a YouTube video, checking for all standard resolutions.

    Args:
        url (str): The URL of the YouTube video.

    Returns:
        list: A list of available resolutions.
    """
    standard_resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p']
    ydl_opts = {'quiet': True}
    available_resolutions = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info['formats']
        
        for resolution in standard_resolutions:
            height = int(resolution[:-1])
            if any(f for f in formats if f.get('height') == height):
                available_resolutions.append(resolution)

    return available_resolutions

def download_video(url, output_path, resolution):
    """
    Downloads a YouTube video at the specified resolution using yt-dlp.

    Args:
        url (str): The URL of the YouTube video.
        output_path (str): The directory where the video will be saved.
        resolution (str): The desired video resolution.
    """
    ydl_opts = {
        'format': f'bestvideo[height={resolution[:-1]}]+bestaudio/best[height<={resolution[:-1]}]',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed successfully at {resolution} resolution.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=GAd3JQ1V-10"
    output_path = "./videos"
    
    available_resolutions = get_available_resolutions(url)
    print(f"Available resolutions: {', '.join(available_resolutions)}")
    
    while True:
        desired_resolution = input("Enter desired resolution (e.g., 720p): ")
        if desired_resolution in available_resolutions:
            break
        else:
            print(f"Invalid resolution. Please choose from: {', '.join(available_resolutions)}")
    
    download_video(url, output_path, desired_resolution)