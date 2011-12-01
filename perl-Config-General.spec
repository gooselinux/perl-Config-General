Name:           perl-Config-General
Version:        2.44
Release:        1%{?dist}
Summary:        Generic configuration module for Perl

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Config-General/
Source0:        http://www.cpan.org/authors/id/T/TL/TLINDEN/Config-General-%{version}.tar.gz
Patch0:         %{name}-2.42-system-ixhash.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::IxHash)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module opens a config file and parses its contents for
you. After parsing the module returns a hash structure which contains
the representation of the config file.
The format of config files supported by Config::General is inspired by
the well known Apache config format, in fact, this module is 100%
read-compatible with Apache configs, but you can also just use simple
name/value pairs in your config files.
In addition to the capabilities of an Apache config file it supports
some enhancements such as here-documents, C-style comments or
multiline options. It is also possible to save the config back to
disk, which makes the module a perfect backend for configuration
interfaces.
It is possible to use variables in config files and there exists also
support for object oriented access to the configuration.


%prep
%setup -q -n Config-General-%{version}
%patch0 -p1
rm -r t/Tie
f=Changelog ; iconv -f iso-8859-1 -t utf-8 -o $f.utf8 $f ; mv $f.utf8 $f


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changelog README example.cfg
%{perl_vendorlib}/Config/
%{_mandir}/man3/Config::*.3*


%changelog
* Tue Sep  8 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.44-1
- Update to 2.44 (#521756).
- Prune pre-2005 %%changelog entries.

* Sun Jul 26 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.43-1
- Update to 2.43 (#513796).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan  4 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.42-1
- 2.42.
- Patch test suite to use system installed Tie::IxHash.
- Fix some spelling errors in %%description.
- Use Source0: instead of Source:.

* Sat Jun 21 2008 Ville Skyttä <ville.skytta@iki.fi> - 2.40-1
- 2.40.

* Tue Jun 17 2008 Ville Skyttä <ville.skytta@iki.fi> - 2.39-1
- 2.39.

* Tue Mar  4 2008 Ville Skyttä <ville.skytta@iki.fi> - 2.38-1
- 2.38.

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.37-2
- rebuild for new perl

* Tue Nov 27 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.37-1
- 2.37 (#398801).
- Convert docs to UTF-8.

* Tue Aug  7 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.33-2
- License: GPL+ or Artistic

* Wed Apr 18 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.33-1
- 2.33.
- BuildRequire perl(ExtUtils::MakeMaker) and perl(Test::More).

* Sat Feb 24 2007 Ville Skyttä <ville.skytta@iki.fi> - 2.32-1
- 2.32.

* Tue Aug 29 2006 Ville Skyttä <ville.skytta@iki.fi> - 2.31-2
- Fix order of arguments to find(1).
- Drop version from perl build dependency.

* Thu Jan 12 2006 Ville Skyttä <ville.skytta@iki.fi> - 2.31-1
- 2.31.

* Fri Sep 16 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.30-1
- 2.30.

* Wed May 18 2005 Ville Skyttä <ville.skytta@iki.fi> - 2.28-2
- 2.28.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.27-2
- rebuilt
