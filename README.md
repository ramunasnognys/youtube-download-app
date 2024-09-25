## YouTube Downloader with Resolution Selection

This Python script uses the `yt-dlp` library to download YouTube videos, allowing users to select the desired resolution.

### Inputs:

- **URL (str):** The URL of the YouTube video to download.
- **Output Path (str):** The directory where the downloaded video will be saved.

### Outputs:

- **Downloaded Video (mp4):** The YouTube video downloaded at the selected resolution, saved in the specified output path.

### Process:

1. **Get Available Resolutions:** The script first checks the available resolutions for the provided YouTube video.
2. **Display Resolutions:** It presents the user with a list of available resolutions.
3. **User Input:** The user is prompted to enter their desired resolution.
4. **Resolution Validation:** The script validates the user's input, ensuring it's a valid resolution from the available options.
5. **Download Video:** The script downloads the video at the specified resolution, saving it in the designated output path.
6. **Download Completion:** Upon successful download, the script confirms completion and indicates the resolution of the downloaded video.

### Usage:

1. Install the `yt-dlp` library: `pip install yt-dlp`
2. Run the script (e.g., `python test.py`)
3. Enter the YouTube video URL when prompted.
4. Select the desired resolution from the displayed options.

The script will download the video at the chosen resolution and save it to the specified output path.