import pika

connection = pika.BlockingConnection(pika.URLParameters('amqp://kvpcnezw:0Cwgl0IwHsxHPKobsZr3cvK8Q-c1A9ha@otter.rmq.cloudamqp.com/kvpcnezw'))
channel = connection.channel()


channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()