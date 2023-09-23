# Frame Extractor

Frame Extractor is a simple Python application that allows you to extract individual frames from a video and save them as image files in a specified folder. This can be useful for various purposes, such as video analysis, object detection, or creating image datasets from videos.

## Features

- Extract frames from a video and save them as PNG image files.
- Specify the input video file path and the folder where frames will be saved.
- Frames are saved with sequentially numbered filenames for easy reference.
- Adjustable frame extraction rate (frames per second) to control the number of frames extracted.

## When to Use Frame Extractor

Frame Extractor can be helpful in several scenarios:

1. **Video Analysis**: Extract frames for in-depth video analysis, such as tracking object movements or detecting specific events within the video.

2. **Object Detection**: Create training datasets for object detection models by extracting frames containing objects of interest from videos.

3. **Video Summarization**: Generate a visual summary of a video by extracting key frames at regular intervals.

4. **Quality Control**: Use it in video production or quality control processes to inspect individual frames for issues.

5. **Creating Image Datasets**: Convert videos into image datasets for machine learning tasks like image classification or object recognition.

## How to Use

1. **Installation**: Make sure you have Python installed on your system.

2. **Clone the Repository**: Clone this repository or download the `frame_extractor.py` script.

3. **Usage**:
   - Open a terminal or command prompt.
   - Navigate to the folder containing `frame_extractor.py`.
   - Run the following command, replacing the placeholders with your video file path and desired output folder:
     ```bash
     python frame_extractor.py
     ```
   - Follow the prompts to specify the video file path and output folder.

4. **Review Frames**: Once the extraction process is complete, you'll find the extracted frames in the specified output folder.

## Dependencies

- Python 3.x
- MoviePy library (install it using `pip install moviepy`)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests for any improvements or bug fixes.

## Acknowledgments

- This project uses the [MoviePy](https://zulko.github.io/moviepy/) library for video processing.

---

**Note**: Always respect copyright and usage rights when extracting frames from videos, and ensure you have the necessary permissions to use the video content.
