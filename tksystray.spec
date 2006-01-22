Summary:	Tk systray extension
Summary(pl):	Rozszerzenie Tk o obs³ugê doku systemowego
Name:		tksystray
Version:	0.1
Release:	0.1
License:	Unknown (not provided)
Group:		Development/Languages/Tcl
Source0:	http://sgolovan.nes.ru/debian/pool/main/tksystray/%{name}_%{version}.orig.tar.gz
# Source0-md5:	d1784d2f786304bd6eaa82512fd5cf1c
URL:		http://tkabber.jabber.ru/tksystray
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	imlib2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freedesktop systray for Tk

%description -l pl
Obs³uga doku systemowego Freedesktop dla Tk


%prep
%setup -q -n %{name}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}

install -m 0644 pkgIndex.tcl $RPM_BUILD_ROOT%{_libdir}/%{name}/
install -m 0755 libtray.so $RPM_BUILD_ROOT%{_libdir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libtray.so
%{_libdir}/%{name}/pkgIndex.tcl
