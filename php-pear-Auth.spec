%define		_pearname	Auth
Summary:	Auth - php pear authentication class
Summary(pl):	Auth - klasa dla php pear z klasami autentyfikuj±cymi
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
PreReq:		php-pear >= 4.2.0
PreReq:		php-zlib >= 4.2.0
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		peardir		%{_datadir}/pear

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

install -d $RPM_BUILD_ROOT%{peardir}/%{_pearname}

install *.php			$RPM_BUILD_ROOT%{peardir}
install Container/*.php		$RPM_BUILD_ROOT%{peardir}/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/README*
%dir %{peardir}/%{_pearname}
%{peardir}/*.php
%{peardir}/%{_pearname}/*.php
