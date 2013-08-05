%define _topdir %(pwd)
%define _builddir %{_topdir}/BUILD
%define _rpmdir %{_topdir}/RPMS
%define _sourcedir %{_topdir}/SOURCES
%define _specdir %{_topdir}/SPECS
%define _srcrpmdir %{_topdir}/SRPMS

%define __os_install_post %{nil}
%define __jar_repack 0

Summary: Leap Motion re-packaging.
Name: Leap
Release: x86.5300.f19
Version: 0.8.0
License: LeapMotion
Group: System Environment/Daemon
URL: http://www.leapmotion.com/
Source0: %{name}
BuildRoot: %{_topdir}/%{name}-root

%define _leap_release_arch x86

%description
Leap Motion RPM package.
More info at http://www.leapmotion.com/.

%prep
%{__mkdir} -p %{_srcrpmdir}
%{__mkdir} -p %{_builddir}
%{__mkdir} -p %{_srcrpmdir}
%{__mkdir} -p %{_rpmdir}
%{__mkdir} -p %{_builddir}/%{name}-%{version}
%{__cp} %{_sourcedir}/%{name}-%{version}-%{_leap_release_arch}.deb %{_builddir}/
%{__cp} -r %{_sourcedir}/%{name}-%{version}/* %{_builddir}/%{name}-%{version}/

%setup -T -D

%build
cd %{_builddir}/
ar p %{name}-%{version}-%{_leap_release_arch}.deb data.tar.gz | tar zx
%{__mkdir} -p %{_builddir}/%{name}-%{version}/etc/udev/rules.d/
%{__cp} lib/udev/rules.d/25-com-leapmotion-leap.rules %{_builddir}/%{name}-%{version}/etc/udev/rules.d/
%{__cp} -r usr %{_builddir}/%{name}-%{version}/


%install
%{__mkdir} -p $RPM_BUILD_ROOT
%{__cp} -r %{_builddir}/%{name}-%{version}/* $RPM_BUILD_ROOT

%post
groupadd plugdev
usermod -a -G plugdev root
ln -s /lib/systemd/system/leap.service /etc/systemd/system/leap.service
systemctl daemon-reload

%postun
groupdel plugdev

%clean
%{__rm} -rf %{_srcrpmdir}/*
%{__rm} -rf %{_builddir}/*
%{__rm} -rf $RPM_BUILD_ROOT/*

%files
%defattr(-,root,root,-)
/usr/bin/LeapControlPanel
/usr/bin/Recalibrate
/usr/bin/ScreenLocator
/usr/bin/Visualizer
/usr/bin/leapd
/usr/lib/Leap
/usr/share/Leap
/etc/udev/rules.d/25-com-leapmotion-leap.rules
/lib/systemd/system/leap.service

%doc

%changelog
* Mon Aug 05 2013 - alexis.tejeda@gmail.com
- Leap initial package definition (spec file).