# Tiny4WD-robot

## Introduction

This Tiny4WD robot is based on the robot designed by Brian Corteil, this robot was featured in 
[The Mag Pi issue 51](https://www.raspberrypi.org/magpi/issues/51/) which contrains build 
instructions.  Brian has also released the files for the chassis on his [GitHub site](https://github.com/Corteil/PiMag_Tiny_The_Robot).  If you would prefer not to source each individual part, the Tiny4WD
is now available at [Pimoroni](https://shop.pimoroni.com/products/coretec-tiny-4wd-robot-rover)

I am using the [Rock Candy](http://amzn.to/2oNFBCr) PS3 controller which connected to the Raspberry Pi
with a dedicated 2.4MHz dongle, the Pi thinks this is a wired controller, all the pairing is done directly
between the dongle and the joypad, so we don't have to worry about this at all.

To interface the Rock Candy Controller I used the input library by Tom Oinn called [approxeng.input](https://approxeng.github.io/approxeng.input/index.html)
This is a really neat librarry and currently supports a number of controllers includng the Rock Candy.  When I started using this library it was designed for Python2, however I prefer to use Python3.  I contacted Tom and
he very kindly updated the library and it is now python2 and python3 compatable.

The motor controller I am using is the 4Tronix [Picon Zero motor controller](https://4tronix.co.uk/store/index.php?rt=product/product&product_id=552)
4Tronix provided some sample library code, but I wrote my own library class with Motor and Robot instances.  This 
is documented in my [GitHub repo](https://github.com/keithellis74/Picon-Zero)

## The build
So I downloaded the laser cut files and got them cut at [Ipswich Makerspace](http://ipswichmakerspace.com), bolted
on the 4 micro metal gear motors (I used 50:1 ratio) to the base plate.  Bolted the Raspberry Pi Zero to the 
top plate, connected the jumper wires to the motors and then bolted the top and bottom plates together using
4 No. 50mm stand-offs.

To power the robot I used a 2000mAh lipo battery along with an [Adafruit Power Boost 500C](https://learn.adafruit.com/adafruit-powerboost-500-plus-charger/overview).
This is an expensive but clever device.  It takes the input from a 3.7v lipo and boosts it up to 5v, I use this 5v
to power the Raspberry Pi.  The Power Boost also has a micro USB socket which can be used to charge the battery.
The Power Boost has a number of break out pins, one of which allows a switch to be connected to power down the 
output of the Power Boost.

The Picon Zero motor controller board has a number of power options.

* To power the board itself, it needs 5v, this can be supplied directly from the Raspberry Pi or from the on 
board micro USB socket
* The motors can be feed from the boards 5v supply, (which is either from the Pi or the seperate USB socket) 
or from a seperate terminal block.

I chose to power the PiCon Zero board from the Pi, which is fed from the Power Boost 500C.  The motors will are 
fed from the terminal blocks which I wired up directly to the 3.7v of the lipo battery. 

For a demo of the Tiny4WD robot see my Introduction [YouTube video](https://youtu.be/eh4GcPFB2xY)
