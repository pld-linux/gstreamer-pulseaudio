Summary:	GStreamer plugin for polypaudio
Summary(pl):	Wtyczka GStreamera do polypaudio
Name:		gstreamer-polypaudio
Version:	0.9.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/gst-polyp/gst-polyp-%{version}.tar.gz
# Source0-md5:	382b9f984683dc13c5952a6d833099a0
URL:		http://0pointer.de/lennart/projects/gst-polyp/
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	polypaudio-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer plugin for polypaudio.

%description -l pl
Wtyczka GStreamera do polypaudio.

%prep
%setup -q -n gst-polyp-%{version}

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/*.la
mv $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/libgstpolyp.so{.0.0.0,}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gstreamer-0.10/*.so
