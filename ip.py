import requests
import redis
import threading


def loadip():
    try:
        # for i in range(10):
        url = 'http://mvip.piping.mogumiao.com/proxy/api/get_ip_bs?appKey=895f827cc2144ef48e4bddb7e3e81ad8&count=10&expiryDate=0&format=1&newLine=2'
        req = requests.get(url)
        date = req.json()
        ipdate2 = date['msg']
        global ipdate
        ipdate = ipdate2
        print(ipdate)
    except:
        pass

    import redis
    client = redis.StrictRedis(host='localhost', port=6379, db=4)

    # 插入一个元素
    for x in ipdate:
        y = x['ip'] +':' + x['port']
        print(y)
        client.lpush('ip', y)
    print(client.lrange('ip', 0, -1))
    timer = threading.Timer(25, loadip)
    timer.start()


loadip()


def reip():
    client = redis.StrictRedis(host='localhost', port=6379, db=4)
    result = client.rpop('ip')
    print(result)
    timer = threading.Timer(2, reip)
    timer.start()


reip()