#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libxfce4ui
Version  : 4.13.4
Release  : 21
URL      : http://archive.xfce.org/src/xfce/libxfce4ui/4.13/libxfce4ui-4.13.4.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/libxfce4ui/4.13/libxfce4ui-4.13.4.tar.bz2
Summary  : Private Xfce library for shared code between xfwm4 and xfce4-settings
Group    : Development/Tools
License  : LGPL-2.0
Requires: libxfce4ui-bin
Requires: libxfce4ui-lib
Requires: libxfce4ui-data
Requires: libxfce4ui-doc
Requires: libxfce4ui-locales
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : gtk3-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(sm)
BuildRequires : startup-notification-dev
Patch1: 0001-Set-default-keyboard-shortcuts-for-use-within-Clear-.patch

%description
What is it?
===========
This is libxfce4ui, the replacement of the old libxfcegui4 library. It is used
to share commonly used Xfce widgets among the Xfce applications.

%package bin
Summary: bin components for the libxfce4ui package.
Group: Binaries
Requires: libxfce4ui-data

%description bin
bin components for the libxfce4ui package.


%package data
Summary: data components for the libxfce4ui package.
Group: Data

%description data
data components for the libxfce4ui package.


%package dev
Summary: dev components for the libxfce4ui package.
Group: Development
Requires: libxfce4ui-lib
Requires: libxfce4ui-bin
Requires: libxfce4ui-data
Provides: libxfce4ui-devel

%description dev
dev components for the libxfce4ui package.


%package doc
Summary: doc components for the libxfce4ui package.
Group: Documentation

%description doc
doc components for the libxfce4ui package.


%package lib
Summary: lib components for the libxfce4ui package.
Group: Libraries
Requires: libxfce4ui-data

%description lib
lib components for the libxfce4ui package.


%package locales
Summary: locales components for the libxfce4ui package.
Group: Default

%description locales
locales components for the libxfce4ui package.


