#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v20
# autospec commit: f35655a
#
Name     : pypi-pdm_backend
Version  : 2.4.3
Release  : 22
URL      : https://files.pythonhosted.org/packages/d9/bf/d75d568521cef171ae9138d9ab55c169a98ee803853ca87b7096e4636d5b/pdm_backend-2.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/d9/bf/d75d568521cef171ae9138d9ab55c169a98ee803853ca87b7096e4636d5b/pdm_backend-2.4.3.tar.gz
Summary  : The build backend used by PDM that supports latest packaging standards
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause MIT
Requires: pypi-pdm_backend-license = %{version}-%{release}
Requires: pypi-pdm_backend-python = %{version}-%{release}
Requires: pypi-pdm_backend-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# PDM-Backend
The build backend used by [PDM] that supports latest packaging standards.

%package license
Summary: license components for the pypi-pdm_backend package.
Group: Default

%description license
license components for the pypi-pdm_backend package.


%package python
Summary: python components for the pypi-pdm_backend package.
Group: Default
Requires: pypi-pdm_backend-python3 = %{version}-%{release}

%description python
python components for the pypi-pdm_backend package.


%package python3
Summary: python3 components for the pypi-pdm_backend package.
Group: Default
Requires: python3-core
Provides: pypi(pdm_backend)

%description python3
python3 components for the pypi-pdm_backend package.


%prep
%setup -q -n pdm_backend-2.4.3
cd %{_builddir}/pdm_backend-2.4.3
pushd ..
cp -a pdm_backend-2.4.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1729693797
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pdm_backend
cp %{_builddir}/pdm_backend-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pdm_backend/f15bd5033216f10c392e98887c39374601c898ac || :
cp %{_builddir}/pdm_backend-%{version}/src/pdm/backend/_vendor/editables/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pdm_backend/4caad070b55cf4f951f487b96b1f2b5a2795cf8b || :
cp %{_builddir}/pdm_backend-%{version}/src/pdm/backend/_vendor/packaging/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/pypi-pdm_backend/598f87f072f66e2269dd6919292b2934dbb20492 || :
cp %{_builddir}/pdm_backend-%{version}/src/pdm/backend/_vendor/packaging/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-pdm_backend/fdc0e4eabc45522b079deff7d03d70528d775dc0 || :
cp %{_builddir}/pdm_backend-%{version}/src/pdm/backend/_vendor/pyproject_metadata/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pdm_backend/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9 || :
cp %{_builddir}/pdm_backend-%{version}/src/pdm/backend/_vendor/tomli/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pdm_backend/9da6ca26337a886fb3e8d30efd4aeda623dc9ade || :
cp %{_builddir}/pdm_backend-%{version}/src/pdm/backend/_vendor/tomli_w/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pdm_backend/9da6ca26337a886fb3e8d30efd4aeda623dc9ade || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pdm_backend/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9
/usr/share/package-licenses/pypi-pdm_backend/4caad070b55cf4f951f487b96b1f2b5a2795cf8b
/usr/share/package-licenses/pypi-pdm_backend/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/pypi-pdm_backend/9da6ca26337a886fb3e8d30efd4aeda623dc9ade
/usr/share/package-licenses/pypi-pdm_backend/f15bd5033216f10c392e98887c39374601c898ac
/usr/share/package-licenses/pypi-pdm_backend/fdc0e4eabc45522b079deff7d03d70528d775dc0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
