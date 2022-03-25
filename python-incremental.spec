# TODO: apidocs (BR: pydoctor), tests (BR: twisted.trial >= 16.4.0, click >= 6.0)
#
# Conditional build:
%bcond_with	doc	# API documentation (pydoctor based)
%bcond_with	tests	# unit tests (require Twisted)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Library that versions Python projects
Summary(pl.UTF-8):	Biblioteka wersjonująca projekty w Pythonie
Name:		python-incremental
Version:	21.3.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/incremental/
Source0:	https://files.pythonhosted.org/packages/source/i/incremental/incremental-%{version}.tar.gz
# Source0-md5:	9f7ad12e0c05a12cee52a7350976c4e3
URL:		https://pypi.org/project/incremental/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-click >= 6.0
BuildRequires:	python-twisted >= 16.4.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-click >= 6.0
BuildRequires:	python3-twisted >= 16.4.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	pydoctor
%endif
# replace with other requires if defined in setup.py
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Incremental is a small library that versions your Python projects.

%description -l pl.UTF-8
Incremental to mała biblioteka do wersjonowania projektów w Pythonie.

%package -n python3-incremental
Summary:	Library that versions Python projects
Summary(pl.UTF-8):	Biblioteka wersjonująca projekty w Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-incremental
Incremental is a small library that versions your Python projects.

%description -n python3-incremental -l pl.UTF-8
Incremental to mała biblioteka do wersjonowania projektów w Pythonie.

%package apidocs
Summary:	API documentation for Python incremental module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona incremental
Group:		Documentation

%description apidocs
API documentation for Python incremental module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona incremental.

%prep
%setup -q -n incremental-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
trial-2 incremental
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
trial-3 incremental
%endif
%endif

%if %{with doc}
pydoctor -q --project-name incremental src/incremental
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst
%{py_sitescriptdir}/incremental
%{py_sitescriptdir}/incremental-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-incremental
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst
%{py3_sitescriptdir}/incremental
%{py3_sitescriptdir}/incremental-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc # TODO
%endif
