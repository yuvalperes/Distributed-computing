Consensus protocols in the population model (https://en.wikipedia.org/wiki/Population_protocol). We implement the repeated majority protocol (see <a href="https://github.com/yuvalperes/Distributed-computing/blob/master/consensus_repeated_majority.py">python program here</a>). More details below:

Model: there are n nodes, each with some bounded amount of memory s. Initially each node has a belief bit in {0, 1} and the goal is to reach a state where each node has the belief equal to the initial majority bit. The nodes can communicate in a distributed fashion: at each point in time (discrete time units), a node i is selected uniformly at random. If the node wants to communicate, it gets matched with a random other node j and they exchange memory states. Otherwise, if i does not want to communicate, it can update its state by itself. Note this model is equivalent to having each node equipped with a Poisson clock with a unit rate (when the clock of a node i rings, the node wakes up and can communicate as described above).

The goal is to design protocols that achieve consensus (i.e. the initial majority) with high probability. 
Here we implement the simple repeated majority protocol which only requires three memory states and has been extensively studied (see references below). 

Briefly, the system dynamics are: each node keeps track of a state which is either 0, 1, or ?. Initially each node has state 0 or 1. In each round, a node gets selected uniformly at random and is matched with a random other node. The nodes that get matched exchange state and update their own state based on this communication. Let U, V, and S represent, respectively, the set of nodes storing 0, 1, and ?
    - If a  node in U (resp. V) contacts a node in U, S (resp. V, S), then it does not update its value. 
    - If a node in U (resp. V) contacts a node in V (resp. U), it updates its value to ? (resp. ?).  
    - If a  node in S contacts a node in U (resp. V), then it updates it’s value to 1 (resp. 0). 
    
Some images from the simulation with the fraction of correct (left) and wrong (right) nodes over time. The remaining nodes have the "?" state.

![Correct Nodes](https://github.com/yuvalperes/Distributed-computing/blob/master/correct_fraction_n%3D1000.png)

![Wrong Nodes](https://github.com/yuvalperes/Distributed-computing/blob/master/wrong_fraction_n%3D1000.png)

- <a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2008-114.pdf">Using Three States for Binary Consensus on Complete Graphs</a>, by Etienne Perron, Dinkar Vasuvedan, Milan Vojnovic
- <a href="http://www.cs.yale.edu/homes/aspnes/papers/approximate-majority-journal.pdf">A Simple Population Protocol for Fast Robust Approximate Majority</a>, by Dana Angluin, James Aspnes, David Eisenstat

