import sys, os, time, datetime
import numpy as np

mode = sys.argv[1]
c = sys.argv[2]
ip = sys.argv[3]


print('MODE : %s'%mode)
print('IP : %s'%ip)

NUM_COMMUNICATION_ROUNDS = 1000
NUM_TRAINERS = 2


print("-"*85)
print('|{:^10s}|{:^21s}|{:^50s}|'.format('ROUND','TIME','STATUS'))
print("-"*85)

for r in range(NUM_COMMUNICATION_ROUNDS):
    while not os.path.exists('../conventional_FL_MQ/src/trainer_storage/aggregator_models/model_ep%d.h5'%r):
        time.sleep(1)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('|{:^10d}|{:^21s}|{:^50s}|'.format(r,now,'Start training aggregated model %d'%r))
    while not os.path.exists('../conventional_FL_MQ/src/trainer_storage/trainer_models/trainer%s_ep%d.h5'%(c,r)):
        time.sleep(1)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('|{:^10d}|{:^21s}|{:^50s}|'.format(r,now,'Complete training aggregated model %d'%r))
    print("-"*85)