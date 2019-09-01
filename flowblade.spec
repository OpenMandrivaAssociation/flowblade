Name:           flowblade
Version:        2.2
Release:        1
Summary:        Multitrack non-linear video editor
License:        GPLv3
Group:          Video
Url:            https://github.com/jliljebl/flowblade/
Source0:        https://github.com/jliljebl/flowblade/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  pkgconfig(dbus-python)
Requires:       python2-dbus
Requires:       ffmpeg
Requires:       frei0r-plugins >= 1.4
Requires:       ladspa
Requires:       swh-plugins
Requires:       pkgconfig(cairomm-1.0)
Requires:       mlt
Requires:       librsvg2
Requires:       python2-cairo
Requires:       pygtk2
Requires:       python2-imaging
Requires:       python2-mlt
Requires:       python2-numpy
Requires:       sox

BuildArch:      noarch

%description
Flowblade is designed to provide a fast, precise and robust editing experience.

In Flowblade clips are usually automatically placed tightly after or between
clips when they are inserted on the timeline. Edits are fine tuned by trimming
in and out points of clips, or by cutting and deleting parts of clips.

Flowblade provides powerful tools to mix and filter video and audio.

%prep
%setup -q
cp -rf flowblade-trunk/* ./
sed -i 's|%{_datadir}/pyshared|%{py2_puresitedir}|' flowblade
sed -i "s|respaths.LOCALE_PATH|'%{_datadir}/locale'|g" Flowblade/translations.py

%build
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/locale
mv %{buildroot}%{py2_puresitedir}/Flowblade/locale/*  %{buildroot}%{_datadir}/locale
find %{buildroot} -type f -name "*.po*" -delete -print

mkdir -p %{buildroot}%{_datadir}/mime/packages
mv %{buildroot}/usr/lib/mime/packages/flowblade \
  %{buildroot}%{_datadir}/mime/packages/

chmod +x %{buildroot}%{py2_puresitedir}/Flowblade/launch/flowbladebatch \
  %{buildroot}%{py2_puresitedir}/Flowblade/launch/flowbladesinglerender \
  %{buildroot}%{py2_puresitedir}/Flowblade/launch/flowblademedialinker \
  %{buildroot}%{_bindir}/flowblade

chmod -x %{buildroot}%{_datadir}/applications/io.github.jliljebl.Flowblade.desktop \
 # %{buildroot}%{_datadir}/mime/packages/flowblade.xml \
 # %{buildroot}%{_datadir}/mime/packages/flowblade

#cp -rf help %{buildroot}%{py2_puresitedir}/Flowblade/res/

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING copyrights README README.md
%{_bindir}/flowblade
%{_datadir}/applications/io.github.jliljebl.Flowblade.desktop
%{_mandir}/man1/flowblade.1*
%{_datadir}/icons/hicolor/128x128/apps/io.github.jliljebl.Flowblade.png
%{py2_puresitedir}/Flowblade
%{py2_puresitedir}/flowblade-*.egg-info
%{_datadir}/mime/packages/*
%{_datadir}/appdata/io.github.jliljebl.Flowblade.appdata.xml
