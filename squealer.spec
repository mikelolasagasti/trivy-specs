# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/owenrumney/squealer
%global goipath         github.com/owenrumney/squealer
Version:                1.1.0

%gometa

%global goname squealer

%global common_description %{expand:
Telling tales on you for leaking secrets!}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Telling tales on you for leaking secrets

License:        Unlicense
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/cmd/%{name} %{goipath}/cmd/%{name}

%{gobuilddir}/cmd/%{name} completion bash > %{name}.bash
%{gobuilddir}/cmd/%{name} completion fish > %{name}.fish
%{gobuilddir}/cmd/%{name} completion zsh  > %{name}.zsh

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dp %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dp %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dp %{name}.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}


%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%gopkgfiles

%changelog
%autochangelog
