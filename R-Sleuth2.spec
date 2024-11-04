#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: fae1327
#
Name     : R-Sleuth2
Version  : 2.0.7
Release  : 50
URL      : https://cran.r-project.org/src/contrib/Sleuth2_2.0-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Sleuth2_2.0-7.tar.gz
Summary  : Data Sets from Ramsey and Schafer's "Statistical Sleuth (2nd
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n Sleuth2
pushd ..
cp -a Sleuth2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1706203690

%install
export SOURCE_DATE_EPOCH=1706203690
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Sleuth2/DESCRIPTION
/usr/lib64/R/library/Sleuth2/INDEX
/usr/lib64/R/library/Sleuth2/Meta/Rd.rds
/usr/lib64/R/library/Sleuth2/Meta/data.rds
/usr/lib64/R/library/Sleuth2/Meta/features.rds
/usr/lib64/R/library/Sleuth2/Meta/hsearch.rds
/usr/lib64/R/library/Sleuth2/Meta/links.rds
/usr/lib64/R/library/Sleuth2/Meta/nsInfo.rds
/usr/lib64/R/library/Sleuth2/Meta/package.rds
/usr/lib64/R/library/Sleuth2/Meta/vignette.rds
/usr/lib64/R/library/Sleuth2/NAMESPACE
/usr/lib64/R/library/Sleuth2/R/Sleuth2
/usr/lib64/R/library/Sleuth2/R/Sleuth2.rdb
/usr/lib64/R/library/Sleuth2/R/Sleuth2.rdx
/usr/lib64/R/library/Sleuth2/data/Rdata.rdb
/usr/lib64/R/library/Sleuth2/data/Rdata.rds
/usr/lib64/R/library/Sleuth2/data/Rdata.rdx
/usr/lib64/R/library/Sleuth2/doc/Sleuth2-manual.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter01-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter01-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter01-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter02-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter02-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter02-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter03-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter03-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter03-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter04-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter04-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter04-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter05-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter05-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter05-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter06-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter06-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter06-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter07-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter07-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter07-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter08-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter08-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter08-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter09-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter09-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter09-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter10-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter10-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter10-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter11-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter11-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter11-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter12-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter12-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter12-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter13-HortonMosaic.R
/usr/lib64/R/library/Sleuth2/doc/chapter13-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter13-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/index.html
/usr/lib64/R/library/Sleuth2/help/AnIndex
/usr/lib64/R/library/Sleuth2/help/Sleuth2.rdb
/usr/lib64/R/library/Sleuth2/help/Sleuth2.rdx
/usr/lib64/R/library/Sleuth2/help/aliases.rds
/usr/lib64/R/library/Sleuth2/help/paths.rds
/usr/lib64/R/library/Sleuth2/html/00Index.html
/usr/lib64/R/library/Sleuth2/html/R.css
