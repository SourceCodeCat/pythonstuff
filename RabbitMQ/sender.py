import pika

connection = pika.BlockingConnection(pika.URLParameters('amqp://kvpcnezw:0Cwgl0IwHsxHPKobsZr3cvK8Q-c1A9ha@otter.rmq.cloudamqp.com/kvpcnezw'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!...again')
print(" [x] Sent 'Hello World!'")
connection.close()