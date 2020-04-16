#### 面试题：进程和线程的区别和联系？
1. 进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
2. 线程 - 操作系统分配CPU的基本单位

#### 并发编程的优势：
1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
2. 改善用户体验 - 让耗时间的操作不会造成程序的假死

#### 线程调度的实现：threading模块的Condition

#### 异步处理：Python 3通过asyncio模块和await和async关键字（在Python 3.7中正式被列为关键字）来支持异步处理
1. 第三方库：aiohttp库,它提供了异步的HTTP客户端和服务器，这个三方库可以跟asyncio模块一起工作，并提供了对Future对象的支持
2. async和await来定义异步执行的函数以及创建异步上下文
3. 当程序不需要真正的并发性或并行性，而是更多的依赖于异步处理和回调时，asyncio就是一种很好的选择
4. 如果程序中有大量的等待与休眠时，也应该考虑asyncio，它很适合编写没有实时数据处理需求的Web应用服务器

#### 其他用于处理并行任务的三方库：joblib、PyMP等
#### 实际开发中，提升系统的可扩展性和并发性通常有2种扩展方式：
1. 垂直扩展：增加单个节点的处理能力
2. 水平扩展：将单个节点变成多个节点

#### AMQP（高级消息队列协议）：重要的有：Apache的ActiveMQ、RabbitMQ等

#### 要实现任务的异步化，可以使用名为Celery的三方库:
1. Celery是Python编写的分布式任务队列，它使用分布式消息进行工作，可以基于RabbitMQ或Redis来作为后端的消息代理

#### Python中使用redis: 安装redis模块： pip3 install redis
1. 使用： import redis

#### Python中使用MongoDB：安装mongodb模块：pip3 install pymongo
1. MongoDB默认数据目录 /data/db ,需要提前创建；
2. bind_ip参数用来将服务绑定到指定的IP地址；
3. --port参数用来指定MongoDB的端口,默认是27017
4. 使用：from pymongo import MongoClient
5. 其他MongoDB库：使用MongoEngine这样的库来简化Python程序对MongoDB的操作；以异步I/O方式访问MongoDB的三方库motor

#### Python中使用Mysql:安装mysql模块：pip install pymysql
1. 使用：import pymysql
2. 使用 autocommit=True 参数在每次操作完SQL后自动提交
3. 查询：from pymysql.cursors import DictCursor
