

Consensus protocols in the population model (https://en.wikipedia.org/wiki/Population_protocol). We implement the repeated majority protocol. More details below:

Model: there are n nodes, each with some bounded amount of memory s. Initially each node has a belief bit in {0, 1} and the goal is to reach a state where each node has the belief equal to the initial majority bit. The nodes can communicate in a distributed fashion: at each point in time (discrete time units), a node i is selected uniformly at random. If the node wants to communicate, it gets matched with a random other node j and they exchange memory states. Otherwise, if i does not want to communicate, it can update its state by itself. Note this model is equivalent to having each node equipped with a Poisson clock with a unit rate (when the clock of a node i rings, the node wakes up and can communicate as described above).

The goal is to design protocols that achieve consensus (i.e. the initial majority) with high probability. 
Here we implement the simple repeated majority (with three states of memory) protocol which has been extensively studied:

-- Using Three States for Binary Consensus on Complete Graphs: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2008-114.pdf, by Etienne Perron, Dinkar Vasuvedan, Milan Vojnovic
-- A Simple Population Protocol for Fast Robust Approximate Majority: http://www.cs.yale.edu/homes/aspnes/papers/approximate-majority-journal.pdf, by Dana Angluin, James Aspnes, David Eisenstat

