Consensus protocols in the population model (https://en.wikipedia.org/wiki/Population_protocol). We implement the repeated majority protocol; python program available <a href="https://github.com/yuvalperes/Distributed-computing/blob/master/consensus_repeated_majority.py">here</a>. More details below:

Model: there are n nodes, each with some bounded amount of memory s. Initially each node has a belief bit in {0, 1} and the goal is to reach a state where each node has the belief equal to the initial majority bit. The nodes can communicate in a distributed fashion: at each point in time (discrete time units), a node i is selected uniformly at random. If the node wants to communicate, it gets matched with a random other node j and they exchange memory states. Otherwise, if i does not want to communicate, it can update its state by itself. Note this model is equivalent to having each node equipped with a Poisson clock with a unit rate (when the clock of a node i rings, the node wakes up and can communicate as described above).

The goal is to design protocols that achieve consensus (i.e. the initial majority) with high probability. 
Here we implement the simple repeated majority (with three states of memory) protocol which has been extensively studied - see papers below. Some images from the simulation with the fraction of correct and wrong nodes over time.

![Correct Nodes](https://github.com/yuvalperes/Distributed-computing/blob/master/correct_fraction_n%3D1000.png)

Fraction of incorrect nodes over time:
![Wrong Nodes](https://github.com/yuvalperes/Distributed-computing/blob/master/wrong_fraction_n%3D1000.jpg)

- <a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2008-114.pdf">Using Three States for Binary Consensus on Complete Graphs</a>, by Etienne Perron, Dinkar Vasuvedan, Milan Vojnovic
- <a href="http://www.cs.yale.edu/homes/aspnes/papers/approximate-majority-journal.pdf">A Simple Population Protocol for Fast Robust Approximate Majority</a>, by Dana Angluin, James Aspnes, David Eisenstat

