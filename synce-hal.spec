%define svn		3519
%define rel		1
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
Version:	0.11.1
Release:	%{release}
License:	MIT
Source0:	%{distname}
URL:		http://synce.sourceforge.net/
Group:		Communications
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libsynce-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libgnet2-devel
BuildRequires:	hal-devel
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
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%post

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%{_libexecdir}/hal*
%{_libexecdir}/synce*
%{_datadir}/hal/fdi/policy/20thirdparty/*

