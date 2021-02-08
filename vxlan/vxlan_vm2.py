#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel,info

def vxlan():
    net = Mininet()

    info('*** Adding hosts\n')
    red2 = net.addHost('red2', ip='10.0.0.2', mac='00:00:00:00:00:02')
    blue2 = net.addHost('blue2', ip='10.0.0.2', mac='00:00:00:00:00:02')

    info('*** Adding switch \n')
    s2 = net.addSwitch('s2')

    info('*** Creating links\n')
    net.addLink(red2, s2)
    net.addLink(blue2, s2)

    info('*** Starting network\n')
    net.start()

    info('*** Running CLI\n')
    CLI(net)

    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    vxlan()

