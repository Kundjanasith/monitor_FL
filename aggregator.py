import sys, os, time, datetime
import numpy as np

mode = sys.argv[1]
ip = sys.argv[2]


print('MODE : %s'%mode)
print('IP : %s'%ip)

NUM_COMMUNICATION_ROUNDS = 1000
NUM_TRAINERS = 2


print("-"*85)
print('|{:^10s}|{:^21s}|{:^50s}|'.format('ROUND','TIME','STATUS'))
print("-"*85)

for r in range(NUM_COMMUNICATION_ROUNDS):
    while not os.path.exists('../conventional_FL_MQ/src/aggregator_storage/aggregator_models/model_ep%d.h5'%r):
        time.sleep(1)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('|{:^10d}|{:^21s}|{:^50s}|'.format(r,now,'Aggregated model %d is ready'%r))

    flag = np.zeros(NUM_TRAINERS)
    c = 0
    while len(np.where(flag==1)[0]) != NUM_TRAINERS:
        if os.path.exists('../conventional_FL_MQ/src/aggregator_storage/trainer_models/trainer%d_ep%d.h5'%(c+1,r)) and flag[c] == 0:
            time.sleep(1)
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('|{:^10d}|{:^21s}|{:^50s}|'.format(r,now,'Received trained model %d from trainer %d'%(r,c+1)))
            flag[c] = 1
        else:
            c = (c + 1) % NUM_TRAINERS

    print('|{:^10d}|{:^21s}|{:^50s}|'.format(r,now,'Start aggregating model %d '%(r+1)))
    print("-"*85)

