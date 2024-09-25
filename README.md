
# YouTube Video Downloader with Resolution Selection and Compression

This Python project provides a script for downloading YouTube videos with custom resolution selection and optional compression. It utilizes the `yt-dlp` library for video downloading and FFmpeg for post-download compression.

## Features

- Fetches available resolutions for a given YouTube video
- Allows users to select their desired resolution
- Downloads the video in the chosen resolution
- Offers an option to compress the downloaded video using FFmpeg
- Displays file size before and after compression

## Inputs

1. **YouTube URL**: The URL of the video to be downloaded
2. **Output Path**: The directory where the video will be saved
3. **Desired Resolution**: User's choice from available resolutions
4. **Compression Option**: Whether to compress the video after download
5. **CRF Value**: Constant Rate Factor for compression (if compression is chosen)

## Outputs

1. **Downloaded Video**: The YouTube video saved in the specified output path
2. **Compressed Video**: (Optional) A compressed version of the downloaded video
3. **Console Output**: Information on available resolutions, download progress, and compression results

## Usage

1. Install required libraries:
   ```
   pip install yt-dlp
   ```
2. Ensure FFmpeg is installed on your system
3. Run the script:
   ```
   python youtube_downloader.py
   ```
4. Follow the prompts to enter the YouTube URL, select resolution, and choose compression options

## Code Structure

- `get_available_resolutions(url)`: Fetches available resolutions for a given YouTube video
- `download_video(url, output_path, resolution)`: Downloads the video at the specified resolution
- `compress_video(input_file, output_file, crf)`: Compresses the downloaded video using FFmpeg
- Main script logic:
  - Prompts for YouTube URL
  - Displays available resolutions
  - Downloads video in chosen resolution
  - Offers compression option
  - Compresses video if chosen
  - Displays file size comparison

## Notes

- The project includes a `.gitignore` file to exclude virtual environments, Python cache files, and downloaded videos from version control
- A `README.md` file provides basic usage instructions
- The `improved.md` file suggests further enhancements, including the implemented compression feature

This project is useful for users who want to download YouTube videos in specific resolutions and have control over the file size through optional compression.
