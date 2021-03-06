# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/apparentlymart/go-cidr
%global goipath         github.com/apparentlymart/go-cidr
Version:                1.1.0

%gometa

%global common_description %{expand:
Go library for various manipulations of CIDR netmasks and their associated
addresses.}

%global golicenses      LICENSE
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library for various manipulations of CIDR netmasks and their associated addresses

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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
* Tue Aug 17 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.1.0-1
- Initial package

