#IO多路复用
#   select
#       直接调用操作系统的IO接口，它监控sockets,open files, and pipes(所有带fileno()方法的文件句柄)何时变成readable 和writeable, 或者通信错误
#       文件描述符(fd)被放在一个数组中，然后select调用的时候遍历这个数组，如果对于的文件描述符可读则会返回改文件描述符。当遍历结束之后，如果仍然没有一个可用设备文件描述符，select让用户进程则会睡眠，直到等待资源可用的时候在唤醒，遍历之前那个监视的数组。每次遍历都是线性的
import socket
import select

sk1 = socket.socket()
sk1.bind(('127.0.0.1', 8080))
sk1.listen(3)

inputs = [sk1, ]
outputs = []
message_dict = {}

while True:
    '''
    select中第1个参数表示:所有的输入的data,就是指外部发过来的数据
    select中第2个参数表示:监控和接收所有要发出去的data
    select中第3个参数表示:错误信息
    select中第4个参数表示:1秒监听一次
    r_list中的socket连接代表有数据可接收(recv),所有在w_list中的存放着你可以对其进行发送(send)操作的socket连接，当连接通信出现error时会把error写到e_list列表中
    '''
    r_list, w_list, e_list = select.select(inputs, outputs, inputs, 1)  #select阻塞进程，同时监听服务器socket和获得的客户端socket, 直到inputs中的socket被触发
    print('正在监听的socket对象%d' % len(inputs))
    print(r_list)
    for sk1_or_conn in r_list:
        #每一个连接对象
        if sk1_or_conn == sk1:      #如果是服务端socket被触发(监听到有客户端连接服务器)
            # 表示有新用户来连接
            conn, address = sk1_or_conn.accept()
            inputs.append(conn)     #inputs加入客户端socket
            message_dict[conn] = []
        else:       #当客户端发送数据时，客户端socket被触发，r_list返回客户端socket  
            # 表示有老用户发消息了
            data_bytes = sk1_or_conn.recv(1024)
            if data_bytes:
                # 如果用户终止连接
                inputs.remove(sk1_or_conn)
                message_dict[sk1_or_conn].put(data_bytes)
                if sk1_or_conn not in outputs:
                    outputs.append(sk1_or_conn)
            else:
                if sk1_or_conn in outputs:
                    outputs.remove(sk1_or_conn)  #既然客户端都断开了，我就不用再给它返回数据了，所以这时候如果这个客户端的连接对象还在outputs列表中，就把它删掉
                inputs.remove(sk1_or_conn)    #inputs中也删除掉
                sk1_or_conn.close()
    #w_list中的socket，也有几种状态，如果这个客户端连接在跟它对应的message_dict里有数据，就把这个数据取出来再发回给这个客户端，否则就把这个连接从outputs中移除，这样下一次循环select()调用时检测到outputs中没有这个连接，那就会认为这个连接还处于非活动状态
    for conn in w_list:
        recv_str = message_dict[conn][0]
        del message_dict[conn][0]
        conn.sendall(bytes(recv_str+'好', encoding='utf-8'))
        outputs.remove(conn)
    #如果在跟某个socket连接通信过程中出了错误，就把这个连接对象在inputs\outputs\message_dict中都删除，再把连接关闭掉
    for sk in e_list:
        inputs.remove(sk)
        if sk in outputs:
            outputs.remove(sk)
        sk.close()
        del message_dict[sk][0]