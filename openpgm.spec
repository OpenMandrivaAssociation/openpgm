%define api 5.2
%define major   0
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

%global version_main      %{api}
%global version_dash_main 5-2
%global version_dash      %{version_dash_main}-122
%global name_alias        pgm

Name:          openpgm
Version:       5.2.122
Release:       15
Summary:       An implementation of the PGM reliable multicast protocol
Group:         System/Libraries
# The license is LGPLv2.1
License:       LGPLv2
# New URL is https://github.com/steve-o/openpgm
# The files are now on https://code.google.com/archive/p/openpgm/downloads
URL:           https://github.com/steve-o/%{name}
Source0:       https://github.com/steve-o/%{name}/archive/release-%{version_dash}.tar.gz#/%{name}-%{version}.tar.gz
# All the following patches have been submitted upstream
# as a merge request: https://github.com/steve-o/openpgm/pull/64
Patch2:        openpgm-02-c-func.patch
Patch3:        openpgm-03-pkgconfig.patch
Patch4:        openpgm-04-py-version-gen.patch
Patch5:        openpgm-05-fix-setgid.patch

%description
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.

%package -n     %{libname}
Summary:        An implementation of the PGM reliable multicast protocol
Group:          System/Libraries

%description -n %{libname}
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.


%package -n	%{develname}
Summary:       Development files for openpgm
Group:         Development/C
Requires:      %{libname} = %{version}-%{release}

%description -n	%{develname}
This package contains OpenPGM related development libraries and header files.


%prep
%setup -q -n %{name}-release-%{version_dash}/%{name}/pgm
%autopatch -p3

libtoolize --force --copy
aclocal
autoheader
automake --copy --add-missing
autoconf

%build
%configure
%make_build

%install
%make_install

mv -f %{buildroot}%{_includedir}/%{name_alias}-%{version_main}/%{name_alias} %{buildroot}%{_includedir}/

%files -n	%{libname}
%doc COPYING LICENSE
%{_libdir}/*%{api}.so.%{major}*

%files -n	%{develname}
%doc examples/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/openpgm-5.2.pc
