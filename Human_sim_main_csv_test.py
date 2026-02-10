#代码之神保佑我不要出bug
#我要用最笨的办法，不是不会优化，而是我思路还没好，现在优化脑子要炸
import random
import csv
human = []
couple = []
#property_human: [sex, age, married, died]

#marriage rate
marriage_rate = 0.54

#birth rate
birth_rate = 1.15

#death rates
death_rate_0_10 = 0.73
death_rate_10_20 = 0.35
death_rate_20_30 = 0.55
death_rate_30_40 = 0.9
death_rate_40_50 = 2.35
death_rate_50_60 = 5.18
death_rate_60_70 = 13.5
death_rate_70_80 = 51.1
death_rate_80_90 = 100

def death(human_property):
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
    a = random.randint(0,10000)
    if a <= dr*100:
        human_property[-1] = 1
    return human_property

def marriage():
    waiting_couple_list_male = []
    waiting_couple_list_female = []
    for a in human:
        if 20<a[1]<40 and a[-1] == 0 and a[-2] == 0: #判断年龄，结婚情况，以及生死情况
            r = random.randint(0, 10000)
            if 20 < a[1] <= 25:
                marriage_rate = 15.2
            if 25 < a[1] <= 30:
                marriage_rate = 37.24
            if 30 < a[1] <= 35:
                marriage_rate = 20.72
            if 35 < a[1] <= 40:
                marriage_rate = 9.14
            if r <= marriage_rate * 100:
                #判断性别加入待定列表
                a[-2] == 1
                if a[0] == 0:
                    waiting_couple_list_female.append(a)
                else:
                    waiting_couple_list_male.append(a)
    #进行结婚匹配，完全没有人权
    for i in range(min(len(waiting_couple_list_male), len(waiting_couple_list_female))-1):

        couple.append([waiting_couple_list_female[i], waiting_couple_list_male[i], 0])

def get_children():
    for a in couple:
        female_age = a[0][1]
        male_age = a[1][1]
        avg_age = (male_age + female_age) / 2
        if 25<= avg_age <= 38:
            if a[-1] == 0:
                r = random.randint(0, 10000)
                if r <= birth_rate * 100:
                    #birth
                    human.append([random.randint(0,1), 0, 0, 0])
                    a[-1] += 1

#__main__
sim_ppl = 140000000
for i in range(sim_ppl):
    human.append([random.randint(0,1), random.randint(0, 90), 0, 0])
sim_years = 100
#按年模拟
with open('data.csv', mode='w', newline='') as file:
    writer
for i in range(sim_years):
    population = 0
    #执行死亡惊喜礼包
    #for a in human:
     #   a = death(a)
    #执行结婚
    marriage()
    #执行生育
    get_children()
    for a in human:
        if a[-1] == 0:
            population += 1

    #print(population)
female_population = 0
male_population = 0
for a in human:
    if a[-1] == 0:
        if a[0] == 0:
            female_population += 1
        if a[0] == 1:
            male_population += 1
print()
print(female_population)
print(male_population)
print(len(human))
#print(human)