#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Library to implement Unicode algorithms for line and word breaking
Summary(pl.UTF-8):	Biblioteka z implmentacją algorytmów Unicode do łamania wierszy i słów
Name:		libunibreak
Version:	6.1
Release:	1
License:	Zlib
Group:		Libraries
#Source0Download: https://github.com/adah1972/libunibreak/releases
Source0:	https://github.com/adah1972/libunibreak/releases/download/libunibreak_6_1/%{name}-%{version}.tar.gz
# Source0-md5:	8df410d010e03de1a339a400a920335e
URL:		https://github.com/adah1972/libunibreak
BuildRequires:	rpm-build >= 4.6
Obsoletes:	liblinebreak < 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libunibreak is an implementation of the line breaking and work
breaking algorithms as described in Unicode Standard Annex 14 and
Unicode Standard Annex 29.

%description -l pl.UTF-8
libunibreak to implementacja algorytmów łamania wierszy i łamania słów
zgodna z opisem w Unicode Standard Annex 14 oraz Unicode Standard
Annex 29.

%package devel
Summary:	Header files for libunibreak library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libunibreak
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	liblinebreak-devel < 2.2

%description devel
Header files for libunibreak library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libunibreak.

%package static
Summary:	Static libunibreak library
Summary(pl.UTF-8):	Statyczna biblioteka libunibreak
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	liblinebreak-static < 2.2

%description static
Static libunibreak library.

%description static -l pl.UTF-8
Statyczna biblioteka libunibreak.

%package apidocs
Summary:	API documentation for libunibreak library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libunibreak
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libunibreak library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libunibreak.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf libunibreak.so $RPM_BUILD_ROOT%{_libdir}/liblinebreak.so

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libunibreak.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENCE NEWS README.md
%attr(755,root,root) %{_libdir}/libunibreak.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libunibreak.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblinebreak.so
%attr(755,root,root) %{_libdir}/libunibreak.so
%{_includedir}/eastasianwidthdef.h
%{_includedir}/graphemebreak.h
%{_includedir}/linebreak.h
%{_includedir}/linebreakdef.h
%{_includedir}/unibreakbase.h
%{_includedir}/unibreakdef.h
%{_includedir}/wordbreak.h
%{_pkgconfigdir}/libunibreak.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liblinebreak.a
%{_libdir}/libunibreak.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/{search,*.css,*.html,*.js,*.png}
