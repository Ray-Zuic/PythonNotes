import numpy as np
from datetime import datetime
#import matplotlib.pyplot as plt


# 门店数据 csv 的链接
url = 'https://media-image1.baydn.com/storage_media_image/uyacwn/e04073523393bb3ef5d467e4eca4b041.459e953d18224934e714f594aa5142de/%E6%98%9F%E5%B7%B4%E5%85%8B%E9%97%A8%E5%BA%97%E6%95%B0%E6%8D%AE%E8%A1%A8.csv'
# 读取门店数据 csv
data = np.genfromtxt(url, delimiter=',', dtype=None, encoding='utf8')

start_time = np.array([datetime.strptime(t,"%H:%M:%S")for t in data[1:,3]])

end_time = np.array([datetime.strptime(t,"%H:%M:%S")for t in data[1:,4]])

hours = np.array([(t.total_seconds()/60/60) for t in (end_time-start_time)])

labels = ['≥14 小时','12-14 小时之间','10-12 小时之间','小于 10 小时']
result = [
    len(hours[hours>=14]),
    len(hours(hours >= 12) & (hours<14)),
    len(hours[hours >= 10] & (hours<12)),
    len(hours[hours<10])
]

#plt.pie(reult.labels=labels,autopct='%0.1f%%')
#plt.show()