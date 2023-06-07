from internetSpeed import InternetSpeedTwitterBot
import time

botInstance = InternetSpeedTwitterBot()
botInstance.get_speed()
time.sleep(30)
botInstance.tweet_at_provider()






