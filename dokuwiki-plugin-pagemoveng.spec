%define		plugin		pagemoveng
Summary:	DokuWiki PageMove plugin
Summary(pl.UTF-8):	Wtyczka PageMove dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20110322
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/dokufreaks/plugin-%{plugin}/tarball/master#/%{plugin}.tgz
# Source0-md5:	9355168bf7f2526dbdce0a33fc3ff2a2
URL:		https://github.com/dokufreaks/plugin-pagemoveng
BuildRequires:	sed >= 4.0
Requires:	dokuwiki >= 20060309
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

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
%setup -qc
# for github urls:
mv *-%{plugin}-*/* .
%{__rm} *-%{plugin}-*/.gitignore

version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
#	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.css
%{plugindir}/*.js
%{plugindir}/*.php
%{plugindir}/*.txt
