%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - PHP PEAR authentication class
Summary(pl):	%{_pearname} - klasa dla PHP PEAR z klasami uwierzytelniającymi
Name:		php-pear-%{_pearname}
Version:	1.2.3
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1506c2a27afe85e8d56eaa8466b6f13a
URL:		http://pear.php.net/package/Auth/
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
uwierzytelniania używającego PHP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{Auth,Container}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/Auth/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Auth
install %{_pearname}-%{version}/Container/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Container

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{README*,tests}
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Auth
%dir %{php_pear_dir}/%{_class}/Container
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Auth/*.php
%{php_pear_dir}/%{_class}/Container/*.php
