import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
from google_books_api_wrapper.api import GoogleBooksAPI


def main(course_code):
    
    course_code = course_code.split()
    f_c_code = "+".join(course_code)
    url = "https://calendar.ualberta.ca/search_advanced.php?cur_cat_oid=39&search_database=Search&search_db=Search&cpage=1&ecpage=1&ppage=1&spage=1&tpage=1&location=33&filter%5Bkeyword%5D="+ f_c_code +"&filter%5Bexact_match%5D=1"
    """ driver = webdriver.Edge()
    driver.get(url) """


    response = requests.get(url)
    source_text = str(response.content)

    showCourse_index = source_text.find("showCourse")
    endOfShowCourse = source_text.find(")", showCourse_index)

    showCourse_code = source_text[showCourse_index:endOfShowCourse]
    catoid = showCourse_code[13:15]
    coid = showCourse_code[21:27]


    course_url = "https://calendar.ualberta.ca/preview_course_nopop.php?catoid=" + catoid + "&coid=" + coid
    course_driver = requests.get(course_url)

    course_driver_content = str(course_driver.content)

    descrip_index = course_driver_content.find("<strong>Description</strong><br> ") + len("<strong>Description</strong><br> ")
    endOfDescrip = course_driver_content.find("</p>", descrip_index)
    course_description = course_driver_content[descrip_index:endOfDescrip]

    # Create a new instance of the GoogleBooksAPI class
    google_books_api = GoogleBooksAPI()

    # Search for books using the API
    search_results = google_books_api.search_book("Python Programming")

    # Print the title and author of each book in the search results
    print(search_results.title)

if __name__ == "__main__":
    course_code = (sys.argv[1]).split()
    f_c_code = "+".join(course_code)
    print(main(f_c_code))