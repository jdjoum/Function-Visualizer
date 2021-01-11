import math
import pylab

def plot_function(s,xmin,xmax,numSamples):
    numPoints = 0
    ys = []
    # Array that will hold all the x values of the function
    xs = []
    xs.append(xmin)
    #print("\nxs array with only xmin:", xs)
    dx = (xmax - xmin) / numSamples
    print("\nThe dx value is going to be:",dx)
    while(numPoints < numSamples):
        numPoints += 1
        xs.append(xmin + dx*numPoints)
    #print("\nxs array with",numSamples," samples added:", xs)
    for x in xs:
        y = eval(s)
        ys.append(y)
    #print("\nys array with",numSamples," samples added:", ys)
    
    print("\nFunction Visualization Table:")
    for i in range(numSamples):
        if(i == 0):
            print("\n{:10s}    {:4s}".format("    x","    y"))
            print("------------------------")
        print("{:10f}    {:4f}".format(xs[i],ys[i]))
        i += 1
    
    print("\nFunction Visualization Graph:")
    pylab.title(s)
    pylab.plot(xs, ys, "bo-")
    pylab.xlabel("Inputs (X-Values)")
    pylab.ylabel("Outputs (Y-Values)")
    pylab.show()
myFunc = "2*math.sin(2*math.pi*x)"
fun_str = input("Enter a function that uses variable x: ")
n = int(input("Enter the number of samples that you want: "))
min = int(input("Enter the minimum x-value: "))
max = int(input("Enter the maximum x-value: "))
plot_function(fun_str,min,max,n)
