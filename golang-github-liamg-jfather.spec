# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/liamg/jfather
%global goipath         github.com/liamg/jfather
Version:                0.0.7

%gometa

%global common_description %{expand:
JSON parsing with extra metadata.}

%global golicenses      LICENSE
%global godocs          _examples README.md

Name:           %{goname}
Release:        %autorelease
Summary:        JSON parsing with extra metadata

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
