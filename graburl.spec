Summary:	Small program that can download files using HTTP
Summary(pl.UTF-8):	Mały program do ściągania plików przy użyciu HTTP
Name:		graburl
Version:	2.0.1
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.ibiblio.org/pub/Linux/apps/www/mirroring/%{name}-%{version}.tar.gz
# Source0-md5:	1dda06b68d9fffb4a417a7527e483917
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GrabURL is a small program that can download files using HTTP. It
maintains an internal list of urls and can scan HTML files downloaded
to add urls recursively. It can use regular expression patterns to be
matched to add an URL, saves progress to a "workfile" to continue
later (ie after a break with Ctrl-C).

GrabURL is used in afraid.org update-scripts.

%description -l pl.UTF-8
GrabURL jest małym programem, który potrafi ściągać pliki używając
HTTP. Zarządza wewnętrzną listą URL-i i może skanować ściągnięte pliki
HTML aby dodać URL-e rekursywnie. Może używać wyrażeń regularnych do
dopasowania dodawanych URL-i, zapisuje postęp do "pliku roboczego",
aby móc kontynuować później (np. po przerwaniu przy pomocy Ctrl-C).

GrabURL jest wykorzystywany w skryptach aktualizujących afraid.org.

%prep
%setup -q -n %{name}

%build
%{__make} -C src linux \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I./libgurl"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install -C src/graburl $RPM_BUILD_ROOT%{_bindir}
install graburlrc.example $RPM_BUILD_ROOT%{_sysconfdir}/graburlrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt Changes.txt GrabURL.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/graburlrc
%attr(755,root,root) %{_bindir}/*
