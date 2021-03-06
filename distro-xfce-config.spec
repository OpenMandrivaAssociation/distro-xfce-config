%define snap 20180408

Summary:	%{distribution} xfce configuration files
Name:		distro-xfce-config
Version:	3.0
Release:	4
Epoch:		1
Group:		Graphical desktop/Xfce
License:	GPLv2+
URL:		https://abf.io/omv_software/distro-xfce-config
Source0:	https://abf.io/omv_software/distro-xfce-config/%{name}-%{snap}.tar.xz
Obsoletes:	xfce-config
%rename	mandriva-xfce-config
BuildArch:	noarch

%description
This package regroups all specific configuration
files for %{distribution} Xfce desktop environment.

%package -n %{name}-common
Summary:	%{distribution} xfce common configuration files
Group:		Graphical desktop/Xfce
Requires(pre):	chkconfig
Requires:	adwaita-icon-theme
Requires:	distro-release-common
%rename		mandriva-xfce-config-common

Requires(pre):	xfconf
Requires(preun):	xfconf
#Requires:	xfce4-weather-plugin
#Requires:	xfce4-cpugraph-plugin
%if %mdkversion > 2008100
Conflicts:	xfce-utils <= 4.4.2-22
Conflicts:	xfce4-power-manager < 0.6.4-3
Conflicts:	xfdesktop < 4.6.0-4
%endif

%description -n %{name}-common
This package regroups all common configuration files
for %{distribution} Xfce desktop environment.

%package -n %{name}-OpenMandriva
Summary:	%distribution xfce configuration files
Group:		Graphical desktop/Xfce
Url:		https://abf.io/omv_software/distro-xfce-config
Requires:	distro-release-OpenMandriva
Requires:	distro-theme-OpenMandriva
Requires(pre):	%{name}-common = %{EVRD}
Requires(preun):	%{name}-common = %{EVRD}
%rename	mandriva-xfce-config-Free
%rename	mandriva-xfce-config-Flash
%rename	mandriva-xfce-config-One
%rename	mandriva-xfce-config-Powerpack

%description -n %{name}-OpenMandriva
This package regroups all specific  files
for %{distribution} Xfce desktop environment.

%prep
%setup -qn %{name}-%{snap}

%install
export sysconfdir=%{_sysconfdir}/xdg
export localstatedir=%{_var}/lib
export iconsdir=%{_iconsdir}
export prefix=%{_prefix}

%makeinstall_std


%pre -n %{name}-OpenMandriva
if [ -d %{_var}/lib/mandriva/xfce-profiles/Flash ]; then
  rm -rf %{_var}/lib/mandriva/xfce-profiles/Flash
  update-alternatives --remove-all xfce-config
fi

%post -n %{name}-OpenMandriva
update-alternatives --install %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml xfce-config %{_var}/lib/mandriva/xfce-profiles/OpenMandriva/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml 10

%postun -n %{name}-OpenMandriva
if ! [ -e %{_var}/lib/mandriva/xfce-profiles/OpenMandriva ]; then
  update-alternatives --remove xfce-config %{_var}/lib/mandriva/xfce-profiles/OpenMandriva/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
fi

%files -n %{name}-common
%doc AUTHORS ChangeLog README.update.urpmi
%dir %{_var}/lib/mandriva/xfce-profiles
%{_sysconfdir}/xdg/Terminal/*
%{_sysconfdir}/xdg/Thunar/*
%{_sysconfdir}/xdg/autostart/*
%{_sysconfdir}/xdg/xfce4/*
%{_sysconfdir}/xdg/menus/*
%{_bindir}/xfce4-firstrun

%files -n %{name}-OpenMandriva
%{_var}/lib/mandriva/xfce-profiles/OpenMandriva
