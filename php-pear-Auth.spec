%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - PHP PEAR authentication class
Summary(pl):	%{_pearname} - klasa dla PHP PEAR z klasami uwierzytelniaj±cymi
Name:		php-pear-%{_pearname}
Version:	1.2.3
Release:	3.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1506c2a27afe85e8d56eaa8466b6f13a
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/Auth/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1.3
BuildRequires:	php-zlib
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Auth package provides methods for creating an authentication
system using PHP.

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet PEAR::Auth dostarcza metody do stworzenia systemu
uwierzytelniania u¿ywaj±cego PHP.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/%{_class}
%patch0 -p2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
cp -a ./%{php_pear_dir}/{.registry,*} $RPM_BUILD_ROOT%{php_pear_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo 'pear/Auth can optionally use package "pear/File_Passwd" (version >= 0.9.5)
pear/Auth can optionally use package "pear/Net_POP3" (version >= 1.3)
pear/Auth can optionally use package "pear/DB"
pear/Auth can optionally use package "pear/MDB"
pear/Auth can optionally use package "pear/Auth_RADIUS"
pear/Auth can optionally use package "pear/File_SMBPasswd"
'

%files
%defattr(644,root,root,755)
%doc doc/%{_pearname}/README*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Container
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Container/*.php

%files  tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
