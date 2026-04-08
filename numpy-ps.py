# Setup
import numpy as np
import pandas as pd
import kagglehub
from numpy.ma.core import indices

# Live Coding 1
views = np.array([15000, 32000, 8500, 45000])
likes = np.array([1200, 3000, 800, 4100])
comments = np.array([150, 400, 50, 600])

# TODO:
# total_interactions = likes + comments
# engagement_rate = (total_interactions / views) * 100
# print(f"The engagement rate was{engagement_rate}")
# # indices = np.argwhere(engagement_rate == 9)
# # print(indices)
#
# # Guided Practice 1
# rpm = np.array([1.5, 2.0, 0.8, 2.5])
# production_cost = np.array([10, 30, 5, 50])
#
# # TODO:
# clean_revenue = (views/1000*rpm)-production_cost
# indice = np.argwhere(clean_revenue == max(clean_revenue) )
# print("income: ", np.round(clean_revenue, 2))
# print(indice)



# Live Coding 2
cpu_load = np.array([
    [45, 50, 55, 40, 48],  # Server 1
    [88, 92, 95, 89, 94],  # Server 2
    [20, 25, 22, 18, 30]   # Server 3
])

# TODO:
# mean_load = np.mean(cpu_load, axis =1)
# print("mean load is", mean_load)
# absolute_max_per_server = np.max(cpu_load, axis = 1)
# print("absolute max per server is", absolute_max_per_server)
# critical_load = cpu_load[cpu_load > 90]
# print("critical loads are", critical_load)
# print("count of accidents", critical_load.size)

# Guided Practice 2
pings = np.array([
    [45, 50, 48, 55],       # Server 1
    [120, 115, 210, 130],   # Server 2
    [300, 250, 310, 280],   # Server 3
    [15, 20, 18, 22]        # Server 4
])

# TODO:
min_response_time = np.min(pings, axis =1)
print("min response time is", min_response_time)
ping_greater_200 = pings[pings > 200]
print("ping_greater_200 is", ping_greater_200)
print(ping_greater_200.size)
print((ping_greater_200.size/pings.size)*100,"%")
average_response_time = np.mean(ping_greater_200)
print("average response time is", average_response_time)




# Live Coding 3
# kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026",
#                                   output_dir="datasets", force_download=True)
df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
# print(df.head())

# TODO: