import numpy as np
import matplotlib.pyplot as plt

n = 1000 # n is the number of runs to simulate.
ts = 10000 # ts is the number of time steps in a second.
DistanceList = []
VelocityList = []

for i in range(n):
    NumTimeSteps = 0
    NumSteps = 0
    Bound = True

    while Bound:
        NumTimeSteps += 1
        MtrStepDecider = np.random.randint(1, ts+1)

        if MtrStepDecider <= 100: # Then the motor decides to step.
            MtrDetachDecider = np.random.randint(1, ts+1)

            if MtrDetachDecider > 100: # The motor moves forward 1 step.
                NumSteps += 1
            else: # The motor falls off.
                Bound = False
                DistanceList.append(8*NumSteps)
                VelocityList.append(10000*(8*NumSteps)/(NumTimeSteps))

        else: # Then the motor decides to not step.
            continue

print np.mean(DistanceList)
print np.mean(VelocityList)
NumBins = 10

plt.figure(1)
n, bins, patches = plt.hist(DistanceList, NumBins)
plt.xlabel('Distances nm')
plt.ylabel('Number of Appearance')
plt.title('Histogram of Motor Moving Distances')

plt.figure(2)
n, bins, patches = plt.hist(VelocityList, NumBins)
plt.xlabel('Velocities nm/s')
plt.ylabel('Number of Appearance')
plt.title('Histogram of Motor Moving Velocities')
plt.show()
