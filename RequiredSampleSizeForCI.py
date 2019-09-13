import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

run = 500 # run is the total number of sampling experiments.
ts = 10000 # ts is the number of time steps in a second.
SampleSize = [5, 10, 20, 40, 80, 160, 320]
# Each Element is the number of runs to simulate.
a = 0 # This is used to monitor the running process.
CorrectPercentageList = []

for n in SampleSize:
    print 'SampleSize =', SampleSize[a] # This is used to monitor the running process.
    a += 1
    CorrectEvents = 0
    b = 0 # This is used to monitor the running process.
    
    for sample in range(run):
        print 'run', range(run)[b] # This is used to monitor the running process.
        b += 1
        DistanceList = []
        for i in range(n):
            NumTimeSteps = 0
            NumSteps = 0
            Bound = True
    
            while Bound:
                NumTimeSteps += 1
                MtrStepDecider = np.random.randint(1, ts)
    
                if MtrStepDecider < 100: # Then the motor decides to step.
                    MtrDetachDecider = np.random.randint(1, ts)
    
                    if MtrDetachDecider >= 100: # The motor moves forward 1 step.
                        NumSteps += 1
                    else: # The motor falls off.
                        Bound = False
                        DistanceList.append(8*NumSteps)
                        
                else: # Then the motor decides to not step.
                    continue
    
        CI = st.t.interval(0.95, len(DistanceList)-1,
                      loc=np.mean(DistanceList), scale=st.sem(DistanceList))
        # Calculate the 95% Confidence Interval

        if CI[0] <= 800 <= CI[1]: # Detect whether expectation is in the CI.
            CorrectEvents += 1
        else:
            print CI

    CorrectPercentage = 100*CorrectEvents/run
    CorrectPercentageList.append(CorrectPercentage)

y_pos = np.arange(len(CorrectPercentageList))
plt.bar(y_pos, CorrectPercentageList, align='center', alpha=0.5)
plt.xticks(y_pos, SampleSize)
plt.xlabel('Sample Size')
plt.ylabel('Proportion of Correct Events/%')
plt.title('Bar Graph of Proportion of Correct Events against Sample Size')
for i, v in enumerate(CorrectPercentageList):
    plt.text(i, v, str(v), horizontalalignment='center')

plt.show()


