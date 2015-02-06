Summary:	Country-to-IPs generator. Geographic IP generator for IPv4 networks
Name:		geoipgen
Version:	0.4
Release:	3
License:	BSD
Group:		Networking/Other
URL:		http://www.morningstarsecurity.com/research/geoipgen
Source0:	http://geoipgen.googlecode.com/files/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	ruby
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GeoIPgen is a country-to-IPs generator. It's a geographic IP generator for IPv4
networks that uses the MaxMind GeoLite Country database. Geoipgen is the first
published use of a geographic ip database in reverse to translate from
country-to-IPs instead of the usual use of IP-to-country.

%prep

%setup -q

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 geoipgen %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README INSTALL
%{_bindir}/geoipgen



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-2mdv2011.0
+ Revision: 610829
- rebuild

* Tue Mar 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdv2010.1
+ Revision: 517049
- import geoipgen


* Tue Mar 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdv2010.0
- initial Mandriva package
