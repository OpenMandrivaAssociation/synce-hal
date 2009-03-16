%define svn		0
%define rel		3
%if %svn
%define release		%mkrel 0.%svn.%rel
%define distname	%name-%svn.tar.lzma
%define	dirname		%name
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.gz
%define dirname		%name-%version
%endif

Name:		synce-hal
Summary:	HAL-based connection framework for Windows Mobile
Version:	0.13.1
Release:	%{release}
License:	MIT
Source0:	%{distname}
Source1:	org.freedesktop.Hal.Device.Synce.conf
Patch0:		synce-hal-1.13.1-dbus.patch
URL:		http://synce.sourceforge.net/
Group:		Communications
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libsynce-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libgnet2-devel
BuildRequires:	hal-devel
BuildRequires:	bluez-devel
Requires:	ppp
Obsoletes:	synce-serial < 0.11.1
Obsoletes:	odccm < 0.11.2
Obsoletes:	synce-vdccm < 0.11
Obsoletes:	synce < 0.11.1
Provides:	synce = %{version}-%{release}

%description
Synce-hal is a connection framework and dccm-implementation for
Windows Mobile devices that integrates with HAL.

%prep
%setup -q -n %{dirname}
%patch0 -p2
cp %{SOURCE1} etc

%build
%if %svn
./autogen.sh
%endif

#fix ppp files location
sed -i s/"ip-up.d"/""/"" bluetooth/Makefile.am
sed -i s/"ip-down.d"/""/"" bluetooth/Makefile.am

#needed by patch0
aclocal -I m4
autoheader
libtoolize --copy --automake
automake --copy --foreign --add-missing
autoconf



%configure2_5x --enable-bluetooth-support
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%{_sysconfdir}/ppp/synce-bt-ipdown
%{_sysconfdir}/ppp/synce-bt-ipup
%{_sysconfdir}/ppp/peers/synce-bt-peer
%{_sysconfdir}/dbus-1/system.d/*.conf
%{_libexecdir}/hal*
%{_libexecdir}/synce*
%{_datadir}/hal/fdi/policy/20thirdparty/*
%{_datadir}/%{name}

