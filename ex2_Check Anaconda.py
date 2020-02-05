import numpy as np
# score = [10,50,60,80,90]
score = [50, 60, 80]
print("평균:{}, 분산:{}, 표준편차:{}".format(np.mean(score), np.var(score), np.std(score)))