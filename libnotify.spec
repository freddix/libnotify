Summary:	Desktop notifications library
Name:		libnotify
Version:	0.7.6
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (tools)
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libnotify/0.7/%{name}-%{version}.tar.xz
# Source0-md5:	a4997019d08f46f3bf57b78e6f795a59
URL:		http://developer.gnome.org/notification-spec/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	glib-gio-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
A library that sends desktop notifications to a notification daemon,
as defined in the Desktop Notifications spec. These notifications can
be used to inform the user about an event or display some form of
information without getting in the user's way.

%package devel
Summary:	libnotify header files
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnotify-based programs development.

%package apidocs
Summary:	libnotify API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libnotify  API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libnotify.so.?
%attr(755,root,root) %{_libdir}/libnotify.so.*.*.*
%{_libdir}/girepository-1.0/Notify-0.7.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/gir-1.0/Notify-0.7.gir
%{_includedir}/libnotify
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

