Name:       libexif
Summary:    Library for extracting extra information from image files
Version:    0.6.19
Release:    3.16
Group:      System/Libraries
License:    LGPLv2+
#URL:        http://libexif.sourceforge.net/
# somewhat heavily modified to add Samsung's own tags for some reason...
Source0:    %{name}-%{version}-samsung.tar.gz
Source1001: packaging/libexif.manifest 

Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.


%package devel
Summary:    Files needed for libexif application development
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The libexif-devel package contains the libraries and header files
for writing programs that use libexif.

%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .

%configure --disable-static \
    --disable-docs

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
%find_lang libexif-12

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libexif

%clean
rm -rf %{buildroot}

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
