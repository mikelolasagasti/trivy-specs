# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/FairwindsOps/pluto
%global goipath         github.com/fairwindsops/pluto/v3
Version:                5.5.1

%gometa

%global common_description %{expand:
A cli tool to help discover deprecated apiVersions in Kubernetes.}

%global golicenses      LICENSE
%global godocs          docs CODE_OF_CONDUCT.md README.md examples

Name:           %{goname}
Release:        %autorelease
Summary:        A cli tool to help discover deprecated apiVersions in Kubernetes

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/pluto %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc docs CODE_OF_CONDUCT.md README.md examples
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
