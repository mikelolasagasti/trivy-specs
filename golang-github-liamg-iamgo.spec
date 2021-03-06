# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/liamg/iamgo
%global goipath         github.com/liamg/iamgo
Version:                0.0.9

%gometa

%global common_description %{expand:
Parse/assemble AWS IAM policy documents and their various quirks.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Parse/assemble AWS IAM policy documents and their various quirks

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
