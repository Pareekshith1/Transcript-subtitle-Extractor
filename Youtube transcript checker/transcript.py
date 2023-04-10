from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        video_id = request.form.get('video_id')
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            transcript = '\n'.join([t['text'] for t in transcript_list])
            return f'Transcript: {transcript}'
        except Exception as e:
            error_message = str(e)
            return f'Error: {error_message}'

    html = '''
       <!DOCTYPE html>
       <html>
       <head>
       	<title>VideoSage</title>
       </head>
       <body>
       <style>
           		body {
			    font-family: Arial, sans-serif;
			background-color: #f2f2f2;
			margin: 0;
			padding: 0;
		}
		
		header {
			background-color: #333;
			color: white;
			padding: 10px;
      height:50px;
			display: flex;
			align-items: center;
			justify-content: space-between;
		}
		
		header h1 {
			font-size: 24px;
      position: relative;
      left: 100px;
			margin: 0;
			padding: 0;
		}
		
		nav {
			display: flex;
			justify-content: space-between;
      height:80px;
			padding: 10px;
			background-color: #ccc;
		}
		
		nav ul {
			list-style: none;
      position:relative;
      top:30px;
      left:600px;
			margin: 0;
			padding: 0;
			display: flex;
		}
		
		nav li {
			margin: 0 10px;
		}
		
		nav a {
			color: #333;
			text-decoration: none;
			font-weight: bold;
			font-size: 16px;
		}
		
		input[type="text"] {
			padding: 10px;
			border: none;
			border-radius: 5px;
			margin: 10px 0;
			width: 70%;
		}
		
		button {
			background-color: #333;
			color: white;
			padding: 10px 20px;
			border: none;
			border-radius: 5px;
			cursor: pointer;
		}
		
		.translation {
			padding: 10px;
      height:500px;
      position:relative;
      top:50px;
			background-color: grey;
			border: 1px solid #ccc;
			border-radius: 5px;
			margin: 10px 0;
			min-height: 100px;
		}

    #textbox{
      width:98.5%;
      height:460px;
      background-color:white;
      overflow-x:display;

      
    }

    .acceptor{
      position:relative;
      top:20px;
      left: 150px;
    }
    
    .join{
        position:relative;
        top:20px;
        left:150px;
    }
           	</style>
       	<header>
       		<h1>VideoSage</h1>
       	</header>
       	<nav>
       		<ul>
       			<li><a href="#">Normal Search</a></li>
       			<li><a href="#">Bulk Search</a></li>
       			<li><a href="#">Transcript Search</a></li>
       			<li><a href="#">Profanity Search</a></li>
       		</ul>
       	</nav>
       	<form method="POST">
       		<div>
       			<input type="text" name="video_id" placeholder="Enter The Youtube Video Id..." class="join">
       			<button type="submit" class="join">Submit</button>
       		</div>
       	</form>
       	<div class="translation">
           <input type="text" id="textbox">
         </div>
       </body>
       </html>
   '''
    return html

if __name__ == '__main__':
    app.run(port=3000, debug=True)



