# Slcm-Reader
Obtain your attendance and marks from SLCM in a CLI without opening your browser. Output will be displayed on the terminal as well as written into a file.


### Requirements
* [Selenium](https://www.selenium.dev/)
* [Pandas](https://pandas.pydata.org/)


### Installation
Download selenium driver for chrome and add the path in the configure() function as follows: 
```python
driver = webdriver.Chrome("File/Path/chromedriver.exe", options=options) # example
```

On your terminal:
```terminal
pip install pandas selenium
```

### Working 

On your terminal go to the appropriate terminal and run the py file (Python3).
```terminal
python slcm.py
```