%prep
%setup -q -n libxfce4ui-4.13.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514495838
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%configure --disable-static --with-vendor-info="Clear Linux Project for Intel Architecture"
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1514495838
rm -rf %{buildroot}
%make_install
%find_lang libxfce4ui
## make_install_append content
mv %{buildroot}%{_sysconfdir}/xdg %{buildroot}%{_datadir}/. && rmdir %{buildroot}%{_sysconfdir} && install -d -D -m 00755 %{buildroot}%{_datadir}/xfce4 && echo "Clear Linux Project for Intel Architecture" > %{buildroot}%{_datadir}/xfce4/vendorinfo
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-about

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/libxfce4ui-2.0.typelib
/usr/share/applications/xfce4-about.desktop
/usr/share/gir-1.0/*.gir
/usr/share/icons/hicolor/48x48/apps/xfce4-logo.png
/usr/share/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
/usr/share/xfce4/vendorinfo

%files dev
%defattr(-,root,root,-)
/usr/include/xfce4/libxfce4kbd-private-2/libxfce4kbd-private/xfce-shortcut-dialog.h
/usr/include/xfce4/libxfce4kbd-private-2/libxfce4kbd-private/xfce-shortcuts-grabber.h
/usr/include/xfce4/libxfce4kbd-private-2/libxfce4kbd-private/xfce-shortcuts-provider.h
/usr/include/xfce4/libxfce4kbd-private-2/libxfce4kbd-private/xfce-shortcuts-xfwm4.h
/usr/include/xfce4/libxfce4kbd-private-2/libxfce4kbd-private/xfce-shortcuts.h
/usr/include/xfce4/libxfce4kbd-private-3/libxfce4kbd-private/xfce-shortcut-dialog.h
/usr/include/xfce4/libxfce4kbd-private-3/libxfce4kbd-private/xfce-shortcuts-grabber.h
/usr/include/xfce4/libxfce4kbd-private-3/libxfce4kbd-private/xfce-shortcuts-provider.h
/usr/include/xfce4/libxfce4kbd-private-3/libxfce4kbd-private/xfce-shortcuts-xfwm4.h
/usr/include/xfce4/libxfce4kbd-private-3/libxfce4kbd-private/xfce-shortcuts.h
/usr/include/xfce4/libxfce4ui-1/libxfce4ui/libxfce4ui-config.h
/usr/include/xfce4/libxfce4ui-1/libxfce4ui/libxfce4ui-enum-types.h
/usr/include/xfce4/libxfce4ui-1/libxfce4ui/libxfce4ui.h
/usr/include/xfce4/libxfce4ui-1/libxfce4ui/xfce-dialogs.h
/usr/include/xfce4/libxfce4ui-1/libxfce4ui/xfce-gdk-extensions.h
/usr/include/xfce4/libxfce4ui-1/libxfce4ui/xfce-gtk-extensions.h
/usr/include/xfce4/libxfce4ui-1/libxfce4ui/xfce-sm-client.h
/usr/include/xfce4/libxfce4ui-1/libxfce4ui/xfce-spawn.h
/usr/include/xfce4/libxfce4ui-1/libxfce4ui/xfce-titled-dialog.h
/usr/include/xfce4/libxfce4ui-2/libxfce4ui/libxfce4ui-config.h
/usr/include/xfce4/libxfce4ui-2/libxfce4ui/libxfce4ui-enum-types.h
/usr/include/xfce4/libxfce4ui-2/libxfce4ui/libxfce4ui.h
/usr/include/xfce4/libxfce4ui-2/libxfce4ui/xfce-dialogs.h
/usr/include/xfce4/libxfce4ui-2/libxfce4ui/xfce-gdk-extensions.h
/usr/include/xfce4/libxfce4ui-2/libxfce4ui/xfce-gtk-extensions.h
/usr/include/xfce4/libxfce4ui-2/libxfce4ui/xfce-sm-client.h
/usr/include/xfce4/libxfce4ui-2/libxfce4ui/xfce-spawn.h
/usr/include/xfce4/libxfce4ui-2/libxfce4ui/xfce-titled-dialog.h
/usr/lib64/libxfce4kbd-private-2.so
/usr/lib64/libxfce4kbd-private-3.so
/usr/lib64/libxfce4ui-1.so
/usr/lib64/libxfce4ui-2.so
/usr/lib64/pkgconfig/libxfce4kbd-private-2.pc
/usr/lib64/pkgconfig/libxfce4kbd-private-3.pc
/usr/lib64/pkgconfig/libxfce4ui-1.pc
/usr/lib64/pkgconfig/libxfce4ui-2.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/libxfce4ui/XfceSMClient.html
/usr/share/gtk-doc/html/libxfce4ui/XfceTitledDialog.html
/usr/share/gtk-doc/html/libxfce4ui/annotation-glossary.html
/usr/share/gtk-doc/html/libxfce4ui/api-index-4-10.html
/usr/share/gtk-doc/html/libxfce4ui/api-index-4-12.html
/usr/share/gtk-doc/html/libxfce4ui/api-index-4-14.html
/usr/share/gtk-doc/html/libxfce4ui/api-index-full.html
/usr/share/gtk-doc/html/libxfce4ui/home.png
/usr/share/gtk-doc/html/libxfce4ui/index.html
/usr/share/gtk-doc/html/libxfce4ui/left-insensitive.png
/usr/share/gtk-doc/html/libxfce4ui/left.png
/usr/share/gtk-doc/html/libxfce4ui/libxfce4ui-Gdk-Extensions.html
/usr/share/gtk-doc/html/libxfce4ui/libxfce4ui-Gtk-Extensions.html
/usr/share/gtk-doc/html/libxfce4ui/libxfce4ui-Spawn.html
/usr/share/gtk-doc/html/libxfce4ui/libxfce4ui-XfceDialogs.html
/usr/share/gtk-doc/html/libxfce4ui/libxfce4ui-extensions.html
/usr/share/gtk-doc/html/libxfce4ui/libxfce4ui-fundamentals.html
/usr/share/gtk-doc/html/libxfce4ui/libxfce4ui-introduction.html
/usr/share/gtk-doc/html/libxfce4ui/libxfce4ui-libxfce4ui-config.html
/usr/share/gtk-doc/html/libxfce4ui/libxfce4ui-sm.html
/usr/share/gtk-doc/html/libxfce4ui/libxfce4ui-widgets.html
/usr/share/gtk-doc/html/libxfce4ui/libxfce4ui.devhelp2
/usr/share/gtk-doc/html/libxfce4ui/right-insensitive.png
/usr/share/gtk-doc/html/libxfce4ui/right.png
/usr/share/gtk-doc/html/libxfce4ui/style.css
/usr/share/gtk-doc/html/libxfce4ui/up-insensitive.png
/usr/share/gtk-doc/html/libxfce4ui/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxfce4kbd-private-2.so.0
/usr/lib64/libxfce4kbd-private-2.so.0.0.0
/usr/lib64/libxfce4kbd-private-3.so.0
/usr/lib64/libxfce4kbd-private-3.so.0.0.0
/usr/lib64/libxfce4ui-1.so.0
/usr/lib64/libxfce4ui-1.so.0.0.0
/usr/lib64/libxfce4ui-2.so.0
/usr/lib64/libxfce4ui-2.so.0.0.0

%files locales -f libxfce4ui.lang
%defattr(-,root,root,-)

