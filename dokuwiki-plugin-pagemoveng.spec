%define		_plugin		pagemove
Summary:	DokuWiki PageMove plugin
Summary(pl.UTF-8):	Wtyczka PageMove dla DokuWiki
Name:		dokuwiki-plugin-%{_plugin}
Version:	0.9.15a
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.isection.co.uk/lib/exe/fetch.php?media=pagemove_20070722.zip
# Source0-md5:	f2cc2a57d40b877a335b52009e4cc072
URL:		http://www.isection.co.uk/doku.php
BuildRequires:	sed >= 4.0
Requires:	dokuwiki >= 20060309
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_plugindir	%{_dokudir}/lib/plugins/%{_plugin}

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
%setup -q -n %{_plugin}

# undos the source
%{__sed} -i -e 's,\r$,,' admin.php

mv lang/cs/pagemove.txt{.txt,}
mv lang/es/pagemove.txt{.txt,}
mv lang/pl/pagemove.txt{.txt,}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}
cp -a . $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_plugindir}
%{_plugindir}/admin.php
%dir %{_plugindir}/lang
%{_plugindir}/lang/en
%lang(cs) %{_plugindir}/lang/cs
%lang(de) %{_plugindir}/lang/de
%lang(es) %{_plugindir}/lang/es
%lang(fr) %{_plugindir}/lang/fr
%lang(lv) %{_plugindir}/lang/lv
%lang(nl) %{_plugindir}/lang/nl
%lang(pl) %{_plugindir}/lang/pl
%lang(ru) %{_plugindir}/lang/ru
%lang(sl) %{_plugindir}/lang/sl
%lang(zh_CN) %{_plugindir}/lang/zh
