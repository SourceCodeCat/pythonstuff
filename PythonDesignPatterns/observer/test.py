from NewsPublisher import *
from SMSSubscriber import *
from EMAILSubscriber import *

if __name__== '__main__':
	news_publisher = NewsPublisher()
	SMSSubscriber(news_publisher)
	EMAILSubscriber(news_publisher)
	news_publisher.addNews("Hello Wrld!")
	news_publisher.notifySubscribers()	
