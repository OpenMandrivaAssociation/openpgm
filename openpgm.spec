%define	api	5.2
%define	major	0
%define oldlib	%mklibname %{name} %{api}
%define olddev	%mklibname -d %{name} %{api}
%define	oname	pgm
%define	libname	%mklibname %{oname} %{api} %{major}
%define	devname	%mklibname -d %{oname} %{api}

Name:		openpgm
Version:	5.2.122
Release:	7
Summary:	An implementation of the PGM reliable multicast protocol

Group:		System/Libraries
License:	LGPLv2.1+
URL:		http://openpgm.googlecode.com/
Source0:	http://openpgm.googlecode.com/files/libpgm-%{version}~dfsg.tar.gz
BuildRequires:	python

%description
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.

%package -n	%{libname}
Summary:	An implementation of the PGM reliable multicast protocol
Group:		System/Libraries
%rename		%{oldlib}

%description -n	%{libname}
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.

%package -n	%{devname}
Summary:	Development files for openpgm
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
%rename		%{olddev}

%description -n %{devname}
This package contains OpenPGM related development libraries and header files.

%prep
%setup -q -n libpgm-%{version}~dfsg/openpgm/pgm

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/lib%{oname}-%{api}.so.%{major}*

%files -n %{devname}
%doc LICENSE
%doc examples/
%{_includedir}/%{oname}-%{api}
%{_libdir}/lib%{oname}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
