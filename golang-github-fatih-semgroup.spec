# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/fatih/semgroup
%global goipath         github.com/fatih/semgroup
Version:                1.2.0

%gometa

%global common_description %{expand:
Like errgroup/waitgroup, but only runs a maximum of tasks at any time.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Like errgroup/waitgroup, but only runs a maximum of tasks at any time

# Upstream license specification: BSD-3-Clause
License:        BSD
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