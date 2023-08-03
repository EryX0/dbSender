import requests
import os
from telegram.ext import Application,CallbackContext
import datetime
import os
from dotenv import load_dotenv # pip install python-dotenv

load_dotenv()
env_vars = os.environ


async def sendDB(context: CallbackContext) -> None:
    session = requests.Session()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Proxy-Connection': 'keep-alive',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
    session.headers.update(headers)
    chat_id = env_vars['CHAT_ID']
    for i in env_vars:
        #pattern SERVER1_API, SERVER1_LOGIN, SERVER1_PASSWORD, SERVER1_CAPTION, SERVER2_API, SERVER2_LOGIN, SERVER2_PASSWORD, ...
        if i[-4:] == '_API':
            loginUrl = env_vars[i][:len(env_vars[i])-6] + 'login'
            user = env_vars[i[:-3] + 'USERNAME']
            password = env_vars[i[:-3] + 'PASSWORD']
            try : caption = env_vars[i[:-3] + 'CAPTION']
            except : caption = i[:-4] + ' Database'
            try : session.post(loginUrl, data = {'username': user, 'password': password}, timeout=30)
            except Exception as Error: 
                await context.bot.send_message(chat_id=chat_id, text='login failed at ' + str(datetime.datetime.now() + datetime.timedelta(hours=3.5)))
                print('Exception ' + type(Error).__name__ + ' Occured, logging exception :\n' + str(Error))
                continue
            dbUrl = env_vars[i][:len(env_vars[i])-6] + 'server/getDb'
            try : db = session.get(dbUrl, timeout=10)
            except Exception as Error:
                await context.bot.send_message(chat_id=chat_id, text='get database failed at ' + str(datetime.datetime.now() + datetime.timedelta(hours=3.5)))
                print('Exception ' + type(Error).__name__ + ' Occured, logging exception :\n' + str(Error))
                continue
            # send document to chat
            await context.bot.send_document(chat_id=chat_id,document=db.content, filename='x-ui.db', caption=caption)
            print('databases sent at ' + str(datetime.datetime.now() + datetime.timedelta(hours=3.5)))
    #exit code
    os._exit(0)
def main() -> None:
    """Run the bot."""
    app = Application.builder().token(env_vars["BOT_API_TOKEN"]).build()
    #run sendDB every two hours
    print("starting the application...)
    app.job_queue.run_once(sendDB, 15)
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
