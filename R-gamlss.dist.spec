#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gamlss.dist
Version  : 6.0.3
Release  : 2
URL      : https://cran.r-project.org/src/contrib/gamlss.dist_6.0-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gamlss.dist_6.0-3.tar.gz
Summary  : Distributions for Generalized Additive Models for Location Scale
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-gamlss.dist-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-gamlss.dist package.
Group: Libraries

%description lib
lib components for the R-gamlss.dist package.


%prep
%setup -q -c -n gamlss.dist
cd %{_builddir}/gamlss.dist

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649176732

%install
export SOURCE_DATE_EPOCH=1649176732
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamlss.dist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamlss.dist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamlss.dist
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gamlss.dist || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gamlss.dist/DESCRIPTION
/usr/lib64/R/library/gamlss.dist/Distributions-2010.pdf
/usr/lib64/R/library/gamlss.dist/INDEX
/usr/lib64/R/library/gamlss.dist/Meta/Rd.rds
/usr/lib64/R/library/gamlss.dist/Meta/features.rds
/usr/lib64/R/library/gamlss.dist/Meta/hsearch.rds
/usr/lib64/R/library/gamlss.dist/Meta/links.rds
/usr/lib64/R/library/gamlss.dist/Meta/nsInfo.rds
/usr/lib64/R/library/gamlss.dist/Meta/package.rds
/usr/lib64/R/library/gamlss.dist/NAMESPACE
/usr/lib64/R/library/gamlss.dist/R/gamlss.dist
/usr/lib64/R/library/gamlss.dist/R/gamlss.dist.rdb
/usr/lib64/R/library/gamlss.dist/R/gamlss.dist.rdx
/usr/lib64/R/library/gamlss.dist/doc/CentileSkewKurt.RData
/usr/lib64/R/library/gamlss.dist/doc/MomentSkewKurt1.RData
/usr/lib64/R/library/gamlss.dist/help/AnIndex
/usr/lib64/R/library/gamlss.dist/help/aliases.rds
/usr/lib64/R/library/gamlss.dist/help/gamlss.dist.rdb
/usr/lib64/R/library/gamlss.dist/help/gamlss.dist.rdx
/usr/lib64/R/library/gamlss.dist/help/paths.rds
/usr/lib64/R/library/gamlss.dist/html/00Index.html
/usr/lib64/R/library/gamlss.dist/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gamlss.dist/libs/gamlss.dist.so
/usr/lib64/R/library/gamlss.dist/libs/gamlss.dist.so.avx2
/usr/lib64/R/library/gamlss.dist/libs/gamlss.dist.so.avx512
