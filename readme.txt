Team Members: Shataxi Dubey & Disha Suthar
------------------------------------------


PART 1
------------------------------------------ 
ThreeNet.py is the source code for Part 1 of assignment

There are two parts of ThreeNet.py. 

In one part, there is default routing (d1->r1->r3->d6) say 'A' and in other part routing is changed (d1->r1->r2->r3->d6) say 'B'.

To choose between routing 'A' OR 'B', use option --routepath
 
For using default route i.e 'A', use sudo python3 threeNet.py --routepath default

For using different route i.e 'B', use sudo python3 threeNet.py --routepath delay


-------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------

PART 2
-------------------------------------------
TwoSwitchOneNet.py is the source code for Part 2 of assignment

Always run the file with config option.

--config option is necessary to pass. Other options --scheme & --loss are not always necessary to pass

Use --config option for choosing the clients 

1. If you want h1 to be client and h4 to be server and TCP connection between h1 and h4 only, pass 'b' in --config option

   sudo python3 twoSwitchOneNet.py --config b

2. If you want h1,h2,h3 to be client and h4 to be server and TCP connection between h1,h2,h3 and h4, pass 'c' in --config option

   sudo python3 twoSwitchOneNet.py --config c

Use --scheme option for choosing the congestion scheme

1. To set congestion scheme to 'vegas' with --config b

   sudo python3 twoSwitchOneNet.py --config b --scheme vegas

Use --loss option for choosing the loss percent

1. To set loss percent to 1 for config b

   sudo python3 twoSwitchOneNet.py --config b --loss 1

2. To set loss percent to 1 for config b and scheme vegas

   sudo python3 twoSwitchOneNet.py --config b --scheme vegas --loss 1
 



 