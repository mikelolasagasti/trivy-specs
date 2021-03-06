# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/zclconf/go-cty-yaml
%global goipath         github.com/zclconf/go-cty-yaml
Version:                1.0.2

%gometa

%global common_description %{expand:
YAML marshalling and unmarshalling for go-cty.}

%global golicenses      LICENSE.libyaml NOTICE LICENSE
%global godocs          CHANGELOG.md

Name:           %{goname}
Release:        %autorelease
Summary:        YAML marshalling and unmarshalling for go-cty

# Upstream license specification: Apache-2.0 and MIT
License:        ASL 2.0 and MIT
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
