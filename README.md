# PYNES

These is the  undergrad project from José Rafael  Ferraz that implements
the core functions  of the NES  CPU (the APU and the second joystick control 
weren't being implemented).

We publish the code and the undergrad monography (in Portuguese only) to
allow  others to  learn more  about how  hardware emulation works. The  code
was  well   documented  on *doc/pynes.pdf*.


## Source Code

Inside _src_  we put the  emulator source  code and inside  _rom_ the
nestest.nes  ROM. This specific ROM validate  the  code  itself  (instructions
emulated, variables and so on). This binary was collected from the community.


## Requirements and Running

This code works with Python 2.7.11 and PyGame 1.9.2 (requirements.txt). 

To run the emulator:

`
$ python src/nesemulator.py rom/nestest.nes
`

Here we have the emulator running:

![running](https://raw.githubusercontent.com/condector/pynes/master/img/nesrunning.png)

and passing all tests:

![running](https://raw.githubusercontent.com/condector/pynes/master/img/nesrunningok.png)


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
