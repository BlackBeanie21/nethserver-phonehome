Summary: NethServer phone-home
Name: nethserver-phonehome
Version: 1.0.1
Release: 1
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-base

BuildRequires: perl
BuildRequires: nethserver-devtools 

%description
NethServer simple phone-home software.

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%config(noreplace) %attr(644,root,root) /etc/sysconfig/phone-home 

%changelog
* Fri Dec 19 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
- Phone Home: generate uuid  - Bug #2988 [NethServer]

* Tue Dec 16 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- First release of phone home - Feature #2975 [NethServer]

