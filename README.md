# Nike Website Web Scraping with Scrapy and Selenium

This repository contains a web scraping project using Scrapy and Selenium to extract clothing and male shoe data from the Nike website. The Nike website employs JavaScript for rendering its content, which necessitates the use of Selenium Chrome WebDriver to obtain the page source. Subsequently, Scrapy selectors are utilized to scrape the desired data from the HTML.

## Technologies Used
- Python
- Scrapy
- Selenium

## Installation
1. Clone this repository to your local machine.
2. Install Python if not already installed.
3. Install Scrapy and Selenium using pip: pip install scrapy selenium
4. Download Chrome WebDriver from here and place it in your system's PATH.



### Usage

1. Navigate to the project directory.
2. Modify the nike_spider.py file to customize the scraping logic according to your requirements.
3. Run the spider using the following command: scrapy crawl nike -o output.json
Replace output.json with output.csv for CSV format.

## Project Structure

- nike_spider.py: Contains the Scrapy spider for scraping data from the Nike website.
- items.py: Defines the Scrapy item classes for storing scraped data.
- middlewares.py: Includes Scrapy middleware for handling Selenium requests.
- pipelines.py: Defines Scrapy pipelines for processing scraped data.

## Scraping Process
1. Selenium Chrome WebDriver is used to navigate to the Nike website and retrieve the page source.
2. Scrapy selectors are employed to parse the HTML and extract desired data such as clothing and male shoe information.
3. The scraped data is saved into JSON or CSV format using Scrapy's built-in functionalities.

## Conclusion
This project demonstrates how to scrape data from the Nike website using Scrapy and Selenium, effectively dealing with JavaScript-rendered content. By following the provided installation and usage instructions, you can customize and execute the web scraping process to suit your specific requirements. Feel free to contribute to this project by enhancing its functionalities or addressing any identified issues.

For any inquiries or suggestions, please contact foyinbo250@gmail.com. Thank you for your interest in this project!

### website view

![image](https://github.com/FaeyO/webscrapping-Nike-website/assets/118575325/51e7e08e-5a1b-4cd2-8303-a98a785b10a6)
