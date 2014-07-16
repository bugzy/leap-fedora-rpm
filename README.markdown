leap-fedora-rpm
===============

## 2.0.3+17004 ##

![](http://oi62.tinypic.com/iqxvk2.jpg "")

# LeapMotion RPM package for Fedora. #

Since alien deb to RPM transformation does not work for fedora 19 and 20 (due package conflict) I've decided to make a RPM packaging for Leap binaries.

The RPM it's pretty basic, simple and flexible to be modified, by default master branch is for x86 and x64 branch for x64 arch.

## How to generate the RPM ##

Be sure to install first rpm tools packaging: 

<pre>
sudo yum install rpm-build rpm-build-libs
</pre>

Due license issues I can't provide the RPM packaged already, but it's pretty easy to do it!. It's necessary to have installed Make and rpm-build devel packages.

Go to https://developer.leapmotion.com/dashboard and download the binaries for Linux. Once you have the file, open a terminal in the folder where the file was downloaded and type/execute these lines:

### For x86 and x86_64 ###

Spec file will build for the host rpm builder architecture, e.g.: if my machine/OS is based on 32 arch, it will build it for i386, no independent branches.

<pre>
git clone git@github.com:atejeda/leap-fedora-rpm.git
tar xzf LeapDeveloperKit_<VERSION>+<RELEASE>_linux.tgz *.deb
mv LeapDeveloperKit_$LEAP_<VERSION>+<RELEASE>_linux/*.deb leap-fedora-rpm/SOURCES/
cd leap-fedora-rpm
make clean all
</pre>

Bear in mind that the code above can change depending on the version used, Leap SDK v1 was using another name convention (zip and unzipped folder).

## Install it ##

Generated RPM is located under RPMS folder, e.g.:

<pre>
sudo yum remove Leap # uninstal older package just in case
sudo yum install -y RPMS/`uname -p`/Leap-VERSION-RELEASE.*.`uname -p`.rpm
</pre>

## Using it ##

I've demonized the leapd binary, for start the daemon use systemctl, e.g.:

 *   Start the daemon: sudo systemctl start leap.service
 *   Stop it: sudo systemctl stop leap.service
 *   Get the status : sudo systemctl status leap.service
 *   Enable it: sudo systemctl enable leap.service

After start the daemon, if the lights of your leap are turned on, so far so good...

Binaries to execute:

 *   Visualizer
 *   Recalibrate
 *   LeapControlPanel
 
## Support? ##

If you want to use it, modify, extend it, follow the normal github workflow, means that must be fork it, merge it, or create a ticket if there's any bug.