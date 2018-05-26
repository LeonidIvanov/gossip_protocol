#  Gossip (epidemic) protocol simulation

In simulate.py you'll find two realization of gossip or epidemic protocol simulation.

You can run it from the shell using

`./simulate.py`

Also you can use:
    -n to set number of nodes, default = 20
    -i to set number of simulation iterations, default = 1000
    -x to set number of random nodes selected each step, default = 4
    --gossip-protocol-advanced to use advanced protocol

`./simulate.py -n 40 -i 500 -x 2 --gossip-protocol-advanced`