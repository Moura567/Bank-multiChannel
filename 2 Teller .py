import random
import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt

# Lists
Arrival_T_D = []
Arrival_T_O = []
Start_Service_T_D = []
Start_Service_T_O = []
Waiting_T_D = []
Waiting_T_O = []
Completion_T_D = []
Completion_T_O = []
Total_T_in_System_D = []
Total_T_in_System_O = []
Service_T_D = []
Service_T_O = []
Inter_Arrival_T_O = []
Inter_Arrival_T_D = []
ord_cust = []
dist_cust = []
Idle_T1 = []
Idle_T2 = []


def generateinterArrivalO():
    xo = random.randint(1, 100)
    if 0 < xo <= 9:
        return 0
    if 9 < xo <= 26:
        return 1
    if 26 < xo <= 53:
        return 2
    if 53 < xo <= 73:
        return 3
    if 73 < xo <= 88:
        return 4
    if 88 < xo <= 100:
        return 5


def generateinterArrivalD():
    xd = random.randint(1, 10)
    if xd == 1:
        return 1
    if 1 < xd <= 3:
        return 2
    if 3 < xd <= 6:
        return 3
    if 7 < xd <= 10:
        return 4


def genearteServiceOrdinary():
    yo = random.randint(1, 100)
    if 0 < yo <= 20:
        return 1
    if 20 < yo <= 60:
        return 2
    if 60 < yo <= 88:
        return 3
    if 88 < yo <= 100:
        return 4


def genearteServiceDistinguished():
    yo = random.randint(1, 100)
    if 0 < yo <= 10:
        return 1
    if 10 < yo <= 40:
        return 2
    if 40 < yo <= 78:
        return 3
    if 78 < yo <= 100:
        return 4


for i in range(10):
    c = np.random.randint(1, 100)
    if 0 < c <= 60:
        ord_cust.append("Ordinary")
    if 60 < c < 100:
        dist_cust.append("Distinguished")
# inter_arrival_time for Distinguished
for i in range(len(dist_cust)):
    if dist_cust[i] == "Distinguished":
        a = generateinterArrivalD()
        Inter_Arrival_T_D.append(a)
for i in range(len(ord_cust)):
    if ord_cust[i] == "Ordinary":
        a = generateinterArrivalD()
        Inter_Arrival_T_O.append(a)
# service_time for Distinguished
for i in range(len(dist_cust)):
    if dist_cust[i] == "Distinguished":
        b = genearteServiceDistinguished()
        Service_T_D.append(b)
for i in range(len(ord_cust)):
    if ord_cust[i] == "Ordinary":
        b = genearteServiceDistinguished()
        Service_T_O.append(b)

x = len(dist_cust)
# TELLER OF Distinguished
for i in range(x):
    # first customer
    if i == 0:
        Inter_Arrival_T_D[0]=0
        Arrival_T_D.append(0)
        Start_Service_T_D.append(0)
        Waiting_T_D.append(0)
        Idle_T1.append(0)
        Completion_T_D.append(Start_Service_T_D[i] + Service_T_D[i])
        Total_T_in_System_D.append(Completion_T_D[i] - Arrival_T_D[i])
    else:
        Arrival_T_D.append(Arrival_T_D[i - 1] + Inter_Arrival_T_D[i])
        Start_Service_T_D.append(max(Arrival_T_D[i], Completion_T_D[i - 1]))
        Waiting_T_D.append(Start_Service_T_D[i] - Arrival_T_D[i])
        Completion_T_D.append(Start_Service_T_D[i] + Service_T_D[i])
        Total_T_in_System_D.append(Completion_T_D[i] - Arrival_T_D[i])

y = len(ord_cust)
for i in range(y):
    if i == 0:
        Inter_Arrival_T_O[0]=0
        Arrival_T_O.append(0)
        Start_Service_T_O.append(0)
        Waiting_T_O.append(0)
        Idle_T2.append(0)
        Completion_T_O.append(Start_Service_T_O[i] + Service_T_O[i])
        Total_T_in_System_O.append(Completion_T_O[i] - Arrival_T_O[i])
    else:
        Arrival_T_O.append(Arrival_T_O[i - 1] + Inter_Arrival_T_O[i])
        Start_Service_T_O.append(max(Arrival_T_O[i], Completion_T_O[i - 1]))
        Waiting_T_O.append(Start_Service_T_O[i] - Arrival_T_O[i])
        Completion_T_O.append(Start_Service_T_O[i] + Service_T_O[i])
        Total_T_in_System_O.append(Completion_T_O[i] - Arrival_T_O[i])
for i in range(x):
    if i == 0:
        Idle_T1[0] = 0
    else:
        m = Arrival_T_D[i] - Completion_T_D[i - 1]
        if m < 0:
            Idle_T1.append(0)
        else:
            Idle_T1.append(m)

for i in range(y):
    if i == 0:
        Idle_T2[0] = 0
    else:
        m = Arrival_T_O[i] - Completion_T_O[i - 1]
        if m < 0:
            Idle_T2.append(0)
        else:
            Idle_T2.append(m)

AvgWT1 = sum(Waiting_T_D) / x
AvgWT2 = sum(Waiting_T_O) / y
MaxWT1 = max(Waiting_T_D)
MaxWT2 = max(Waiting_T_O)
Count_Wait_more_than_1min = 0
Count_Wait_General = 0
Count_Wait_more_than_1min1 = 0
Count_Wait_General1 = 0

