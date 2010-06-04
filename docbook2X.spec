%include	/usr/lib/rpm/macros.perl
Summary:	Docbook2man and docbook2info conversion tools
Summary(pl.UTF-8):	Narzędzia do konwersji docbook do man i info
Name:		docbook2X
Version:	0.8.8
Release:	4
License:	MIT
Group:		Applications/Publishing/SGML
Source0:	http://dl.sourceforge.net/docbook2x/%{name}-%{version}.tar.gz
# Source0-md5:	b9b76a6af198c4f44574cfd17a322f01
# note: Source1 not used now
Source1:	%{name}-docbook2man
URL:		http://docbook2x.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-devel
BuildRequires:	texinfo
Requires:	docbook-dtd
Requires:	sgml-common
Requires:	sgmlparser
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Steve Cheng's docbook2X tools convert DocBook documents into man pages
and Texinfo documents.

%description -l pl.UTF-8
Narzędzia do konwersji docbook2X Steve'a Chenga konwertują dokumenty
DocBooka na strony manuala i dokumenty Texinfo.

%prep
%setup -q

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

mv $RPM_BUILD_ROOT%{_bindir}/{docbook2man,docbook2X2man}
mv $RPM_BUILD_ROOT%{_mandir}/man1/{docbook2man,docbook2X2man}.1
mv $RPM_BUILD_ROOT%{_bindir}/{docbook2texi,docbook2X2texi}
mv $RPM_BUILD_ROOT%{_mandir}/man1/{docbook2texi,docbook2X2texi}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README THANKS TODO doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*.info*
