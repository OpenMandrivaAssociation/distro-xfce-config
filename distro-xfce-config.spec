%define snap 20140903

Summary:	%{distribution} Xfce configuration files
Name:		distro-xfce-config
Version:	2014.0
Release:	1
Group:		Graphical desktop/Xfce
License:	GPLv2+
URL:		https://abf.io/omv_software/distro-xfce-config
# (tpg) http://svn.mandriva.com/svn/soft/mandriva-xfce-config/
Source0:	https://abf.io/omv_software/distro-xfce-config/%{name}-%{snap}.tar.xz
Obsoletes:	xfce-config
%rename	mandriva-xfce-config
BuildArch:	noarch

%description
This package regroups all specific configuration
files for %{distribution} Xfce desktop environment.

%package -n %{name}-common
Summary:	%{distribution} Xfce common configuration files
Group:		Graphical desktop/Xfce
Requires(pre):	update-alternatives
Requires:	ia_ora-xfce
Requires:	elementary-icons
Requires:	distro-release-common
%rename		mandriva-xfce-config-common

Requires(pre):	xfconf
Requires(preun):	xfconf
#Requires:	xfce4-weather-plugin
#Requires:	xfce4-cpugraph-plugin
Requires:	dynamic
%if %mdkversion > 2008100
Conflicts:	xfce-utils <= 4.4.2-22
Conflicts:	xfce4-power-manager < 0.6.4-3
Conflicts:	xfdesktop < 4.6.0-4
%endif

%description -n %{name}-common
This package regroups all common configuration files
for %{distribution} Xfce desktop environment.

%package -n %{name}-OpenMandriva
Summary:	%distribution Xfce Flash configuration files
Group:		Graphical desktop/Xfce
Url:		https://abf.io/omv_software/distro-xfce-config
# (tpg) mandriva stuff
Requires:	distro-release-OpenMandriva
Requires:	mandriva-theme-OpenMandriva
Requires(pre):	%{name}-common = %{version}-%{release}
Requires(preun):	%{name}-common = %{version}-%{release}

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
%{_bindir}/xfce4-firstrun

%files -n %{name}-OpenMandriva
%{_var}/lib/mandriva/xfce-profiles/OpenMandriva
