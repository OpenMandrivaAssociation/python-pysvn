%define oname pysvn

Summary:	Highlevel Subversion Python bindings
Name:		python-%{oname}
Version:	1.5.1
Release:	%mkrel 1
License:	Apache License
Group:		Development/Python
URL:		http://pysvn.tigris.org 
Source0:	%{oname}-%{version}.tar.gz
Patch0:		pysvn-no_rpath.diff
Patch1:		pysvn-optflags.diff
BuildRequires:	libapr-devel
BuildRequires:	libexpat-devel
BuildRequires:	libneon-devel
BuildRequires:	libpython-devel
BuildRequires:	subversion-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
pysvn is a highlevel and easy to use Python bindings to Subversion.

%package	docs
Summary:	Programmer's documentation for pysvn
Group:		Development/Python

%description	docs
pysvn is a highlevel and easy to use Python bindings to Subversion.

This package contains the pysvn Programmer's Guide and the Programmer's
Reference.

%prep

%setup -q -n %{oname}-%{version}
%patch0 -p0
%patch1 -p0

cd Source && python setup.py configure

%build
%make -C Source

%install
rm -rf %{buildroot}

install -d %{buildroot}%{py_sitedir}/%{oname}
cp -a Source/%oname/*.py %{buildroot}%{py_sitedir}/%{oname}
install -d %{buildroot}%{py_platsitedir}/%{oname}
cp -a Source/%{oname}/_pysvn*.so %{buildroot}%{py_platsitedir}/%{oname}
%py_compile %{buildroot}%{py_sitedir}/%{oname}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc LICENSE.txt
%dir %{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}/*
%dir %{py_platsitedir}/%{oname}
%{py_platsitedir}/%{oname}/*

%files docs
%defattr(-,root,root)
%doc Docs/*.html Docs/*.js Examples


