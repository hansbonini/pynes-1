# PYNES

This is a  graduation project from José Rafael  Ferraz that implements
all functionalities  related to  the CPU (not  have time  to implement
them APU and the second joystick control).

We publish the code and the graduation project (in Portuguese only) to
allow  others to  learn more  about how  emulation works,  and how  to
simulate  a   full  hardware.   The  code   was  well   documented  on
*doc/pynes.pdf*.



## Source Code

Inside _src_  we have all  emulator source  code and inside  _rom_ the
nestest.nes  ROM  used  to  validate  the  code  itself  (instructions
emulated, variables and so on). Also, a log file that was collected
from the community.


## Requirements and Running

This code works with Python 2.7.11 and PyGame 1.9.2 (requirements.txt). 

To run the emulator:

`
$ python src/nesemulator.py rom/nestest.nes
`

Here we have the emulator running:

![running](https://raw.githubusercontent.com/condector/pynes/img/nesrunning.png)

and passing all tests:

![running](https://raw.githubusercontent.com/condector/pynes/img/nesrunningok.png)


## Joystick Control Mapping


The control was mapped as table bellow:

    Joystick    |    Keyboard
    ____________|_____________
        A       |       a
        B       |       s
      Select    |    Space
      Start     |     Enter
        UP      |    UP Arrow
       Down     |    DOWN Arrow
       Left     |    LEFT Arrow
      Right     |    RIGHT Arrow

The ESC key shutdown the emulator.