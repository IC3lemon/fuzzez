# fuzzez

***
PPT - https://www.canva.com/design/DAGBh2oqDeU/WULS7LlvxEOvD_v8kVjOzA/edit?utm_content=DAGBh2oqDeU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton



Ight so listen chumps

## main Shit

> `fuzzez/launchapp.py` is the main app ka file, it has all the juice.\
> `fuzzez/main.py` is the ui juice.\
> `fuzzez/send_kernel.yml` sends the shit to ansible.
> `fuzzez/ansi/configs/` contains individual yml files which on execution with ansi fuzz those individual modules

## pending tasks

1.
> ### fuzz according to module selected.
> ![image](https://github.com/IC3lemon/fuzzez/assets/150153966/0d3cc06a-1f5d-463b-9519-6704b20fe7c5)
> 
> according to option selected it executes the corresponding configs ka yml file on the webserver

2.
> ### scrape syzkaller website and update ui.
```python
def scrapeAndShowResults(self):
  print("show this shi")
  print("need the ips and shi")
  '''
  driver.get("{ip1}")  #coverage
  r = driver.find_elements_by_xpath("//table[@class= 'spTable']/tbody/tr")
  c = driver.find_elements_by_xpath("//*[@class= 'spTable']/tbody/tr[3]/td")
  rc = len (r)'''
```
>the commented lines currently not working, selenium for firefox gay, might need Prashant.
```python
    driver_path = "\geckodriver.exe"
    driver = webdriver.Firefox(driver_path)
```
`driver = webdriver.Firefox(driver_path)` getting an error here mainly
