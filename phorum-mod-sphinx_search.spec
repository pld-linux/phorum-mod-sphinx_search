%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.0.0
%define		module		sphinx_search
Summary:	Sphinx Fulltext-Search Module
Name:		phorum-mod-%{module}
Version:	1.0.0
Release:	0.7
License:	Apache-like
Group:		Applications/WWW
Source0:	http://www.phorum.org/phorum5/file.php/download/62/3354/sphinx_search_%{version}.tar.gz
# Source0-md5:	fd6bafce5d77c1baf90bf5f5e157bfb8
Source1:	sph_counter.sql
Source2:	sphinx.conf
Patch0:		paths.patch
Patch1:		errors.patch
Patch2:		index_names.patch
Patch3:		cleanup-junk.patch
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
mv %{module}/* .
cp -a %{SOURCE1} .
cp -a %{SOURCE2} .
%undos *.php *.txt README Changelog
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# php-sphinx
rm sphinxclient.php

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{moduledir}
cp -a *.txt *.php $RPM_BUILD_ROOT%{moduledir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog sphinx.conf sph_counter.sql
%dir %{moduledir}
%{moduledir}/*.php
%{moduledir}/info.txt
