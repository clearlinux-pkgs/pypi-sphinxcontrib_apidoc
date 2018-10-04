#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-apidoc
Version  : 0.3.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/57/55/23f6919551a5e0a824f0effc3a85dd1cbc8df225196c0f6b82c7cea38299/sphinxcontrib-apidoc-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/55/23f6919551a5e0a824f0effc3a85dd1cbc8df225196c0f6b82c7cea38299/sphinxcontrib-apidoc-0.3.0.tar.gz
Summary  : A Sphinx extension for running 'sphinx-apidoc' on each build
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-apidoc-python3
Requires: sphinxcontrib-apidoc-license
Requires: sphinxcontrib-apidoc-python
Requires: Sphinx
Requires: pbr
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
sphinxcontrib-apidoc
        ====================

%package license
Summary: license components for the sphinxcontrib-apidoc package.
Group: Default

%description license
license components for the sphinxcontrib-apidoc package.


%package python
Summary: python components for the sphinxcontrib-apidoc package.
Group: Default
Requires: sphinxcontrib-apidoc-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-apidoc package.


%package python3
Summary: python3 components for the sphinxcontrib-apidoc package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sphinxcontrib-apidoc package.


%prep
%setup -q -n sphinxcontrib-apidoc-0.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538676027
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/sphinxcontrib-apidoc
cp LICENSE %{buildroot}/usr/share/doc/sphinxcontrib-apidoc/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/sphinxcontrib-apidoc/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
