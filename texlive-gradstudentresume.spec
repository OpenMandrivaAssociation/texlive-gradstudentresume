%global tl_name gradstudentresume
%global tl_revision 38832

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A generic template for graduate student resumes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gradstudentresume
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gradstudentresume.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gradstudentresume.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers a template for graduate students writing an academic
CV. The goal is to create a flexible template that can be customized
based on each specific individual's needs.

