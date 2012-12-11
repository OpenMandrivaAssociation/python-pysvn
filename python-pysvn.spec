%define oname pysvn

Summary:	Highlevel Subversion Python bindings
Name:		python-%{oname}
Version:	1.7.6
Release:	1
License:	Apache License
Group:		Development/Python
URL:		http://pysvn.tigris.org 
Source0:	http://pysvn.barrys-emacs.org/source_kits/%{oname}-%{version}.tar.gz
BuildRequires:	apr-devel
BuildRequires:	apr-util-devel
BuildRequires:	expat-devel
BuildRequires:	neon-devel
BuildRequires:	subversion-devel
BuildRequires:	subversion-tools
BuildRequires:	python-devel

%description
pysvn is a highlevel and easy to use Python bindings to Subversion.

%package	docs
Summary:	Programmer's documentation for pysvn
Group:		Development/Python
BuildArch:	noarch

%description	docs
pysvn is a highlevel and easy to use Python bindings to Subversion.

This package contains the pysvn Programmer's Guide and the Programmer's
Reference.

%prep
%setup -q -n %{oname}-%{version}

%build
cd Source
python setup.py configure --verbose --fixed-module-name --enable-debug

#fix flags
sed -i -e 's|$(LDLIBS)|$(LDFLAGS) $(LDLIBS)|g' Makefile
sed -i -e 's|-Wall -fPIC|%{optflags} -fPIC|g' Makefile

#fix build
sed -i -e 's|-lssl|-lssl -lpython2.7 -lapr-1 -lsvn_fs-1 -lsvn_wc-1 -lsvn_subr-1|g' Makefile

#disable rpath
sed -i -e 's|-Wl,--rpath -Wl,%{_libdir}||g' Makefile

%make LDFLAGS="%{ldflags}" 

%install
install -d %{buildroot}%{py_platsitedir}/%{oname}
cp -a Source/%oname/*.py %{buildroot}%{py_platsitedir}/%{oname}
cp -a Source/%{oname}/_pysvn*.so %{buildroot}%{py_platsitedir}/%{oname}

%files 
%defattr(-,root,root)
%doc LICENSE.txt
%{py_platsitedir}/%{oname}

%files docs
%defattr(-,root,root)
%doc Docs/*.html Docs/*.js Examples




%changelog
* Thu Dec 02 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.7.4-2mdv2011.0
+ Revision: 605307
- Rebuild with apr with workaround to issue with gcc type based

* Sun Oct 31 2010 Jani Välimaa <wally@mandriva.org> 1.7.4-1mdv2011.0
+ Revision: 591241
- mark docs subpackage as noarch
- new version 1.7.4
- use fixed module name
- drop py_requires macro
- disable byte-compiling
- disable rpath
- use correct compiler flags

* Tue Apr 13 2010 Funda Wang <fwang@mandriva.org> 1.7.2-2mdv2010.1
+ Revision: 534501
- rebuild

* Wed Jan 06 2010 Frederik Himpe <fhimpe@mandriva.org> 1.7.2-1mdv2010.1
+ Revision: 486817
- update to new version 1.7.2

* Sat Aug 29 2009 Frederik Himpe <fhimpe@mandriva.org> 1.7.0-1mdv2010.0
+ Revision: 422259
- update to new version 1.7.0

* Wed Feb 18 2009 Bogdano Arendartchuk <bogdano@mandriva.com> 1.6.3-1mdv2009.1
+ Revision: 342645
- new version 1.6.3

* Wed Feb 18 2009 Bogdano Arendartchuk <bogdano@mandriva.com> 1.5.1-6mdv2009.1
+ Revision: 342578
- added patch to force the support of python 2.6

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.5.1-5mdv2009.1
+ Revision: 323992
- fix linkage
- rebuild

* Wed Sep 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-4mdv2009.0
+ Revision: 285435
- fix deps
- rebuilt against latest neon libs

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Jun 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.1-2mdv2008.0
+ Revision: 36976
- rebuild for expat


* Thu Mar 01 2007 Jérôme Soyer <saispo@mandriva.org> 1.5.1-1mdv2007.0
+ Revision: 130370
- New release

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - fix after version upgrade)

* Wed Dec 06 2006 Jérôme Soyer <saispo@mandriva.org> 1.5.0-1mdv2007.1
+ Revision: 91597
- Remove patch and update
- Rebuild for latest pyhton

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - Import python-pysvn

