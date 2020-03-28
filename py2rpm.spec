%global pypi_name pyp2rpm

Name:           pyp2rpm
Version:        3.3.3
Release:        1
Group:          Development/Python
Summary:        Convert Python packages to RPM SPECFILES

License:        MIT
URL:            https://github.com/fedora-python/pyp2rpm
Source0:        https://pypi.python.org/packages/89/83/efcc943c2aa19cb348433b08dcd7a055e58bb4db224d41769b2a33968949/pyp2rpm-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-flexmock >= 0.9.3
BuildRequires:  python-pytest
BuildRequires:  python-pip
BuildRequires:  python-wheel
 
Requires:       python-jinja2
Requires:       python-setuptools
Requires:       python-click

%description
Convert Python packages to RPM SPECFILES. 
Packages can be downloaded from PyPI and the product 
is in line with Fedora Packaging Guidelines or Mageia Python Policy


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
#%%{__python3} setup.py build


%install
%py3_install
#%%{__python3} setup.py install --skip-build --root %{buildroot}


%files
%doc LICENSE
%{_bindir}/pyp2rpm
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

