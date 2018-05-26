#!/usr/bin/env python
import argparse
from random import randint


def gossip_protocol(n=20, x=4):
    remaining_nodes = list(range(n))
    infected_nodes = [0]
    buffer = [0]
    g = 0
    while buffer:
        for j in range(x):
            random_node = remaining_nodes[randint(0, len(remaining_nodes) - 1)]
            if random_node not in infected_nodes:
                buffer.append(random_node)
                infected_nodes.append(random_node)
        buffer.pop()
        g += 1
    if len(infected_nodes) == n:
        print('Success, after {} iterations'.format(g))
        return 1
    else:
        print('Failure, after {} iterations'.format(g))
        return 0


def gossip_protocol_advanced(n=20, x=4):
    remaining_nodes = list(range(n))
    infected_nodes = [0]
    buffer = [0]
    i = 0
    while buffer:
        for j in range(x):
            if not remaining_nodes:
                break
            else:
                random_node = remaining_nodes[randint(0, len(remaining_nodes) - 1)]
                if random_node not in infected_nodes:
                    buffer.append(random_node)
                    infected_nodes.append(random_node)
                remaining_nodes.remove(random_node)
        buffer.pop()
        i += 1
    if len(infected_nodes) == n:
        print('Success, after {} iterations'.format(i))
        return 1
    else:
        print('Failure, after {} iterations'.format(i))
        return 0


def protocol_iterator(n, x, iterations, protocol=gossip_protocol):
    success_count = 0
    for i in range(iterations):
        success_count += protocol(n, x)
    print('In {}% cases all nodes received the packet'.format(success_count / iterations * 100))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help="Number of nodes you wish to simulate.", type=int)
    parser.add_argument('-i', help="Number of simulations you want to run", type=int)
    parser.add_argument('-x', help="Number of random nodes to use in one step", type=int)
    parser.add_argument('-a', '--gossip-protocol-advanced',
                        help="Run simulation using advanced protocol",
                        action="store_true",
                        )

    args = parser.parse_args()

    if args.gossip_protocol_advanced:
        protocol_iterator(n=args.n, x=args.x, iterations=args.i, protocol=gossip_protocol_advanced)
    else:
        protocol_iterator(n=args.n, x=args.x, iterations=args.i, protocol=gossip_protocol)
