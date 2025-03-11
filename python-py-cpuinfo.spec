#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Get CPU info with pure Python 2
Summary(pl.UTF-8):	Pobieranie informacji o CPU w czystym Pythonie 2
Name:		python-py-cpuinfo
Version:	8.0.0
Release:	7
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/py-cpuinfo/
Source0:	https://files.pythonhosted.org/packages/source/p/py-cpuinfo/py-cpuinfo-%{version}.tar.gz
# Source0-md5:	cf3bec89839a0bf18c5f6c1c18aaee10
URL:		https://github.com/workhorsy/py-cpuinfo
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work
without any extra programs or libraries, beyond what your OS provides.
It does not require any compilation (C/C++, assembly, et cetera) to
use. It works with Python 2 and 3.

%description -l pl.UTF-8
Py-cpuinfo pobiera informacje o CPU z poziomu czystego Pythona.
Powinien działać bez dodatkowych programów czy bibliotek, tylko z tym,
co udostępnia system operacyjny. Nie wymaga żadnej kompilacji (C/C++,
asemblera itp.). Działa z Pythonem 2 i 3.

%package -n python3-py-cpuinfo
Summary:	Get CPU info with pure Python 3
Summary(pl.UTF-8):	Pobieranie informacji o CPU w czystym Pythonie 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-py-cpuinfo
Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work
without any extra programs or libraries, beyond what your OS provides.
It does not require any compilation (C/C++, assembly, et cetera) to
use. It works with Python 2 and 3.

%description -n python3-py-cpuinfo -l pl.UTF-8
Py-cpuinfo pobiera informacje o CPU z poziomu czystego Pythona.
Powinien działać bez dodatkowych programów czy bibliotek, tylko z tym,
co udostępnia system operacyjny. Nie wymaga żadnej kompilacji (C/C++,
asemblera itp.). Działa z Pythonem 2 i 3.

%prep
%setup -q -n py-cpuinfo-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} test_suite.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} test_suite.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cpuinfo{,-py2}

%py_postclean
%endif

%if %{with python3}
%py3_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cpuinfo{,-py3}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.rst
%attr(755,root,root) %{_bindir}/cpuinfo-py2
%{py_sitescriptdir}/cpuinfo
%{py_sitescriptdir}/py_cpuinfo-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-py-cpuinfo
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.rst
%attr(755,root,root) %{_bindir}/cpuinfo-py3
%{py3_sitescriptdir}/cpuinfo
%{py3_sitescriptdir}/py_cpuinfo-%{version}-py*.egg-info
%endif
