%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Auth
Summary:	%{_pearname} - PHP PEAR authentication class
Summary(pl.UTF-8):	%{_pearname} - klasa dla PHP PEAR z klasami uwierzytelniającymi
Name:		php-pear-%{_pearname}
Version:	1.6.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5b753f9f6ad799aa3ac1c691c07b2654
URL:		http://pear.php.net/package/Auth/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php-pear >= 4:1.0-8
Suggests:	php-imap
Suggests:	php-pear-Auth_RADIUS
Suggests:	php-pear-Crypt_CHAP
Suggests:	php-pear-DB
Suggests:	php-pear-File_Passwd
Suggests:	php-pear-File_SMBPasswd
Suggests:	php-pear-HTTP_Client
Suggests:	php-pear-Log
Suggests:	php-pear-MDB
Suggests:	php-pear-MDB2
Suggests:	php-pear-Net_POP3
Suggests:	php-pear-Net_Vpopmaild
Suggests:	php-pear-SOAP
Suggests:	php-pecl-kadm5
Suggests:	php-pecl-vpopmail
Suggests:	php-saprfc
Suggests:	php-soap
Obsoletes:	php-pear-Auth-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Auth/RADIUS.*) pear(Crypt/CHAP.*) pear(DB.*) pear(File/Passwd.*) pear(File/SMBPasswd.*) pear(HTTP/Client.*) pear(Log.*) pear(MDB.*) pear(MDB2.*) pear(Net/POP3.*) pear(Net/Vpopmaild.*) pear(SOAP.*)

%description
The PEAR::Auth package provides methods for creating an authentication
system using PHP.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet PEAR::Auth dostarcza metody do stworzenia systemu
uwierzytelniania używającego PHP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log optional-packages.txt
%doc docs/%{_pearname}/README*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/Auth/*.php
%{php_pear_dir}/Auth/Container
%{php_pear_dir}/Auth/Frontend
