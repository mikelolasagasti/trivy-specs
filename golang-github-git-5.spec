# Generated by go2rpm 1.6.0
# Needs network access to Github
%bcond_with check
%global debug_package %{nil}

# https://github.com/go-git/go-git
%global goipath         github.com/go-git/go-git/v5
Version:                5.4.2
%global commit          bc1f419cebcf7505db31149fa459e9e3f8260e00

%gometa

%global common_description %{expand:
A highly extensible Git implementation in pure Go.}

%global golicenses      LICENSE
%global godocs          _examples CODE_OF_CONDUCT.md COMPATIBILITY.md\\\
                        CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A highly extensible Git implementation in pure Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
# No testdata packed
rm -rfv plumbing/transport/ssh/auth_method_test.go

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