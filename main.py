from a import process_hotel_data
from a import saveE
import time

while True:
    start_time = time.time()
    city_id = input("输入city_id,若输入多个请以逗号隔开:")  # 替换成你的城市ID
    city_id = city_id.split(',')
    city_id = [int(i) for i in city_id]
    # target_count = int(input("输入想要多少酒店信息："))  # 替换成你需要的最大页面数
    for i in city_id:
        print(i)
    # 调用处理酒店数据的函数
        process_hotel_data(i)
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f"Elapsed time for this iteration: {elapsed_time} seconds")
    done = input("是否继续？(y/n)")
    if done == 'n':
        break


