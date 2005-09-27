# TODO
# - http://pear.php.net/bugs/bug.php?id=4371
%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - PHP PEAR authentication class
Summary(pl):	%{_pearname} - klasa dla PHP PEAR z klasami uwierzytelniaj±cymi
Name:		php-pear-%{_pearname}
Version:	1.2.3
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1506c2a27afe85e8d56eaa8466b6f13a
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/Auth/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear >= 4:1.0-8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional
%define		_noautoreq 'pear(Auth/RADIUS.php)' 'pear(File/Passwd.php)' 'pear(File/SMBPasswd.php)' 'pear(Net/POP3.php)'
# tests
# 'pear(DBContainer.php) 'pear(FileContainer.php) 'pear(IMAPContainer.php) 'pear(MDBContainer.php) 'pear(POP3Container.php) 'pear(POP3aContainer.php) 'pear(TestAuthContainer.php)'

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
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Autoreq:	no
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/%{_class}
%patch0 -p2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/README*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/Container
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Container/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
