import time

for x in range(2, 6):
    print('Sleep {} seconds..'.format(x))
    time.sleep(x)  # "Sleep" for x seconds
print('Done!')
