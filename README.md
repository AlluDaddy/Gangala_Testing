# Gangala_Testing
# WINDOWS
To install all the dependencies required to this code:
``` 
pip install -r requirements.txt 
```



The chromedriver is dependent on the version of the chrome.


To know the version of your chrome:

Go to Settings in chrome -> click on About chrome

![alt text](https://github.com/AlluDaddy/Gangala_Testing/blob/main/image.png?raw=true)

To install the Chrome driver:

open: https://chromedriver.chromium.org/downloads

Click on the corresponding CHROMEDRIVER as per the version of chrome.

![image](https://user-images.githubusercontent.com/60499478/123657865-d35bf580-d84e-11eb-87de-48883f889b0a.png)

Click on the corresponding link as per the software.

![image](https://user-images.githubusercontent.com/60499478/123658411-52e9c480-d84f-11eb-87f4-ec3b9365fd41.png)

After the downloading, copy the filepath and paste it in path variable (maintest.py file).

Example:  Path = "D:\Download(D)\chromedriver_win32 (1)\chromedriver.exe".

# LINUX

To install all the dependencies required to this code:

 ```
 pip3 install -r requirements.txt
 ```
 

The chromedriver is dependent on the version of the chrome.


To know the version of your chrome:

Go to Settings in chrome -> click on About chrome

![alt text](https://github.com/AlluDaddy/Gangala_Testing/blob/main/image.png?raw=true)

To install the Chrome driver:

open: https://chromedriver.chromium.org/downloads

Click on the corresponding CHROMEDRIVER as per the version of chrome.

![image](https://user-images.githubusercontent.com/60499478/123657865-d35bf580-d84e-11eb-87de-48883f889b0a.png)

Click on the corresponding link as per the software.

![image](https://user-images.githubusercontent.com/60499478/123658411-52e9c480-d84f-11eb-87f4-ec3b9365fd41.png)

Go to chromedriver path and run this command

```
sudo mv chromedriver /usr/bin/chromedriver
```

To re-check the path of chromedriver:
```
whereis chromedriver
```

In Linux, no need to mention the path of the chromedriver in the code. 

![image](https://user-images.githubusercontent.com/60499478/123985654-472f0700-d9e3-11eb-8de7-70a61402b013.png)





