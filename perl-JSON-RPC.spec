#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	JSON
%define		pnam	RPC
Summary:	JSON::RPC - JSON RPC 2.0 Server Implementation
#Summary(pl.UTF-8):	
Name:		perl-JSON-RPC
Version:	1.01
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/JSON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	802d5bb488f3587f16aa69e8c002132b
URL:		http://search.cpan.org/dist/JSON-RPC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::Accessor::Lite)
BuildRequires:	perl(JSON)
BuildRequires:	perl(Plack)
BuildRequires:	perl(Router::Simple)
BuildRequires:	perl-libwww
BuildRequires:	perl(Plack::Request)
BuildRequires:	perl(Plack::Test)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON::RPC is a set of modules that implment JSON RPC 2.0 protocol.

    If you are using old JSON::RPC code (up to 0.96), DO NOT EXPECT
    YOUR CODE TO WORK WITH THIS VERSION. THIS VERSION IS 
    ****BACKWARDS INCOMPATIBLE****



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/JSON/*.pm
%{perl_vendorlib}/JSON/RPC
%{_mandir}/man3/*
