%define svn		0
%define rel		5
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
Version:	0.14
Release:	%{release}
License:	MIT
Source0:	%{distname}
Source1:	org.freedesktop.Hal.Device.Synce.conf
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

%build
%if %svn
./autogen.sh
%endif

%configure2_5x --enable-bluetooth-support --with-hal-addon-dir=%{_libexecdir}/hal/scripts
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -Dpm644 %{buildroot}%{_sysconfdir}/ppp/ip-up.d/synce-bt-ipup \
%{buildroot}/%{_sysconfdir}/ppp/synce-bt-ipup
install -Dpm644 %{buildroot}%{_sysconfdir}/ppp/ip-down.d/synce-bt-ipdown \
%{buildroot}/%{_sysconfdir}/ppp/synce-bt-ipdown
rm -rf %{buildroot}%{_sysconfdir}/ppp/{ip-up.d,ip-down.d}

%clean
rm -rf %{buildroot}

%post

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%{_sysconfdir}/ppp/synce-bt-ipdown
%{_sysconfdir}/ppp/synce-bt-ipup
%{_bindir}/synce-unlock.py
%{_sysconfdir}/ppp/peers/synce-bt-peer
%{_sysconfdir}/dbus-1/system.d/*.conf
%{_libexecdir}/hal/scripts/hal-synce*
%{_libexecdir}/synce-serial-chat
%{_libexecdir}/hal-dccm
%{_datadir}/hal/fdi/policy/20thirdparty/*
%{_datadir}/%{name}

