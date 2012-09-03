%define		php_min_version 5.0.0
%define		module		sphinx_search
%include	/usr/lib/rpm/macros.php
Summary:	Sphinx Fulltext-Search Module
Name:		phorum-mod-%{module}
Version:	1.1.1
Release:	1
License:	Apache-like
Group:		Applications/WWW
Source0:	https://github.com/glensc/phorum-sphinx_search/tarball/%{version}/%{name}-%{version}.tgz
# Source0-md5:	18ca3bd65e2290489d8610138b1591c5
URL:		https://github.com/glensc/phorum-sphinx_search
BuildRequires:	rpm-php-pearprov
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	phorum >= 5.2
Requires:	php(date)
Requires:	php(pcre)
Requires:	php(sphinx)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		modsdir		%{_datadir}/phorum/mods
%define		moduledir	%{modsdir}/%{module}

# no pear deps
%define		_noautopear	pear

# exclude optional php dependencies
%define		_noautophp	%{nil}

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
Module for using sphinx as fulltext search-engine instead of phorum
built-in search.

%prep
%setup -qc
mv *-%{module}-*/* .

# php-sphinx (native) or php-pecl-sphinx (extension)
%{__rm} sphinxapi.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{moduledir}
cp -p *.txt *.php $RPM_BUILD_ROOT%{moduledir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog sphinx.conf sph_counter.sql crontab
%dir %{moduledir}
%{moduledir}/*.php
%{moduledir}/info.txt
