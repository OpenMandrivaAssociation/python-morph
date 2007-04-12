
Summary: Morphology Toolbox for Python
Name: python-morph
Version: 0.8
Release: %mkrel 2
Source0: pymorph-%{version}.tar.bz2
Patch0:  pymorph-demo-import.patch
License: BSD
Group: Sciences/Other
Url: http://www.mmorph.com/pymorph/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides: pymorph = %{version}-%{release}
BuildArch: noarch
Requires: python-numeric
Requires: python-imaging
Buildrequires: dos2unix

%description
The pymorph Morphology Toolbox for Python is a powerful collection of latest
state-of-the-art gray-scale morphological tools that can be applied to image
segmentation, non-linear filtering, pattern recognition and image analysis.
The pymorph Morphology Toolbox is an open source software for Morphological
Image Analysis and Signal Processing written in Python. It is a companion
resource for the book: Hands-on Morphological Image Processing , by Edward
Dougherty and Roberto Lotufo, published by SPIE, Aug 2003, ISBN=0-8194-4720-X.

%prep
%setup -q -n pymorph
%patch0
find -type f -name '*.html' -exec dos2unix -U {} \;
find -type f -name '*.css' -exec dos2unix -U {} \;

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/python%{pyver}/site-packages
cp PURELIB/adtools/morph08pybase/morph.py $RPM_BUILD_ROOT/%{py_puresitedir}
cp PURELIB/adtools/morph08pybase/morphdemo.py $RPM_BUILD_ROOT/%{py_puresitedir}
cp PURELIB/adtools/adpil10all/adpil.py $RPM_BUILD_ROOT/%{py_puresitedir}
cp PURELIB/adtools/adpil10all/adpildemo.py $RPM_BUILD_ROOT/%{py_puresitedir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{py_puresitedir}/*
%doc PLATLIB/adtools/morph08pybase/data
%doc PLATLIB/adtools/morph08pybase/html


