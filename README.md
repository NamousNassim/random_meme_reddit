# random_meme_reddit 


# ScreenShots 

![Screenshot](ScreenShots/screen.png) 
![Screenshot2](ScreenShots/screen2.png)  

Author: 
- Namous Nassim

Usage:
- Ensure Flask and the required dependencies are installed.
- Run the Python script.
- Access the application through the defined host and port.

Flask Web Application for Random Programmer Humor Post

This Python code demonstrates a Flask web application that fetches a random post from the "ProgrammerHumor" subreddit and displays the post's title and URL on a webpage.

- Flask: A Python web framework for building web applications.

   - Flask: Used to create the Flask application.
   - render_template: Used to render an HTML template.
   - requests: Used to send HTTP requests and retrieve responses.
   - json: Used to parse JSON data.
   - random: Used to generate random values.


  Fetching data from Reddit:
   - url = "https://www.reddit.com/r/ProgrammerHumor/random.json": Specifies the URL to fetch random posts from the "ProgrammerHumor" subreddit.
  


Rendering the template:
   - Returns the rendered HTML template "index.html" with the post's title and URL.

HTML Template:
- It displays the post's title and an image sourced from the URL.



Usage:
- Ensure Flask and the required dependencies are installed.
- Run the Python script.
- Access the application through the defined host and port.
