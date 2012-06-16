Name:           libexif
Version:        0.6.19
Release:        5
License:        LGPL-2.0+
Summary:        Library for extracting extra information from image files
Group:          System/Libraries
Source0:        %{name}-%{version}.tar.gz
Source1001:     libexif.manifest

Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%package devel
Summary:        Files needed for libexif application development
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
The libexif-devel package contains the libraries and header files
for writing programs that use libexif.

%prep
%setup -q

%build
cp %{SOURCE1001} .

%configure --disable-docs

make %{?_smp_mflags}

%install
%make_install
%find_lang libexif-12

rm -rf %{buildroot}%{_datadir}/doc/libexif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f libexif-12.lang
%manifest libexif.manifest
%{_libdir}/libexif.so.*

%files devel
%manifest libexif.manifest
%{_includedir}/libexif
%{_libdir}/*.so
%{_libdir}/pkgconfig/libexif.pc
