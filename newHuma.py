import pandas as pd
import random

file_path = 'your_file.xlsx'
df = pd.read_excel(file_path)
data_2d_list = df.values.tolist()
brList = []
for row in data_2d_list:
    birthrate = row[7]
    brList.append(birthrate)
    print(row)



#death rates
death_rate_0_10 = 0.73
death_rate_10_20 = 0.35
death_rate_20_30 = 0.55
death_rate_30_40 = 0.9
death_rate_40_50 = 2.35
death_rate_50_60 = 5.18
death_rate_60_70 = 13.5
death_rate_70_80 = 51.1
death_rate_80_90 = 70
death_rate_90_100 = 100

human = []
mid_age = 37
population_start = int(data_2d_list[-1][-1])
for i in range(int(population_start / 2)):
    human.append([random.randint(0,mid_age),random.randint(0,1)，random.randint(0,1)])
for i in range(int(population_start / 2)):
    human.append([random.randint(mid_age,90),random.randint(0,1),random.randint(0,1)])

def death(humanlist):
    del_list = []
    for human_property in humanlist:
        age = human_property[1]
        dr = 0
        if 0 <= age < 10:
            dr = death_rate_0_10
        if 10 <= age < 20:
            dr = death_rate_10_20
        if 20 <= age < 30:
            dr = death_rate_20_30
        if 30 <= age < 40:
            dr = death_rate_30_40
        if 40 <= age < 50:
            dr = death_rate_40_50
        if 50 <= age < 60:
            dr = death_rate_50_60
        if 60 <= age < 70:
            dr = death_rate_60_70
        if 70 <= age < 80:
            dr = death_rate_70_80
        if 80 <= age < 90:
            dr = death_rate_80_90
        if 90 <= age < 100:
            dr = death_rate_90_100

        a = random.randint(0,10000)

        if a <= dr*100:
            del_list.append(humanlist.index(human_property))

    del_list.sort()
    cnt = len(del_list)
    cnt2 = 0
    while True:
        humanlist.pop(del_list[cnt2])
        if cnt == 0:
            break
        cnt -= 1
        cnt2 += 1
    return humanlist

def fertality(humanlist):
    cnt_new = 0
    for a in humanlist:
        if a[1] == 0 and a[2] == 0:
            cnt_new += 1
    for a in range(int(cnt_new * br)):
        humanlist.append([0,random.randint(0,1),0])
    return humanlist

#__main__
for a in range(5):