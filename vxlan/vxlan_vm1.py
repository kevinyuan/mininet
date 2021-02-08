#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel,info

def vxlan():
    net = Mininet()

    info('*** Adding hosts\n')
    red1 = net.addHost('red1', ip='10.0.0.1', mac='00:00:00:00:00:01')
    blue1 = net.addHost('blue1', ip='10.0.0.1', mac='00:00:00:00:00:01')

    info('*** Adding switch \n')
    s1 = net.addSwitch('s1')

    info('*** Creating links\n')
    net.addLink(red1, s1)
    net.addLink(blue1, s1)

    info('*** Starting network\n')
    net.start()

    info('*** Running CLI\n')
    CLI(net)

    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    vxlan()

