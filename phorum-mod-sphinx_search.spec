%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.0.0
%define		module		sphinx_search
Summary:	Sphinx Fulltext-Search Module
Name:		phorum-mod-%{module}
Version:	1.1
Release:	1
License:	Apache-like
Group:		Applications/WWW
Source0:	http://download.github.com/glensc-phorum-%{module}-%{version}-0-g20786ed.tar.gz
# Source0-md5:	74498f460023d41c1d44ac6fca6518d5
URL:		http://www.phorum.org/phorum5/read.php?62,136982,138325
BuildRequires:	rpm-php-pearprov
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	phorum >= 5.2
Requires:	php(sphinx)
Requires:	php-date
Requires:	php-pcre
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
rm sphinxapi.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{moduledir}
cp -a *.txt *.php $RPM_BUILD_ROOT%{moduledir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog sphinx.conf sph_counter.sql crontab
%dir %{moduledir}
%{moduledir}/*.php
%{moduledir}/info.txt
