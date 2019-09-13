import numpy as np
import matplotlib.pyplot as plt

n = 200 # n is the number of runs to simulate.
ts = 10000 # ts is the number of time steps in a second.
DistanceList = []
VelocityList = []

for i in range(n):
    print 'run', i # This is used to monitor the process.
    NumTimeSteps = 0
    NumSteps = 0
    Bound1 = True
    Bound2 = False
    Mtr2 = True

    while Bound1 or Bound2: # The cargo is still on the MT.
        NumTimeSteps += 1
        MtrStepDecider1 = np.random.randint(1, ts+1)
        MtrStepDecider2 = np.random.randint(1, ts+1)

        if Bound1:
            if MtrStepDecider1 <= 100: # Then motor1 decides to step.
                MtrDetachDecider1 = np.random.randint(1, ts+1)

                if MtrDetachDecider1 > 100: # Motor1 moves forward 1 step.
                    Mtr2 = False
                    NumSteps += 1
                else: # Motor1 falls off.
                    Bound1 = False
                    Mtr2 = True
        else:
            MtrRebindDecider1 = np.random.randint(1, ts+1)
            if MtrRebindDecider1 <= 2: # Motor1 rebinds to MT.
                Bound1 = True

        if Bound2:
            if MtrStepDecider2 <= 100: # Then motor2 decides to step.
                MtrDetachDecider2 = np.random.randint(1, ts+1)

                if MtrDetachDecider2 > 100: # Motor2 moves forward 1 step.
                    if Mtr2: # This avoids the cargo moves 2 steps in 1 time step.
                        NumSteps += 1
                else: # Motor2 falls off.
                    Bound2 = False
        else:
            MtrRebindDecider2 = np.random.randint(1, ts+1)
            if MtrRebindDecider2 <= 2: # Motor2 rebinds to MT.
                Bound2 = True

        if not Bound1 and not Bound2: # Both motor fall off.
            DistanceList.append(8*NumSteps)
            VelocityList.append(10000*(8*NumSteps)/(NumTimeSteps))

print 'Mean distance is', np.mean(DistanceList)
print 'Mean velocity is', np.mean(VelocityList)
