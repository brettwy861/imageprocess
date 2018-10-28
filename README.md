# Screenshot and color analysis 
## [screenshot.py](./screenshot.py)
screenshot.py takes screenshots of webpages and stores to png files.
### Install
0. Install chrome browser (by default in /usr/bin)
1. ```pip install selenium```
2. Get latest release version ```VER=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)```
3. Get the zip for the driver ```wget https://chromedriver.storage.googleapis.com/$VER$/chromedriver_linux64.zip```
4. Unzip it ```unzip chromedriver_linux64.zip```
5. ```chmod +x chromedriver```
6. ```
   sudo mv -f chromedriver /usr/local/share/chromedriver
   sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
   sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
   ```
7. make sure chromedriver exist in /usr/bin/
8. configure urlList in screenshot.py or load from a local file
9. run this script with python screenshot.py

## [colorhist.py](./colorhist.py)
colorhist.py analyzes all png files in the current path, yielding major color components and their proportions and stores to a json file.

