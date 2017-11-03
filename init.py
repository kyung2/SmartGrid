import math
'''
data {
    'app': 'name',
    'power': double,
    'duration': number,
    'start': number,
    'end': number,
    'opt': iter
}
'''
#get File data
def getData():
    f = open("./data.txt", 'r')
    dataSet = []
    maxDuation = 0

    while True:
        app = f.readline()[:-1]
        if not app: break
        
        power = float(f.readline())
        duration = math.ceil(int(f.readline()) / 60)
        start = int(f.readline())
        end = int(f.readline())
        
        data = {\
            'app': app,
            'power': power,
            'duration': duration,
            'start': start,
            'end': end,
            'opt': combinations2(list(range(1,25)),duration)
        }
        dataSet.append(data)
        print(data)

        if maxDuation < data['duration']:
            maxDuation = data['duration']
    
    f.close()
    return dataSet

#Combination lib
def combinations2(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))    
    cycles = list(range(n, n-r, -1))
    
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(list(range(r))):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return