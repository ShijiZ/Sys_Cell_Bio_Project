import numpy as np
import matplotlib.pyplot as plt

n = 200 # n is the number of runs to simulate.
ts = 10000 # ts is the number of time steps in a second.
Windows = [500, 1000, 2000, 4000, 10000]

Xticks = []
Chance = []
for window in Windows:
    NumObservation = 10000/window
    ChanceList = []

    for i in range(n):
        Frequency = 0

        for a in range(NumObservation):
            NumTimeSteps = 0
            NumSteps = 0
            Bound = True

            while Bound and NumTimeSteps < window:
                NumTimeSteps += 1
                MtrStepDecider = np.random.randint(1, ts)

                if MtrStepDecider < 100: # Then the motor decides to step.
                    MtrDetachDecider = np.random.randint(1, ts)

                    if MtrDetachDecider >= 100: # The motor moves forward 1 step.
                        NumSteps += 1
                    else:
                        Bound = False # The motor falls off.
                        Velocity = 10000*(8*NumSteps)/(NumTimeSteps)

                else: # Then the motor decides to not step.
                    continue

            else:
                Velocity = 10000*(8*NumSteps)/(NumTimeSteps)

            if Velocity >= 3600:
                Frequency += 1

        Frequency = float(Frequency) # Necessary for Python 2
        ChanceList.append(Frequency/NumObservation)

    Chance.append(np.mean(ChanceList))
    Xticks.append(window*10**(-4))

y_pos = np.arange(len(Chance))
plt.bar(y_pos, Chance, align='center', alpha=0.5)
plt.xticks(y_pos, Xticks)
plt.xlabel('Windows/s')
plt.ylabel('Chance')
plt.title('Bar Graph of the Chance of Observing at Least 3600 nm/sec Velocity \n'
          'at Least Once in 1 Second Interval')
for i, v in enumerate(Chance):
    plt.text(i, v, str(v), horizontalalignment='center')
plt.show()
