# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/go-git/go-git
%global goipath         github.com/go-git/go-git/v5
Version:                5.4.2

%gometa

%global common_description %{expand:
A highly extensible Git implementation in pure Go.}

%global golicenses      LICENSE
%global godocs          _examples CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md COMPATIBILITY.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A highly extensible Git implementation in pure Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/emirpasic/gods/trees/binaryheap)
BuildRequires:  golang(github.com/go-git/gcfg)
BuildRequires:  golang(github.com/go-git/go-billy/v5)
BuildRequires:  golang(github.com/go-git/go-billy/v5/osfs)
BuildRequires:  golang(github.com/go-git/go-billy/v5/util)
BuildRequires:  golang(github.com/imdario/mergo)
BuildRequires:  golang(github.com/jbenet/go-context/io)
BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/kevinburke/ssh_config)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/ProtonMail/go-crypto/openpgp)
BuildRequires:  golang(github.com/sergi/go-diff/diffmatchpatch)
BuildRequires:  golang(github.com/xanzy/ssh-agent)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/crypto/ssh/knownhosts)
BuildRequires:  golang(golang.org/x/net/proxy)
BuildRequires:  golang(golang.org/x/sys/execabs)
BuildRequires:  golang(gopkg.in/check.v1)

%if %{with check}
# Tests
BuildRequires:  git
BuildRequires:  golang(github.com/armon/go-socks5)
BuildRequires:  golang(github.com/gliderlabs/ssh)
BuildRequires:  golang(github.com/go-git/go-billy/v5/memfs)
BuildRequires:  golang(github.com/go-git/go-git-fixtures/v4)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/ProtonMail/go-crypto/openpgp/armor)
BuildRequires:  golang(github.com/ProtonMail/go-crypto/openpgp/errors)
BuildRequires:  golang(golang.org/x/text/unicode/norm)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cli/go-git; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

#%%if %{with check}
#%%check
#%%gocheck -r auth_method
#%%endif

%files
%license LICENSE
%doc _examples CODE_OF_CONDUCT.md CONTRIBUTING.md README.md COMPATIBILITY.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Aug 17 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 5.4.2-1%{?dist}
- Initial package
