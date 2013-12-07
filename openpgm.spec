%define major	5
%define minor	2
%define libname %mklibname %{name} %{major}.%{minor}
%define devname %mklibname -d %{name} %{major}.%{minor}

Name:          openpgm
Version:       5.2.122
Release:       5
Summary:       An implementation of the PGM reliable multicast protocol

Group:         System/Libraries
# The license is LGPLv2.1
License:       LGPLv2
URL:           http://openpgm.googlecode.com/
Source0:       http://openpgm.googlecode.com/files/libpgm-%{version}~dfsg.tar.gz
BuildRequires: python

%description
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.

%package -n     %{libname}
Summary:        An implementation of the PGM reliable multicast protocol
Group:          System/Libraries

%description -n %{libname}
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.

%package -n    %{devname}
Summary:       Development files for openpgm
Group:         Development/C
Requires:      %{libname} = %{version}-%{release}

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
%{_libdir}/*.so.*

%files -n %{devname}
%doc COPYING LICENSE
%doc examples/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/openpgm-5.2.pc
