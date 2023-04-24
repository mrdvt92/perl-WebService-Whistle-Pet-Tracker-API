Name:           perl-WebService-Whistle-Pet-Tracker-API
Version:        0.02
Release:        2%{?dist}
Summary:        Perl interface to access the Whistle Pet Tracker Web Service
License:        MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/WebService-Whistle-Pet-Tracker-API/
Source0:        http://www.cpan.org/modules/by-module/WebService/WebService-Whistle-Pet-Tracker-API-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(JSON::XS)
Requires:       perl(HTTP::Tiny)
Requires:       perl(JSON::XS)
Requires:       perl(Tie::IxHash)
Requires:       perl(Net::MQTT::Simple)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Perl interface to access the Whistle Pet Tracker Web Service

%prep
%setup -q -n WebService-Whistle-Pet-Tracker-API-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
