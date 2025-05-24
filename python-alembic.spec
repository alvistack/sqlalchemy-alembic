# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-alembic
Epoch: 100
Version: 1.17.0
Release: 1%{?dist}
BuildArch: noarch
Summary: A database migration tool for SQLAlchemy
License: MIT
URL: https://github.com/sqlalchemy/alembic/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
Alembic is a database migrations tool written by the author of 
SQLAlchemy.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-alembic
Summary: A database migration tool for SQLAlchemy
Requires: python3
Requires: python3-Mako
Requires: python3-SQLAlchemy >= 1.4.0
Requires: python3-tomli
Requires: python3-typing-extensions >= 4.12
Provides: python3-alembic = %{epoch}:%{version}-%{release}
Provides: python3dist(alembic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-alembic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(alembic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-alembic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(alembic) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-alembic
Alembic is a database migrations tool written by the author of 
SQLAlchemy.

%files -n python%{python3_version_nodots}-alembic
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-alembic
Summary: A database migration tool for SQLAlchemy
Requires: python3
Requires: python3-Mako
Requires: python3-SQLAlchemy >= 1.4.0
Requires: python3-tomli
Requires: python3-typing-extensions >= 4.12
Provides: python3-alembic = %{epoch}:%{version}-%{release}
Provides: python3dist(alembic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-alembic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(alembic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-alembic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(alembic) = %{epoch}:%{version}-%{release}

%description -n python3-alembic
Alembic is a database migrations tool written by the author of 
SQLAlchemy.

%files -n python3-alembic
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-alembic
Summary: A database migration tool for SQLAlchemy
Requires: python3
Requires: python3-mako
Requires: python3-sqlalchemy >= 1.4.0
Requires: python3-tomli
Requires: python3-typing-extensions >= 4.12
Provides: python3-alembic = %{epoch}:%{version}-%{release}
Provides: python3dist(alembic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-alembic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(alembic) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-alembic = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(alembic) = %{epoch}:%{version}-%{release}

%description -n python3-alembic
Alembic is a database migrations tool written by the author of
SQLAlchemy.

%files -n python3-alembic
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
