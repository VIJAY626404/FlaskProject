# Multi-Site Data Scraper

This project is a simple web application built using Flask that scrapes data from YouTube and Amazon based on a user's search query. The app extracts video titles from YouTube and product names from Amazon and displays the top 5 results from each platform.

## Features

- Scrape YouTube for video titles based on a search query
- Scrape Amazon for product names based on a search query
- Display the top 5 results from both platforms
- Easy-to-use web interface

## Technologies Used

- Python
- Flask (Backend framework)
- BeautifulSoup (Web scraping)
- Requests (HTTP requests)
- HTML/CSS (Frontend)

## Project Structure

```plaintext
Multi-Site Data Scraper/
├── app.py                 # Main Flask application
├── templates/
│   └── home.html          # HTML template for displaying results
├── static/
│   └── (optional)         # Static files like CSS, JS, images if needed
└── README.md              # Project documentation
```
## How to Run the Project
1. **Clone the repository:**
     ``` base
     git clone https://github.com/yourusername/multi-site-data-scraper.git
      cd multi-site-data-scraper
     ```
2. **Install the required Python packages:**
     ``` base
     git clone https://github.com/yourusername/multi-site-data-scraper.git
      cd multi-site-data-scraper
     ```
3. **Run the Flask app:**
 ``` base
python app.py
 ```

Enter a search query in the input field and view the top results from YouTube and Amazon.

## Limitations
- Scraping content from websites may violate their terms of service. Please use this tool responsibly.
- Amazon blocks some automated requests, so results may vary.
- The app currently returns only the top 5 results for simplicity.
## Future Enhancements
- Add support for more websites like eBay, Bing, etc.
- Improve the error handling and user interface.
- Implement a feature to download the scraped data as a CSV file.
## Contributing
Feel free to fork this repository, create a new branch, and submit a pull request. Contributions and suggestions are welcome!

## License
This project is licensed under the MIT License.
