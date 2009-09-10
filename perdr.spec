Name:           perdr
Version:        0.0108
Release:        %mkrel 5
Epoch:          0
Summary:        Windows Portable Executable disassembler
License:        GPLv2+
Group:          Development/Other
URL:            http://perdr.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/perdr/perdr-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
perdr is a disassembler for the Windows Portable Executable format.
It reverses module info and code to screen. It supports the full
Pentium III and instruction sets.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(0755,root,root) %{_bindir}/perdr
%dir %{_datadir}/perdr
%{_datadir}/perdr/winapifn.lst
%{_mandir}/man1/*

