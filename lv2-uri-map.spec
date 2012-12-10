%define extname uri-map
%define debug_package %{nil}

Name:           lv2-%{extname}
Version:        1.4
Release:        2
Summary:        LV2 %{extname} extension

Source:         http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
URL:            http://lv2plug.in/ns/extensions/%{extname}/
License:        ISC
Group:          System/Libraries
BuildRequires:  waf
BuildRequires:  pkgconfig
Requires:       lv2core

%description
This extension defines an interface that can be used in LV2 plugins and
hosts to create %{extname}s in plugins.

%package    devel
Summary:    Development files for the LV2 %{extname} extension
Group:      Development/C
Requires:   %{name} = %{version}
Requires:   lv2core-devel

%description    devel
This package contains development files for the LV2 %{extname} extension.


%files
%defattr(-,root,root,-)
%{_libdir}/lv2/%{extname}.lv2/manifest.ttl
%{_libdir}/lv2/%{extname}.lv2/%{extname}.ttl

%files devel
%{_includedir}/lv2/lv2plug.in/ns/ext/%{extname}
%{_libdir}/lv2/%{extname}.lv2/%{extname}.h
%{_libdir}/pkgconfig/lv2-lv2plug.in-ns-ext-%{extname}.pc

%prep
%setup -q

%build
./waf configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}
./waf

%install
rm -rf %{buildroot}

./waf install --destdir=%{buildroot}


%clean
rm -rf %{buildroot}


%changelog
* Tue Apr 17 2012 Frank Kober <emuse@mandriva.org> 1.4-2
+ Revision: 791519
- fixed build arch which is not noarch

* Sun Feb 19 2012 Frank Kober <emuse@mandriva.org> 1.4-1
+ Revision: 777517
- imported package lv2-uri-map

