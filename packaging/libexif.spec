#sbs-git:slp/pkgs/l/libexif libexif 0.6.19 57d8319d0146f2739299469313fc694846cd7c10
Name:       libexif
Summary:    Library for extracting extra information from image files
Version: 0.6.19
Release:    1
Group:      System/Libraries
License:    LGPLv2+
#URL:        http://libexif.sourceforge.net/
# somewhat heavily modified to add Samsung's own tags for some reason...
Source0:    %{name}-%{version}-samsung.tar.gz

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
%setup -q -n %{name}-%{version}-samsung

%build

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
%{_libdir}/libexif.so.*

%files devel
%{_includedir}/libexif
%{_libdir}/*.so
%{_libdir}/pkgconfig/libexif.pc
