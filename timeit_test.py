import timeit
from tuneup import main as test


t = timeit.Timer(stmt=test)
results = t.repeat(repeat=7, number=3)
min_value = min([result/3 for result in results])


print('Best time accross 7 repeats of 3 runs per repeat: ', min_value)
