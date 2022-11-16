Name:		texlive-gradstudentresume
Version:	38832
Release:	1
Summary:	A generic template for graduate student resumes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gradstudentresume
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gradstudentresume.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gradstudentresume.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a template for graduate students writing an
academic CV. The goal is to create a flexible template that can
be customized based on each specific individual's needs.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gradstudentresume
%doc %{_texmfdistdir}/doc/latex/gradstudentresume

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
