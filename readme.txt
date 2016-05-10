The following libraries are required to run the project and are to be installed by pip

- Selenium
- BeautifulSoup
- Requests

The following additional requirements are also to be satisfied

- Firefox WebDriver (inbuilt) or Chrome Webdriver (included with files) 
- Proxy is to be set from within the code by uncommenting the "setProxy(myproxy)" line (firefox only)
- In case the script returns a time out error because of slow internet, please increase the timeout time in the code


In case of webdrivers, some work well with Linux, while some with OS X, 
The given webdrivers were tested with linux and OS X only, so in case the Chrome version doesnt work please try using the firefox version.
Also in case of chrome, please change "chromedriver = '/Users/rohanlokeshsharma/Downloads/chromedriver'" to appropriate paths
Also in case of chrome ,proxy settings are not supported through the selenium library and have to be manually set.

ChromeDriver was used because of the huge performance gains over firefox, but has some problems handling form submissions.


Installation ---->

1. Selenium

pip install -U selenium

2.Beautiful Soup

pip install beautifulsoup

The project may run without the requests library