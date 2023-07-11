# Instructions for Ubuntu/Debian (self-hosted):

1. Generate the .env file from the template

```
cp .env.example .env
```

2. open the .env file with any text editor (e.g nano)

```
nano .env
```

3. change required values with your respective ones (at least one server info should be added).

```
BOT_API_TOKEN = YOUR_BOT_API_TOKEN                      **required**
CHAT_ID = YOUR_DESIRED_CHAT_ID                          **required**

SERVER0_API = http://example.data.com/Path/panel/       **required**
SERVER0_USERNAME = server0_username                     **required**
SERVER0_PASSWORD = server0_password                     **required**
SERVER0_CAPTION = server0_caption                       *optional*

SERVER1_API = http://example1.notIranian.shop/panel/    *optional*
SERVER1_USERNAME = server1_username                     *optional*
SERVER1_PASSWORD = server1_username                     *optional*
SERVER1_CAPTION = server1_caption                       *optional*

SERVER2_API = http://optionalSecond.heaven.me/panel/    *optional*
...
...
...
```

4. install the requirements

```
pip install -r requirements.txt
```

5. run the application

```
python3 main.py
```

**or** set a cronjob to run it periodically, [tutorial for setting cronjob here](https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e).
