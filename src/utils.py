import numpy as np


def pulse2distance(pulse, width=0.375, cycle=2):
    '''
    pulse: 1からはじめて観測終了までのパルス数をリスト化したもの
    width: モータが1パルス駆動したときのマウスの移動幅(mm)
    cycle: 1パルス動かすためにかかる時間(msec)
    '''
    maxpulse = np.max(pulse)
    maxdistance = maxpulse * width
    dist = [maxdistance - width * d for d in pulse]
    return dist
