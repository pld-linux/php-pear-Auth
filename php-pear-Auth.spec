%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define		_pearname	%{_class}
Summary:	%{_pearname} - php pear authentication class
Summary(pl):	%{_pearname} - klasa dla php pear z klasami uwierzytelniającymi
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Auth package provides methods for creating an authentication
system using PHP.

%description -l pl
Pakiet PEAR::Auth dostarcza metody do stworzenia systemu
uwierzytelniania używającego PHP.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Container

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/Container/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Container

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/README*
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Container/*.php
