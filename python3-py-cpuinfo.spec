#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Get CPU info with pure Python
Summary(pl.UTF-8):	Pobieranie informacji o CPU w czystym Pythonie
Name:		python3-py-cpuinfo
Version:	9.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/py-cpuinfo/
Source0:	https://files.pythonhosted.org/packages/source/p/py-cpuinfo/py-cpuinfo-%{version}.tar.gz
# Source0-md5:	b323b82dddf2e47bc554c124586c16dc
URL:		https://github.com/workhorsy/py-cpuinfo
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work
without any extra programs or libraries, beyond what your OS provides.
It does not require any compilation (C/C++, assembly, et cetera) to
use.

%description -l pl.UTF-8
Py-cpuinfo pobiera informacje o CPU z poziomu czystego Pythona.
Powinien działać bez dodatkowych programów czy bibliotek, tylko z tym,
co udostępnia system operacyjny. Nie wymaga żadnej kompilacji (C/C++,
asemblera itp.).

%prep
%setup -q -n py-cpuinfo-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} test_suite.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cpuinfo{,-py3}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.rst
%attr(755,root,root) %{_bindir}/cpuinfo-py3
%{py3_sitescriptdir}/cpuinfo
%{py3_sitescriptdir}/py_cpuinfo-%{version}-py*.egg-info
