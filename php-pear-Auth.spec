%include	/usr/lib/rpm/macros.php
%define		_pearname	Auth
Summary:	Auth - php pear authentication class
Summary(pl):	Auth - klasa dla php pear z klasami autentyfikuj±cymi
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Auth package provides methods for creating an authentication
system using PHP.

%description -l pl
Pakiet PEAR::Auth dostarcza metody do stworzenia systemu
autentyfikacji u¿ywaj±cego PHP.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}
install Container/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/README*
%dir %{php_pear_dir}/%{_pearname}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_pearname}/*.php
