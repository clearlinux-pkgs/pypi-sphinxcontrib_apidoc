#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v3
# autospec commit: 537da87
#
Name     : pypi-sphinxcontrib_apidoc
Version  : 0.5.0
Release  : 41
URL      : https://files.pythonhosted.org/packages/52/8c/a4fe93b51a1026c217731337cfe50569b8521d3e254dd451126bed208cd8/sphinxcontrib-apidoc-0.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/52/8c/a4fe93b51a1026c217731337cfe50569b8521d3e254dd451126bed208cd8/sphinxcontrib-apidoc-0.5.0.tar.gz
Summary  : A Sphinx extension for running 'sphinx-apidoc' on each build
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-sphinxcontrib_apidoc-license = %{version}-%{release}
Requires: pypi-sphinxcontrib_apidoc-python = %{version}-%{release}
Requires: pypi-sphinxcontrib_apidoc-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pbr)
BuildRequires : pypi(sphinx)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
====================
sphinxcontrib-apidoc
====================
.. image:: https://github.com/sphinx-contrib/apidoc/actions/workflows/ci.yaml/badge.svg
:target: https://github.com/sphinx-contrib/apidoc/actions/workflows/ci.yaml
:alt: Build Status

%package license
Summary: license components for the pypi-sphinxcontrib_apidoc package.
Group: Default

%description license
license components for the pypi-sphinxcontrib_apidoc package.


%package python
Summary: python components for the pypi-sphinxcontrib_apidoc package.
Group: Default
Requires: pypi-sphinxcontrib_apidoc-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxcontrib_apidoc package.


%package python3
Summary: python3 components for the pypi-sphinxcontrib_apidoc package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_apidoc)
Requires: pypi(pbr)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinxcontrib_apidoc package.


%prep
%setup -q -n sphinxcontrib-apidoc-0.5.0
cd %{_builddir}/sphinxcontrib-apidoc-0.5.0
pushd ..
cp -a sphinxcontrib-apidoc-0.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1705503246
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_apidoc
cp %{_builddir}/sphinxcontrib-apidoc-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_apidoc/f46de5f58d55a3c4dff150b3a055d90c2458b44e || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinxcontrib_apidoc/f46de5f58d55a3c4dff150b3a055d90c2458b44e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
