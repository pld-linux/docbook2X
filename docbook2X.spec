%include	/usr/lib/rpm/macros.perl
Summary:	Docbook2man and docbook2info conversion tools
Summary(pl):	Narzêdzia do konwersji docbook do man i info 
Name:		docbook2X
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
Source0:	http://shell.ipoline.com/~elmert/hacks/docbook2X/%{name}.tar.gz
Source1:	docbook2X-docbook2man
Requires:	sgml-common
Requires:	sgmlparser
Requires:	docbook-dtd
URL:		http://shell.ipoline.com/~elmert/hacks/docbook2X/	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Steve Cheng's docbook2man-spec conversion tools. Usage: docbook2man
manpage.sgml. Prints name(s) of created manpage(s), or some error
messages.

%description -l pl 
Narzêdzia do konwersji docbook2man Steve Cheng'a. U¿ycie: docbook2man
manpage.sgml. Wypisuje nazwy stworzonych w bie¿±cym katalogu stron man,
lub komunikat o b³êdzie.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}

install  *spec.pl *links.pl $RPM_BUILD_ROOT%{_datadir}/%{name}
install  %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/docbook2man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/%{name}/*spec.pl
%attr(755,root,root) %{_datadir}/%{name}/*links.pl
%attr(755,root,root) %{_bindir}/*
