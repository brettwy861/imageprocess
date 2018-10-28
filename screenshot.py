"""
0. install chrome browser (by default in /usr/bin)
1. pip install selenium
2. get latest release version Ver = curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE 
3. wget https://chromedriver.storage.googleapis.com/$Ver$/chromedriver_linux64.zip
4. unzip chromedriver_linux64.zip
5. chmod +x chromedriver
6. sudo mv -f chromedriver /usr/local/share/chromedriver
   sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
   sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
7. make sure chromedriver exist in /usr/bin/
8. run this script with python screenshot.py
"""
from selenium import webdriver
import time


def take_screenshot(url, save_fn="capture.png"):
    DRIVER = 'chromedriver'
    # browser = webdriver.Firefox() # Get local session of firefox
    browser = webdriver.Chrome(DRIVER)
    browser.set_window_size(1440, 900)
    browser.get(url) # Load page
    #scroll down to the bottom and up to the top
    browser.execute_script("""
        (function () {
            var x = 0;
            var step = 100;
            window.scroll(0, 0);
            function f() {
                if (x < document.body.scrollHeight) {
                    x += step;
                    window.scroll(0, x);
                    setTimeout(f, 100);
                } else {
                    window.scroll(0, 0);
                    document.title += " scrolled";
                }
            }
            setTimeout(f, 500);
        })();
    """)
    
    for i in range(30):
        if "scrolled" in browser.title:
            break
        time.sleep(10)
    
    browser.execute_script(""" if (typeof(ulp_active_window_id) != "undefined") ulp_self_close();""")
    #browser.execute_script("""ulp_self_close();""")
    time.sleep(2)
    browser.save_screenshot(save_fn)
    browser.close()


if __name__ == "__main__":
    urlList = ['https://www.microsoft.com/','https://www.cnn.com/',
               'https://amazon.com/','https://hulu.com/', 'https://uber.com/','google.com','eos.io']
    
    for item in urlList:
        if item[0:4]=='http':
            url_main=item.split('//')[1].rstrip('/')
        else:
            url_main = item.rstrip('/')
        urlbreak = url_main.split('.')
        if len(urlbreak)==2:
            name = '_'.join(urlbreak)
        elif len(urlbreak)==3:
            name = '_'.join(urlbreak[1:])
        else:
            name = '_'.join(urlbreak)
            
        if item[0:4]!='http':
            URL = 'http://'+item
        else:
            URL = item
            
        take_screenshot(URL,name+'.png')
    