%define		plugin		pagemove
Summary:	DokuWiki PageMove plugin
Summary(pl.UTF-8):	Wtyczka PageMove dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	0.9.15a
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.isection.co.uk/lib/exe/fetch.php?media=pagemove_20070722.zip
# Source0-md5:	f2cc2a57d40b877a335b52009e4cc072
Patch0:		%{name}-redirectlinks.patch
Patch1:		%{name}-selflinks.patch
URL:		http://www.isection.co.uk/doku.php
BuildRequires:	sed >= 4.0
Requires:	dokuwiki >= 20060309
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin is designed for moving and renaming pages within your Wiki
whilst maintaining the integrity of links to and from the page.

In full you can:
- Rename a page.
- Move a page to an existing namspace.
- Move a page to a new namespace.
- A combination of the above.

%description -l pl.UTF-8
Ta wtyczka służy do przesuwania i zmiany nazw stron wewnątrz Wiki z
zachowaniem integralności odnośników z i do strony.

W zupełności można:
- usunąć stronę,
- przenieść stronę do istniejącej przestrzeni nazw,
- przenieść stronę do nowej przestrzeni nazw,
- wykonać połączenie powyższych.

%prep
%setup -q -n %{plugin}
# undos the source
%{__sed} -i -e 's,\r$,,' admin.php

%patch0 -p1
%patch1 -p1
mv lang/cs/pagemove.txt{.txt,}
mv lang/es/pagemove.txt{.txt,}
mv lang/pl/pagemove.txt{.txt,}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/admin.php
%dir %{plugindir}/lang
%{plugindir}/lang/en
%lang(cs) %{plugindir}/lang/cs
%lang(de) %{plugindir}/lang/de
%lang(es) %{plugindir}/lang/es
%lang(fr) %{plugindir}/lang/fr
%lang(lv) %{plugindir}/lang/lv
%lang(nl) %{plugindir}/lang/nl
%lang(pl) %{plugindir}/lang/pl
%lang(ru) %{plugindir}/lang/ru
%lang(sl) %{plugindir}/lang/sl
%lang(zh_CN) %{plugindir}/lang/zh
