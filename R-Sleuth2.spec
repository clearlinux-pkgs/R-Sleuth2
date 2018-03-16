#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Sleuth2
Version  : 2.0.4
Release  : 1
URL      : https://cran.r-project.org/src/contrib/Sleuth2_2.0-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Sleuth2_2.0-4.tar.gz
Summary  : Data Sets from Ramsey and Schafer's "Statistical Sleuth (2nd
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-evaluate
Requires: R-highr
BuildRequires : R-evaluate
BuildRequires : R-highr
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n Sleuth2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521184554

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521184554
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Sleuth2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Sleuth2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Sleuth2
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library Sleuth2|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/Sleuth2/doc/chapter01-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter01-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter02-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter02-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter03-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter03-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter04-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter04-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter05-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter05-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter06-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter06-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter07-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter07-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter08-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter08-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter09-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter09-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter10-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter10-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter11-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter11-HortonMosaic.pdf
/usr/lib64/R/library/Sleuth2/doc/chapter12-HortonMosaic.Rnw
/usr/lib64/R/library/Sleuth2/doc/chapter12-HortonMosaic.pdf
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
