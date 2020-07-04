import os
import time
import cairo
import rsvg
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from reportlab.graphics import renderPDF, renderPM


def send_request(req_url):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
    driver.get(req_url)

    time.sleep(5)
    content = driver.find_element_by_class_name('highcharts-root').get_attribute('outerHTML')
    driver.close()
    return content


def get_png(data):
    img = cairo.ImageSurface(cairo.FORMAT_ARGB32, 640, 480)
    ctx = cairo.Context(img)
    handle = rsvg.Handle(None, data)
    handle.render_cairo(ctx)
    img.write_to_png("save.png")


def main():
    response = send_request(req_url=url)
    if response is not None:
        print(response)
        get_png(data=response)


if __name__ == '__main__':
    url = 'https://openweathermap.org/city/6058560'
    main()
