%define oname pysvn

Summary:	Highlevel Subversion Python bindings
Name:		python-%{oname}
Version:	1.7.4
Release:	%mkrel 2
License:	Apache License
Group:		Development/Python
URL:		http://pysvn.tigris.org 
Source0:	http://pysvn.barrys-emacs.org/source_kits/%{oname}-%{version}.tar.gz
BuildRequires:	apr-devel
BuildRequires:	expat-devel
BuildRequires:	neon-devel
BuildRequires:	subversion-devel
BuildRequires:	subversion-tools
BuildRequires:	python-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}

install -d %{buildroot}%{py_platsitedir}/%{oname}
cp -a Source/%oname/*.py %{buildroot}%{py_platsitedir}/%{oname}
cp -a Source/%{oname}/_pysvn*.so %{buildroot}%{py_platsitedir}/%{oname}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc LICENSE.txt
%{py_platsitedir}/%{oname}

%files docs
%defattr(-,root,root)
%doc Docs/*.html Docs/*.js Examples


