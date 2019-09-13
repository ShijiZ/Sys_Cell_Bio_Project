import numpy as np
import matplotlib.pyplot as plt

n = 200 # n is the number of runs to simulate.
ts = 10000 # ts is the number of time steps in a second.
Windows = [500, 1000, 2000, 4000, 10000]

VelocityVariation = []
Xticks = []
for window in Windows:

    VelocityList = []
    for i in range(n):
        NumTimeSteps = 0
        NumSteps = 0
        Bound = True

        while Bound and NumTimeSteps < window:
            # Make sure we only focus the observed window.
            NumTimeSteps += 1
            MtrStepDecider = np.random.randint(1, ts)

            if MtrStepDecider < 100: # Then the motor decides to step.
                MtrDetachDecider = np.random.randint(1, ts)

                if MtrDetachDecider >= 100: # The motor moves forward 1 step.
                    NumSteps += 1
                else:
                    Bound = False # The motor falls off.
                    VelocityList.append(10000*(8*NumSteps)/(NumTimeSteps))

            else: # Then the motor decides to not step.
                continue

        else:
            VelocityList.append(10000*(8*NumSteps)/(NumTimeSteps))

    VelocityVariation.append(np.var(VelocityList, ddof=1))
    Xticks.append(window*10**(-4))

y_pos = np.arange(len(VelocityVariation))
plt.bar(y_pos, VelocityVariation, align='center', alpha=0.5)
plt.xticks(y_pos, Xticks)
plt.xlabel('Windows/s')
plt.ylabel('Variations of Velocities')
plt.title('Bar Graph of Motor Moving Velocity Variations')
for i, v in enumerate(VelocityVariation):
    plt.text(i, v, str(int(v)), horizontalalignment='center')
plt.show()
