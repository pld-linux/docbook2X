%include	/usr/lib/rpm/macros.perl
Summary:	Docbook2man and docbook2info conversion tools
Summary(pl):	Narzêdzia do konwersji docbook do man i info
Name:		docbook2X
Version:	0.8.2
Release:	1
License:	GPL
Group:		Applications/Publishing/SGML
Source0:	http://dl.sourceforge.net/docbook2x/%{name}-%{version}.tar.gz
# Source0-md5:	60e9837d7f4f343f567a5da499d13be0
Source1:	%{name}-docbook2man
Requires:	sgml-common
Requires:	sgmlparser
Requires:	docbook-dtd
URL:		http://docbook2x.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Steve Cheng's docbook2man-spec conversion tools. Usage: docbook2man
manpage.sgml. Prints name(s) of created manpage(s), or some error
messages.

%description -l pl
Narzêdzia do konwersji docbook2man Steve Cheng'a. U¿ycie: docbook2man
manpage.sgml. Wypisuje nazwy stworzonych w bie¿±cym katalogu stron
man, lub komunikat o b³êdzie.

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
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{perl_privlib}/XML/Handler/Templates.pm
%{_mandir}/man1/*
%{_infodir}/*.info*
