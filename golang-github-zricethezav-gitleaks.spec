# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/zricethezav/gitleaks
%global goipath         github.com/zricethezav/gitleaks
Version:                7.6.0

%gometa

%global common_description %{expand:
Scan git repos (or files) for secrets using regex and entropy}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Scan git repos (or files) for secrets using regex and entropy

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/go-git/go-git/v5)
BuildRequires:  golang(github.com/go-git/go-git/v5/plumbing)
BuildRequires:  golang(github.com/go-git/go-git/v5/plumbing/format/diff)
BuildRequires:  golang(github.com/go-git/go-git/v5/plumbing/object)
BuildRequires:  golang(github.com/go-git/go-git/v5/plumbing/storer)
BuildRequires:  golang(github.com/go-git/go-git/v5/plumbing/transport)
BuildRequires:  golang(github.com/go-git/go-git/v5/plumbing/transport/http)
BuildRequires:  golang(github.com/go-git/go-git/v5/plumbing/transport/ssh)
BuildRequires:  golang(github.com/go-git/go-git/v5/storage/memory)
BuildRequires:  golang(github.com/hako/durafmt)
BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/sergi/go-diff/diffmatchpatch)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(golang.org/x/sync/errgroup)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/gitleaks %{goipath}/bin/gitleaks

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
%doc examples README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Sep 06 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 7.6.0-1
- Initial package
