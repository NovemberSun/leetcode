from configparser import ConfigParser
import numpy as np
from collections import defaultdict
import os
#生成config对象
conf = ConfigParser()
#用config对象读取配置文件
dir = '/media/vv/E/Data/ACDC/training'
str_to_ind = {'DCM':0, 'HCM':1, 'MINF':2, 'NOR':3, 'RV':4}
ind_to_str = {}
d = defaultdict(list)
for k in str_to_ind.keys():
    ind_to_str[str_to_ind[k]] = k

for id in os.listdir(dir):
    id_path = os.path.join(dir,id)
    files = os.listdir(id_path)
    cfg_path = os.path.join(id_path, files[0])
    nfo = np.loadtxt(cfg_path, dtype=str, delimiter=': ')
    d[nfo[2,1]].append(id)

outfile=dir+'/pathology.txt'
fw = open(outfile,'w+')
fw.write(str(d))
fw.close()