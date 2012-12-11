
Summary: Morphology Toolbox for Python
Name: python-morph
Version: 0.8
Release: %mkrel 7
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
Buildrequires: python-devel

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
mkdir -p $RPM_BUILD_ROOT/%{py_puresitedir}
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




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.8-7mdv2010.0
+ Revision: 442315
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.8-6mdv2009.1
+ Revision: 323811
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.8-5mdv2009.0
+ Revision: 242421
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 26 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.8-3mdv2008.0
+ Revision: 71569
- fix build on x86_64
- build requires python
- reb?\195uild


* Wed Aug 09 2006 glehmann
+ 08/09/06 20:05:30 (55107)
use py_puresitedir

* Sun Jul 30 2006 glehmann
+ 07/30/06 10:26:36 (42700)
Import python-morph

* Sun Sep 25 2005 <gaetan.lehmann@jouy.inra.fr> 0.8-1mdk
- initial contrib

