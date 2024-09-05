from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Set headers to simulate browser requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

@app.route('/', methods=['GET', 'POST'])
def home():
    youtube_data = []
    amazon_data = []

    query = request.args.get('query')
    print(f"Query received: {query}")  # Debug print statement

    if query:
        youtube_data = scrape_youtube(query)
        amazon_data = scrape_amazon(query)

    return render_template('home.html', youtube_data=youtube_data, amazon_data=amazon_data)


def scrape_youtube(query):
    url = f'https://www.youtube.com/results?search_query={query}'
    try:
        response = requests.get(url, headers=HEADERS)
        print(f"Response from YouTube: {response.status_code}")  # Debug status code
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())  # Print the HTML for debugging
        video_titles = [title.text.strip() for title in soup.select('#video-title')]
        return video_titles[:5]  # Return only top 5 titles for brevity
    except Exception as e:
        return [f"Error: {str(e)}"]

def scrape_amazon(query):
    url = f'https://www.amazon.com/s?k={query}'
    try:
        response = requests.get(url, headers=HEADERS)
        print(f"Response from Amazon: {response.status_code}")  # Debug status code
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())  # Print the HTML for debugging
        product_names = [name.text.strip() for name in soup.select('.a-size-base-plus')]
        return product_names[:5]  # Return only top 5 products for brevity
    except Exception as e:
        return [f"Error: {str(e)}"]


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
