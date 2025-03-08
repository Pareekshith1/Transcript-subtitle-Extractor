# Transcript Subtitle Extractor

## Overview

The **Transcript Subtitle Extractalso **eight Flask-based web application that extracts subtitles or transcripts from YouTube videos using the `youtube-transcript-api`. Users can enter a YouTube video ID, and the application will retrieve the transcript and display it in an easy-to-read format.

## Features

- Extracts subtitles/transcripts from YouTube videos.
- Provides a simple web interface for user input.
- Handles errors gracefully if the transcript is unavailable.
- Lightweight Flask application that runs on a local server.

## Technologies Used

- **Python** (Flask, youtube-transcript-api)
- **HTML & CSS** (Frontend design for user interaction)

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package manager)

### Setup Steps

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Pareekshith1/Transcript-subtitle-Extractor.git
   cd Transcript-subtitle-Extractor
   ```
2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Application:**
   ```sh
   python app.py
   ```
4. **Access the Web Interface:**
   Open your browser and go to `http://127.0.0.1:3000/`.

## Usage

1. Enter a **YouTube Video ID** in the input field.
2. Click **Submit**.
3. If a transcript is available, it will be displayed on the screen.
4. If the transcript is unavailable, an error message will be shown.

## File Structure

```
Transcript-subtitle-Extractor/
│── app.py               # Main Flask application
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
│── ABOUT.md             # About the project
│── COLLABORATION.md     # Contribution guidelines
│── LICENSE              # Open-source license
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

We welcome contributions! Check out the [COLLABORATION.md](COLLABORATION.md) file for guidelines on how to contribute.

## Contact

For any issues or feature requests, feel free to open an issue in the repository.

