#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Upload
Summary:	CGI::Upload - CGI class for handling browser file uploads
Summary(pl):	CGI::Upload - klasa CGI do obs�ugi przesy�u plik�w przez przegl�dark�
Name:		perl-CGI-Upload
Version:	1.05
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	30ae6bb548d9806b74ff3e2fde8fcdfc
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
CGI::Upload udost�pnia prosty i bezpieczny spos�b do obs�ugi plik�w,
presy�anych przez przegl�dark� w zapytaniach multipart/form-data.
Podstawow� przewag� tego modu�u nad innymi istniej�cymi modu�ami jest
pojedy�czy interfejs, dostarczaj�cy najcz�ciej wymaganych informacji,
zwi�zanych z przesy�em plik�w przy u�yciu zapyta� multipart/form-data.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
