# Slcm-Reader
Obtain your attendance and marks from SLCM in a CLI without opening your browser. Output will be displayed on the terminal as well as written into a file. (Marks not complete yet)


### Requirements
* [Selenium](https://www.selenium.dev/)
* [Pandas](https://pandas.pydata.org/)


### Installation
Download Selenium driver for [Chrome](https://chromedriver.chromium.org/downloads) or [Firefox](https://github.com/mozilla/geckodriver/releases) and add the path in the configure() function in slcm.py as follows: 
```python
driver = webdriver.Chrome("File/Path/chromedriver.exe", options=options) # example
```

On your terminal:
```terminal
pip install pandas selenium
```
##### Note: Change Chrome to Firefox in the configure() function in slcm.py code if Firefox is opted instead of Chrome.

### Working 

On your terminal go to the appropriate directory and run the py file (Python3).
```terminal
python slcm.py
```
