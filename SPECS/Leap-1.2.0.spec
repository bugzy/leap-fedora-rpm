%define _topdir %(pwd)
%define _builddir %{_topdir}/BUILD
%define _rpmdir %{_topdir}/RPMS
%define _sourcedir %{_topdir}/SOURCES
%define _specdir %{_topdir}/SPECS
%define _srcrpmdir %{_topdir}/SRPMS

%define __os_install_post %{nil}
%define __jar_repack 0
%define debug_package %{nil}
%define __arch_install_post /usr/lib/rpm/check-buildroot
%define __find_provides %{nil}
%define __find_requires %{nil}
%define _use_internal_dependency_generator 0
Autoprov: 0
Autoreq: 0

Summary: Leap Motion re-packaging.
Name: Leap
Release: 10943%{?dist}
Version: 1.2.0
BuildArch: %{_target_cpu}
License: LeapMotion
Group: System Environment/Daemon
URL: http://www.leapmotion.com/
Source0: %{name}
BuildRoot: %{_topdir}/%{name}-root
Requires: qt5-qtbase qt5-qtwebkit qt5-qtscript qt5-qtsensors qt5-qtmultimedia qt5-qtlocation
%description
Leap Motion RPM package.
More info at http://www.leapmotion.com/.

%prep
%{__mkdir_p} %{_srcrpmdir}
%{__mkdir_p} %{_builddir}
%{__mkdir_p} %{_srcrpmdir}
%{__mkdir_p} %{_rpmdir}
%{__mkdir_p} %{_builddir}/%{name}-%{version}
%if "%{_target_cpu}" == "x86_64"
%{__cp} %{_sourcedir}/%{name}-%{version}-x64.deb %{_builddir}/
%else
%{__cp} %{_sourcedir}/%{name}-%{version}-x86.deb %{_builddir}/
%endif
%{__cp} -r %{_sourcedir}/%{name}-%{version}/* %{_builddir}/%{name}-%{version}/

%setup -T -D

%build
cd %{_builddir}/
%if "%{_target_cpu}" == "x86_64"
%{__ar} p %{name}-%{version}-x64.deb data.tar.gz | %{__tar} zx
%else
%{__ar} p %{name}-%{version}-x86.deb data.tar.gz | %{__tar} zx
%endif
%{__mkdir_p} %{_builddir}/%{name}-%{version}/etc/udev/rules.d/
%{__cp} lib/udev/rules.d/25-com-leapmotion-leap.rules %{_builddir}/%{name}-%{version}/etc/udev/rules.d/
%{__cp} -r usr %{_builddir}/%{name}-%{version}/
echo %{_build_vendor}

%install
%{__mkdir} -p $RPM_BUILD_ROOT
%if "%{_target_cpu}" == "x86_64"
%{__mv} %{_builddir}/%{name}-%{version}/%{_exec_prefix}/lib %{_builddir}/%{name}-%{version}/%{_libdir}
%endif
%{__cp} -r %{_builddir}/%{name}-%{version}/* $RPM_BUILD_ROOT
export NO_BRP_CHECK_RPATH=true

%post
groupadd plugdev
usermod -a -G plugdev root
ln -s /lib/systemd/system/leap.service /etc/systemd/system/leap.service
systemctl daemon-reload

%postun
groupdel plugdev
rm -f /etc/systemd/system/leap.service

%clean
%{__rm} -rf %{_srcrpmdir}/*
%{__rm} -rf %{_builddir}/*
%{__rm} -rf $RPM_BUILD_ROOT/*

%files
%defattr(-,root,root,-)
%{_bindir}/LeapControlPanel
%{_bindir}/Recalibrate
%{_bindir}/Visualizer
%{_bindir}/platforms
%{_sbindir}/leapd
%{_libdir}/Leap
%{_datarootdir}/Leap
/etc/udev/rules.d/25-com-leapmotion-leap.rules
/lib/systemd/system/leap.service

%doc

%changelog
* Fri Apr 25 2014 - bugzylittle@gmail.com
- Leap updated package definition (spec file) for 1.2.x.
* Fri Dec 23 2013 - bugzylittle@gmail.com
- Leap updated package definition (spec file) for 1.1.2.
* Fri Nov 01 2013 - bugzylittle@gmail.com
- Leap updated package definition (spec file).
* Mon Aug 10 2013 - alexis.tejeda@gmail.com
- BuildArch based on the host cpu arch, disabled rpath check, added dist to the release.
* Mon Aug 05 2013 - alexis.tejeda@gmail.com
- Leap initial package definition (spec file).