import os
import time
import base64
from selenium import webdriver
from selenium.webdriver import ChromeOptions


def send_request(req_url):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
    driver.get(req_url)

    time.sleep(5)
    driver.execute_script("var canvas=document.getElementsByTagName('canvas')[0]; var image=canvas.toDataURL('image/png', 1.0); document.getElementsByTagName('canvas')[0].setAttribute('value', image);")
    content = driver.find_element_by_tag_name('canvas').get_attribute('value')
    driver.close()
    return content


def base_to_image(base_string):
    imgdata = base64.b64decode(base_string.partition(",")[2])
    filename = 'weather.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)


def main():
    response = send_request(req_url=url)
    if response is not None:
        print('Success')
        base_to_image(base_string=response)


if __name__ == '__main__':
    url = 'https://openweathermap.org/city/6058560'
    main()