for i in range(x):
    if Waiting_T_D[i] > 1:
        Count_Wait_more_than_1min += 1
    if Waiting_T_D[i] > 0:
        Count_Wait_General += 1

for i in range(y):
    if Waiting_T_O[i] > 1:
        Count_Wait_more_than_1min1 += 1
    if Waiting_T_O[i] > 0:
        Count_Wait_General1 += 1

# probability of Waiting
Prob_of_Wait1M = (Count_Wait_more_than_1min / x)
Prob_of_Wait = (Count_Wait_General / x)
Prob_of_Wait1M1 = (Count_Wait_more_than_1min1 / y)
Prob_of_Wait1 = (Count_Wait_General1 / y)
t = PrettyTable(['Customer', 'Type_of_cust', 'inter_arrival_time', 'arrival_time', 'waiting_time', 'start_Service_time',
                 'service_time',
                 'compl_time', 'total_t_in_system', "Idle_Time"])
for i in range(x):
    t.add_row(
        [(i + 1), dist_cust[i], round(Inter_Arrival_T_D[i], 2), round(Arrival_T_D[i], 2), round(Waiting_T_D[i], 2),
         round(Start_Service_T_D[i], 2), round(Service_T_D[i], 2),
         round(Completion_T_D[i], 2), round(Total_T_in_System_D[i], 2), round(Idle_T1[i], 2)])
print(t)

print("Number Of Customers Waited in teller 1: ", Count_Wait_General)
print("probability of waiting time in teller 1: " + str(Prob_of_Wait * 100) + "%")
print("Number Of Customers Waited More Than 1 Minute in teller 1: ", Count_Wait_more_than_1min)
print("probability of waiting more than 1 minute in teller 1: " + str(Prob_of_Wait1M * 100) + "%")
print("Average waiting time in teller 1: ", round(AvgWT1, 2), "Min")
print("Maximum waiting time in teller 1: ", round(MaxWT1, 2), "Min")
plt.hist(Inter_Arrival_T_D, density=True, bins=30)
plt.ylabel('prob of I_A_T')
plt.xlabel('Values of I_A_T')
plt.show()

plt.hist(Arrival_T_D, density=True, bins=30)
plt.ylabel('prob of A_T')
plt.xlabel('Values of A_T')
plt.show()

plt.hist(Waiting_T_D, density=True, bins=30)
plt.ylabel('prob of W_T')
plt.xlabel('Values of W_T')
plt.show()

plt.hist(Service_T_D, density=True, bins=30)
plt.ylabel('prob of S_T')
plt.xlabel('Values of S_T')
plt.show()

plt.hist(Completion_T_D, density=True, bins=30)
plt.ylabel('prob of C_T')
plt.xlabel('Values of C_T')
plt.show()

plt.hist(Total_T_in_System_D, density=True, bins=30)
plt.ylabel('prob of T_I_S')
plt.xlabel('Values of T_I_S')
plt.show()

t1 = PrettyTable(
    ['Customer', 'Type_of_cust', 'inter_arrival_time', 'arrival_time', 'waiting_time', 'start_Service_time',
     'service_time',
     'compl_time', 'total_t_in_system', "Idle_Time"])
for i in range(y):
    t1.add_row([(i + 1), ord_cust[i], round(Inter_Arrival_T_O[i], 2), round(Arrival_T_O[i], 2), round(Waiting_T_O[i], 2),
               round(Start_Service_T_O[i], 2), round(Service_T_O[i], 2),
               round(Completion_T_O[i], 2), round(Total_T_in_System_O[i], 2), round(Idle_T2[i], 2)])

print(t1)
print("Number Of Customers Waited in teller 2: ", Count_Wait_General1)
print("probability of waiting time in teller 2: " + str(Prob_of_Wait1 * 100) + "%")
print("Number Of Customers Waited More Than 1 Minute in teller 2: ", Count_Wait_more_than_1min1)
print("probability of waiting more than 1 minute in teller 2: " + str(Prob_of_Wait1M1 * 100) + "%")
print("Average waiting time in teller 2: ", round(AvgWT2, 2), "Min")
print("Maximum waiting time in teller 2: ", round(MaxWT2, 2), "Min")
plt.hist(Inter_Arrival_T_O, density=True, bins=30)
plt.ylabel('prob of I_A_T')
plt.xlabel('Values of I_A_T')
plt.show()

plt.hist(Arrival_T_O, density=True, bins=30)
plt.ylabel('prob of A_T')
plt.xlabel('Values of A_T')
plt.show()

plt.hist(Waiting_T_O, density=True, bins=30)
plt.ylabel('prob of W_T')
plt.xlabel('Values of W_T')
plt.show()

plt.hist(Service_T_O, density=True, bins=30)
plt.ylabel('prob of S_T')
plt.xlabel('Values of S_T')
plt.show()

plt.hist(Completion_T_O, density=True, bins=30)
plt.ylabel('prob of C_T')
plt.xlabel('Values of C_T')
plt.show()

plt.hist(Total_T_in_System_O, density=True, bins=30)
plt.ylabel('prob of T_I_S')
plt.xlabel('Values of T_I_S')
plt.show()
