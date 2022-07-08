# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/aquasecurity/defsec
%global goipath         github.com/aquasecurity/defsec
Version:                0.68.9

%gometa

%global common_description %{expand:
DefSec is a set of tools for scanning IaC and configuration files.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        DefSec is a set of tools for scanning IaC and configuration files

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
