Summary:	Public Domain Icons
Name:		apache-icons
Version:	1.0
Release:	1
License:	Public Domain
Group:		Applications/WWW
# icons from apache 2.2.6 distributions
Source0:	%{name}.tar.bz2
# Source0-md5:	9e6091b200af6d03576534919c79ea96
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These icons were originally made for Mosaic for X and have been
included in the NCSA httpd and Apache server distributions in the
past. They are in the public domain and may be freely included in any
application.

%prep
%setup -qc
mv apache-icons/README* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}
cp -a apache-icons $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.html
%{_datadir}/%{name}
