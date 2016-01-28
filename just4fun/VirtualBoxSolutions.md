# Solve Small Resolution problem in VirtualBox

Sometimes the resolution of the guest machine in VirtualBox does not detect the proper size. To solve it, do the following in the guest machine:

```
sudo apt-get install virtualbox-guest-dkms virtualbox-guest-utils
```

Remove the useless libcheese

```
sudo apt-get remove libcheese-gtk23
```

Install the Xserver Core

```
sudo apt-get install xserver-xorg-core
```

Finally install Guest X11 for VirtualBox

```
sudo apt-get install -f virtualbox-guest-x11
```

Reboot VirtualBox