#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	CGI
%define		pnam	Upload
Summary:	CGI::Upload - CGI class for handling browser file uploads
Summary(pl.UTF-8):	CGI::Upload - klasa CGI do obsługi przesyłu plików przez przeglądarkę
Name:		perl-CGI-Upload
Version:	1.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2f599b179c49e3d843351b77d94e5777
URL:		http://search.cpan.org/dist/CGI-Upload/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
#BuildRequires:	perl-CGI
BuildRequires:	perl-File-MMagic
BuildRequires:	perl-HTTP-BrowserDetect
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Upload has been written to provide a simple and secure manner by
which to handle files uploaded in multipart/form-data requests through
a web browser.  The primary advantage which this module offers over
existing modules is the single interface providing the most often required
information regarding files uploaded through multipart/form-data requests.

%description -l pl.UTF-8
CGI::Upload udostępnia prosty i bezpieczny sposób do obsługi plików,
przesyłanych przez przeglądarkę w zapytaniach multipart/form-data.
Podstawową przewagą tego modułu nad innymi istniejącymi modułami jest
pojedyńczy interfejs, dostarczający najczęściej wymaganych informacji,
związanych z przesyłem plików przy użyciu zapytań multipart/form-data.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
