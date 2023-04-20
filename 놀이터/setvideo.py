from moviepy.video.io.VideoFileClip import VideoFileClip

def compress_video(input_file, output_file, start_time=None, end_time=None, bitrate="1500k"):
    """
    Compresses a video file while minimizing quality loss.
    :param input_file: The path to the input video file.
    :param output_file: The path to the output video file.
    :param start_time: The start time of the segment to be extracted (in seconds). Optional.
    :param end_time: The end time of the segment to be extracted (in seconds). Optional.
    :param bitrate: The target bitrate of the output video (in kbps). Default is 1500k.
    """
    # Load the video clip
    video_clip = VideoFileClip(input_file)
    video_clip = video_clip.without_audio()

    # Extract the specified segment if start_time and end_time are provided
    if start_time is not None and end_time is not None:
        video_clip = video_clip.subclip(start_time, end_time)

    # Compress the video
    video_clip.write_videofile(output_file, bitrate=bitrate)


compress_video(f'video50.mp4', "compressed_video.mp4", start_time=0, end_time=35, bitrate="1500k")
