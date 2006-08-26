Summary:	GStreamer plugin for PulseAudio sound server
Summary(pl):	Wtyczka GStreamera dla serwera d¼wiêku PulseAudio
Name:		gstreamer-pulseaudio
Version:	0.9.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/gst-pulse/gst-pulse-%{version}.tar.gz
# Source0-md5:	70c1897c7a51589797984a67dab90c86
URL:		http://0pointer.de/lennart/projects/gst-pulse/
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	pulseaudio-devel >= 0.9.2
BuildRequires:	pkgconfig
Obsoletes:	gstreamer-polypaudio
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer plugin for PulseAudio sound server.

%description -l pl
Wtyczka GStreamera dla serwera d¼wiêku PulseAudio.

%prep
%setup -q -n gst-pulse-%{version}

%build
%configure \
	--disable-lynx \
	--disable-static
%{__make} \
	libgstpulse_la_LDFLAGS=-avoid-version

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/gstreamer-0.10/*.so
