from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip

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

    if end_time == None :
        duration = video_clip.duration
    else : 
        duration = end_time

    # Extract the specified segment if start_time and end_time are provided
    if start_time is not None and end_time is not None:
        video_clip = video_clip.subclip(start_time, duration)

    # Compress the video
    video_clip.write_videofile(output_file, bitrate=bitrate)

def get_videoinfo(input_file):
    class VideoInfo():
        def __init__(self) :
            self.name = ""
            self.duration = ""

    
    video_info = VideoInfo()
    video_clip = VideoFileClip(input_file)
    
    video_info.duration = video_clip.duration

    return video_info


#compress_video(f'video53.mp4', "compressed_video.mp4", start_time=16, end_time=duration, bitrate="1500k")
#compress_video(f'video56.mp4', "compressed_video.mp4", start_time=0, end_time=12, bitrate="1500k")
