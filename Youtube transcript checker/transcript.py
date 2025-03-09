from flask import Flask, request, render_template_string
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    transcript = ""  # Initialize empty transcript

    if request.method == 'POST':
        video_id = request.form.get('video_id')
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            transcript = '\n'.join([t['text'] for t in transcript_list])
        except Exception as e:
            transcript = f"Error: {str(e)}"

    return render_template_string(TEMPLATE, transcript=transcript)

# HTML template with a textarea for better transcript display
TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>VideoSage - YouTube Transcript Extractor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: white;
            padding: 15px;
            text-align: center;
            font-size: 24px;
        }
        .container {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background: white;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            border-radius: 8px;
        }
        input[type="text"], button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #333;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background-color: #555;
        }
        textarea {
            width: 100%;
            height: 300px;
            margin-top: 15px;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
            resize: none;
        }
    </style>
</head>
<body>
    <header>VideoSage - YouTube Transcript Extractor</header>
    <div class="container">
        <form method="POST">
            <input type="text" name="video_id" placeholder="Enter YouTube Video ID..." required>
            <button type="submit">Get Transcript</button>
        </form>
        <textarea readonly>{{ transcript }}</textarea>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
