%global tl_name chemformula-ru
%global tl_revision 71883

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Using the chemformula package with babel-russian settings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemformula-ru
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemformula-ru.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemformula-ru.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The chemformula package and babel-russian settings (russian.ldf) both
define macros named "\ch". The package chemformula-ru undefines babel's
macro to prevent an error when both packages are loaded together.
Optionally it redefines the \cosh macro to print the hyperbolic cosine
in Russian notation and/or defines a new macro \Ch for that purpose.

