from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import clips_array

def merge_videos(video_path1, video_path2, output_path):
    try:
        clip1 = VideoFileClip(video_path1)
        clip2 = VideoFileClip(video_path2)
        
        # Resize the clips if they have different dimensions
        if clip1.size != clip2.size:
            clip2 = clip2.resize(clip1.size)
        
        final_clip = clips_array([[clip1, clip2]])
        final_clip.write_videofile(output_path, codec='libx264')
    except:
        return "오류발생"
# Example usage
#영상합치기('video1.mp4', 'video2.mp4', 'merged_video.mp4')
