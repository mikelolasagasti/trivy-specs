# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/liamg/memoryfs
%global goipath         github.com/liamg/memoryfs
Version:                1.4.2

%gometa

%global common_description %{expand:
In-memory filesystem implementation of io/fs.FS.}

%global golicenses      LICENSE
%global godocs          _examples README.md

Name:           %{goname}
Release:        %autorelease
Summary:        In-memory filesystem implementation of io/fs.FS

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
