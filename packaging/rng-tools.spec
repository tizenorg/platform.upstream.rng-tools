Name:           rng-tools
Version:        4
Release:        0
License:        GPL-2.0+
Summary:        A random number generator daemon
Url:            http://sourceforge.net/projects/gkernel
Group:          Development/Tools
Source0:        %{name}-%{version}.tar.gz
Source1:        rngd.service

%description
A daemon that monitors a hardware random number generator, and supplies entropy
from that to the system kernel's /dev/random machinery.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
install -Dm0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/systemd/system/rngd.service

%docs_package

%files
%license COPYING
%{_bindir}/rngtest
%{_prefix}/lib/systemd/system/rngd.service
%{_sbindir}/rngd
