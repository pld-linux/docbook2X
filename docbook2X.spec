%include	/usr/lib/rpm/macros.perl
Summary:	Docbook2man and docbook2info conversion tools
Summary(pl):	Narzêdzia do konwersji docbook do man i info
Name:		docbook2X
Version:	0.8.5
Release:	3
License:	MIT
Group:		Applications/Publishing/SGML
Source0:	http://dl.sourceforge.net/docbook2x/%{name}-%{version}.tar.gz
# Source0-md5:	05d549646ac11caba6c7f1e07ced33e3
# note: Source1 not used now
Source1:	%{name}-docbook2man
URL:		http://docbook2x.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-XML-SAX
Requires:	docbook-dtd
Requires:	sgml-common
Requires:	sgmlparser
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Steve Cheng's docbook2X tools convert DocBook documents into man pages
and Texinfo documents.

%description -l pl
Narzêdzia do konwersji docbook2X Steve'a Chenga konwertuj± dokumenty
DocBooka na strony manuala i dokumenty Texinfo.

%prep
%setup -q

%{__perl} -pi -e 's/install_perl/install_vendor/' perl/Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README THANKS TODO doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{perl_vendorlib}/XML/Handler/SGMLSpl.pm
%{_mandir}/man1/*
%{_infodir}/*.info*
