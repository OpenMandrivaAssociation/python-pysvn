%define oname pysvn

Summary:	Highlevel Subversion Python bindings
Name:		python-%{oname}
Version:	1.5.1
Release:	%mkrel 5
License:	Apache License
Group:		Development/Python
URL:		http://pysvn.tigris.org 
Source0:	%{oname}-%{version}.tar.gz
Patch0:		pysvn-no_rpath.diff
Patch1:		pysvn-optflags.diff
Patch2:		pysvn-linkage.patch
BuildRequires:	apr-devel
BuildRequires:	expat-devel
BuildRequires:	neon-devel
BuildRequires:	subversion-devel
%py_requires -d
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch2 -p0 -b .linkage

%build
cd Source
python setup.py configure
%make LDFLAGS="%{?ldflags}" 

%install
rm -rf %{buildroot}

install -d %{buildroot}%{py_platsitedir}/%{oname}
cp -a Source/%oname/*.py %{buildroot}%{py_platsitedir}/%{oname}
install -d %{buildroot}%{py_platsitedir}/%{oname}
cp -a Source/%{oname}/_pysvn*.so %{buildroot}%{py_platsitedir}/%{oname}
%py_compile %{buildroot}%{py_platsitedir}/%{oname}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc LICENSE.txt
%dir %{py_platsitedir}/%{oname}
%{py_platsitedir}/%{oname}/*

%files docs
%defattr(-,root,root)
%doc Docs/*.html Docs/*.js Examples


