# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/aquasecurity/go-dep-parser
%global goipath         github.com/aquasecurity/go-dep-parser
%global commit          dda1673181319dd5f216ba4324e75ab98bdc296f

%gometa

%global common_description %{expand:
Dependency Parser for Multiple Programming Languages.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Dependency Parser for Multiple Programming Languages

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/hashicorp/go-retryablehttp)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(golang.org/x/xerrors)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Aug 17 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0-0.1%{?dist}.20210817gitdda1673
- Initial package

