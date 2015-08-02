Name:           flowblade
Version:        0.18.0
Release:        1
Summary:        Multitrack non-linear video editor
License:        GPLv3
Group:          Video
Url:            https://code.google.com/p/flowblade/
# Obtaining the source:
# hg clone https://code.google.com/p/flowblade/
Source0:         %{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
Requires:       pkgconfig(dbus-python)
Requires:       ffmpeg
Requires:       frei0r-plugins >= 1.4
Requires:       ladspa
Requires:       swh-plugins
Requires:       pkgconfig(cairomm-1.0)
Requires:       mlt
Requires:       librsvg2
Requires:       python2-cairo
Requires:       gnome-python2
Requires:       gnome-python2-gnomevfs
Requires:       pygtk2
Requires:       python2-imaging
Requires:       python-mlt
Requires:       python-numpy
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

sed -i 's|%{_datadir}/pyshared|%{py_puresitedir}|' flowblade
sed -i "s|respaths.LOCALE_PATH|'%{_datadir}/locale'|g" Flowblade/translations.py

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/locale
mv %{buildroot}%{py_puresitedir}/Flowblade/locale/*  %{buildroot}%{_datadir}/locale
find %{buildroot} -type f -name "*.po*" -delete -print

mkdir -p %{buildroot}%{_datadir}/mime/packages
mv %{buildroot}/usr/lib/mime/packages/flowblade \
  %{buildroot}%{_datadir}/mime/packages/

chmod +x %{buildroot}%{py_puresitedir}/Flowblade/launch/flowbladebatch \
  %{buildroot}%{py_puresitedir}/Flowblade/launch/flowblademedialinker \
  %{buildroot}%{_bindir}/flowblade

chmod -x %{buildroot}%{_datadir}/applications/flowblade.desktop \
  %{buildroot}%{_datadir}/mime/packages/flowblade.xml \
  %{buildroot}%{_datadir}/mime/packages/flowblade


desktop-file-validate %{buildroot}%{_datadir}/applications/flowblade.desktop

%find_lang Flowblade %{name}.lang


%files -f %{name}.lang
%{_bindir}/flowblade
%{_datadir}/applications/flowblade.desktop
%{_mandir}/man1/flowblade.1*
%{_datadir}/pixmaps/flowblade.png
%{py_puresitedir}/Flowblade
%{py_puresitedir}/flowblade-*.egg-info
%{_datadir}/mime/packages/*
