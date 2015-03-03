%global gemname hammer_cli_gutterball
%global confdir hammer

%if 0%{?rhel} < 7
%global gem_dir /usr/lib/ruby/gems/1.8
%endif

%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}
Summary: Gutterball commands for Hammer
Name: rubygem-%{gemname}
Version: 1.0.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/Katello/hammer-cli-gutterball
Source0: %{gemname}-%{version}.gem
Source1: gutterball.yml

%if !( 0%{?rhel} > 6 || 0%{?fedora} > 18 )
Requires: ruby(abi)
%endif
Requires: ruby(rubygems)
Requires: rubygem(hammer_cli) >= 0.1.1
BuildRequires: ruby(rubygems)
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires: rubygems-devel
%endif
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Hammer-CLI-Gutterball is a Hammer module which provides additional functionality for use with the foreman_gutterball plugin.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d
install -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/gutterball.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{geminstdir}
%{geminstdir}/
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/gutterball.yml
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}

%changelog
* Tue Mar 03 2015 Adam Price <komidore64@gmail.com> 1.0.0-1
- new package built with tito

