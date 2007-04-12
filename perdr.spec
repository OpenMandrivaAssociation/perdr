Name:           perdr
Version:        0.0104
Release:        %mkrel 1
Epoch:          0
Summary:        Windows Portable Executable disassembler
License:        GPL
Group:          Development/Other
URL:            http://perdr.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/perdr/perdr-%{version}.tar.bz2
Patch0:         perdr-0.0104-build.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
perdr is a disassembler for the Windows Portable Executable format.
It reverses module info and code to screen. It supports the full
Pentium III and instruction sets.

%prep
%setup -q
%patch0 -p1

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
%{_mandir}/man1/*


