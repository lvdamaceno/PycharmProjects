import redis

r = redis.StrictRedis(host='localhost', port=6379,
                      charset="utf-8", decode_responses=True)

a = [0, 1, 1, 2, 3, 5, 8, 13]
b = [0, 1, 1, 2, 3]

r.set('X', a)
r.set('Y', b)

value = r.get('X')

print(value)

