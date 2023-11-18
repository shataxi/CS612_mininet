import argparse
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import Controller
from mininet.log import setLogLevel, info

def emptyNet():

    #initialise parser
    parser=argparse.ArgumentParser()
    #optional argument
    parser.add_argument("--config")
    parser.add_argument("--scheme")
    parser.add_argument("--loss")
    #read arguments from command line
    args=parser.parse_args()
    scheme,link_loss = '',0
    if args.loss==1 or args.loss==3:
        link_loss=args.loss
    else:
        print('loss can be either 1 or 3, pass --loss 1 or --loss 3, if loss option is not passed or incorrect argument is given loss is set to zero')
    if args.scheme=='vegas':
        print('congestion control scheme is  vegas')
        scheme='-Z vegas'
    if args.scheme=='reno':
        print('congestion control scheme is  reno')
        scheme='-Z reno'
    if args.scheme=='cubic':
       print('congestion control scheme is cubic')
       scheme='-Z cubic'
    if args.scheme=='bbr':
        print('congestion control scheme is bbr')
        scheme='-Z bbr'

    "Create an empty network and add nodes to it."
    #TCLink for configuring the link for traffic control
    net = Mininet( controller=Controller, waitConnected=True ,link=TCLink)

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1' )

    info( '*** Creating links\n' )
    net.addLink( h1, s1)
    net.addLink( h2, s1 )

#link 2
    info( '*** Adding hosts\n' )
    h3 = net.addHost( 'h3', ip='10.0.0.3' )
    h4 = net.addHost( 'h4', ip='10.0.0.4' )

    info( '*** Adding switch\n' )
    s2 = net.addSwitch( 's2' )

    info( '*** Creating links\n' )
    net.addLink( h3, s2 )
    net.addLink( h4, s2 ,port1=5001)

#link1--#link2

    net.addLink(s1,s2,loss=link_loss)
    info( '*** Starting network\n')
    net.start()

    #running server on h4 using iperf
    print('Nodes in the link ****----****',net.hosts[0],net.hosts[1],net.hosts[2],net.hosts[3])
    serv=net.hosts[3]
    client1=net.hosts[0]
    client2=net.hosts[1]
    client3=net.hosts[2]

    host1=serv.popen('iperf -s')


    if args.config=='b':
       print('h1 is client and h4 is server')
       host2=client1.popen('iperf -c {0} -p 5001 -t 30 {1}'.format(serv.IP(),scheme))
       host2.wait()

    elif args.config=='c':
       print('h1,h2,h3 are client and h4 is server')
       host2=client1.popen('iperf -c {0} -p 5001 -t 30 {1}'.format(serv.IP(),scheme))
       host3=client2.popen('iperf -c {0} -p 5001 -t 30 {1}'.format(serv.IP(),scheme))
       host4=client3.popen('iperf -c {0} -p 5001 -t 30 {1}'.format(serv.IP(),scheme))
       host2.wait()
       host3.wait()
       host4.wait()
    else:
       print('--config takes arguments b and c only, pass --config b or --config c')

    host1.terminate()

    info( '*** Stopping network' )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()

