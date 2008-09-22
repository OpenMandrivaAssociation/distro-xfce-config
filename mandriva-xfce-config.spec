%define snap 20080922

Summary: 	Mandriva Xfce configuration files
Name:    	mandriva-xfce-config
Version: 	2009.0
Release: 	%mkrel 6
Group:   	Graphical desktop/Xfce
License: 	GPLv2+
URL:		http://wiki.mandriva.com/en/XfceLive
# (tpg) http://svn.mandriva.com/svn/soft/mandriva-xfce-config/
Source0: 	%{name}-%{snap}.tar.bz2
BuildArch: 	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package regroups all specific configuration files for Mandriva Xfce
desktop environment.

%package -n %{name}-common
Summary: 	Mandriva Xfce common configuration files
Group: 		Graphical desktop/Xfce
Requires(pre):	update-alternatives
Requires:	ia_ora-xfce
Requires:       tango-icon-theme
Requires:	mandriva-release-common
%if %mdkversion > 2008100
Conflicts:	xfce-utils <= 4.4.2-22
%endif

%description -n %{name}-common
This package regroups all common configuration files for Mandriva Xfce desktop
environment.

%package -n %{name}-Flash
Summary: 	Mandriva Xfce Flash configuration files
Group: 		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/XfceLive
# (tpg) mandriva stuff
Requires:	mandriva-release-Flash
Requires:	mandriva-theme-Flash
Requires(pre):	%{name}-common = %{version}-%{release}
Requires(preun): %{name}-common = %{version}-%{release}
Conflicts:	%{name}-Free
Conflicts:	%{name}-One
Conflicts:	%{name}-Powerpack
Provides:	%{name}

%description -n %{name}-Flash
This package regroups all specific  files for Mandriva Flash Xfce desktop
environment.

%package -n %{name}-Free
Summary: 	Mandriva Xfce Free configuration files
Group: 		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/XfceLive
# (tpg) mandriva stuff
Requires:	mandriva-release-Free
Requires:	mandriva-theme-Free
Requires(pre):	%{name}-common = %{version}-%{release}
Requires(preun): %{name}-common = %{version}-%{release}
Conflicts:	%{name}-Flash
Conflicts:	%{name}-One
Conflicts:	%{name}-Powerpack
Provides:	%{name}

%description -n %{name}-Free
This package regroups all specific  files for Mandriva Free Xfce desktop
environment.

%package -n %{name}-One
Summary: 	Mandriva Xfce One configuration files
Group: 		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/XfceLive
# (tpg) mandriva stuff
Requires:	mandriva-release-One
Requires:	mandriva-theme-One
Requires(pre):	%{name}-common = %{version}-%{release}
Requires(preun): %{name}-common = %{version}-%{release}
Conflicts:	%{name}-Flash
Conflicts:	%{name}-Free
Conflicts:	%{name}-Powerpack
Provides:	%{name}

%description -n %{name}-One
This package regroups all specific  files for Mandriva One Xfce desktop
environment.

%package -n %{name}-Powerpack
Summary:	Mandriva Xfce Powerpack configuration files
Group:		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/XfceLive
# (tpg) mandriva stuff
Requires:	mandriva-release-Powerpack
Requires:	mandriva-theme-Powerpack
Requires(pre):	%{name}-common = %{version}-%{release}
Requires(preun): %{name}-common = %{version}-%{release}
Conflicts:	%{name}-Flash
Conflicts:	%{name}-Free
Conflicts:	%{name}-One
Provides:	%{name}

%description -n %{name}-Powerpack
This package regroups all specific  files for Mandriva Powerpack Xfce desktop
environment.

%prep
%setup -qn %{name}-%{snap}

%install
rm -rf %{buildroot}
%if %mdkversion < 200900
export sysconfdir=%{_sysconfdir}/X11/xdg
%else
export sysconfdir=%{_sysconfdir}/xdg
%endif
export localstatedir=%{_var}/lib
export iconsdir=%{_iconsdir}
export prefix=%{_prefix}

%makeinstall_std 

%clean
rm -rf %{buildroot}

%post -n %{name}-common
%update_icon_cache Tango

%postun -n %{name}-common
%clean_icon_cache Tango

%pre -n %{name}-Flash
if [ -d %{_var}/lib/mandriva/xfce-profiles/Flash ]; then
  rm -rf %{_var}/lib/mandriva/xfce-profiles/Flash
fi

%post -n %{name}-Flash
%if %mdkversion < 200900
update-alternatives --install %{_sysconfdir}/X11/xdg/xfce4/mcs_settings xfce-config %{_var}/lib/mandriva/xfce-profiles/Flash/xfce4/mcs_settings 10
%else
update-alternatives --install %{_sysconfdir}/xdg/xfce4/mcs_settings xfce-config %{_var}/lib/mandriva/xfce-profiles/Flash/xfce4/mcs_settings 10
%endif

%postun -n %{name}-Flash
if ! [ -e /var/lib/mandriva/xfce-profiles/Flash ]; then
  update-alternatives --remove xfce-config /var/lib/mandriva/xfce-profiles/Flash/xfce4/mcs_settings
fi

%pre -n %{name}-Free
if [ -d %{_var}/lib/mandriva/xfce-profiles/Free ]; then
  rm -rf %{_var}/lib/mandriva/xfce-profiles/Free
fi

%post -n %{name}-Free
%if %mdkversion < 200900
update-alternatives --install %{_sysconfdir}/X11/xdg/xfce4/mcs_settings xfce-config %{_var}/lib/mandriva/xfce-profiles/Free/xfce4/mcs_settings 10
%else
update-alternatives --install %{_sysconfdir}/xdg/xfce4/mcs_settings xfce-config %{_var}/lib/mandriva/xfce-profiles/Free/xfce4/mcs_settings 10
%endif

%postun -n %{name}-Free
if ! [ -e /var/lib/mandriva/xfce-profiles/Free ]; then
  update-alternatives --remove xfce-config /var/lib/mandriva/xfce-profiles/Free/xfce4/mcs_settings
fi

%pre -n %{name}-One
if [ -d %{_var}/lib/mandriva/xfce-profiles/One ]; then
  rm -rf %{_var}/lib/mandriva/xfce-profiles/One
fi

%post -n %{name}-One
%if %mdkversion < 200900
update-alternatives --install %{_sysconfdir}/X11/xdg/xfce4/mcs_settings xfce-config %{_var}/lib/mandriva/xfce-profiles/One/xfce4/mcs_settings 10
%else
update-alternatives --install %{_sysconfdir}/xdg/xfce4/mcs_settings xfce-config %{_var}/lib/mandriva/xfce-profiles/One/xfce4/mcs_settings 10
%endif

%postun -n %{name}-One
if ! [ -e /var/lib/mandriva/xfce-profiles/One ]; then
  update-alternatives --remove xfce-config /var/lib/mandriva/xfce-profiles/One/xfce4/mcs_settings
fi

%pre -n %{name}-Powerpack
if [ -d %{_var}/lib/mandriva/xfce-profiles/Powerpack ]; then
  rm -rf %{_var}/lib/mandriva/xfce-profiles/Powerpack
fi

%post -n %{name}-Powerpack
%if %mdkversion < 200900
update-alternatives --install %{_sysconfdir}/X11/xdg/xfce4/mcs_settings xfce-config %{_var}/lib/mandriva/xfce-profiles/Powerpack/xfce4/mcs_settings 10
%else
update-alternatives --install %{_sysconfdir}/xdg/xfce4/mcs_settings xfce-config %{_var}/lib/mandriva/xfce-profiles/Powerpack/xfce4/mcs_settings 10
%endif

%postun -n %{name}-Powerpack
if ! [ -e /var/lib/mandriva/xfce-profiles/Powerpack ]; then
  update-alternatives --remove xfce-config /var/lib/mandriva/xfce-profiles/Powerpack/xfce4/mcs_settings
fi

%files -n %{name}-common
%defattr(-,root,root)
%doc AUTHORS ChangeLog README.update.urpmi
%if %mdkversion < 200900
%{_sysconfdir}/X11/xdg/Terminal/*
%{_sysconfdir}/X11/xdg/Thunar/*
%{_sysconfdir}/X11/xdg/autostart/*
%{_sysconfdir}/X11/xdg/xfce4/*
%else
%{_sysconfdir}/xdg/Terminal/*
%{_sysconfdir}/xdg/Thunar/*
%{_sysconfdir}/xdg/autostart/*
%{_sysconfdir}/xdg/xfce4/*
%{_bindir}/xfce4-update-config
%endif

%files -n %{name}-Flash
%defattr(-,root,root)
%{_var}/lib/mandriva/xfce-profiles/Flash

%files -n %{name}-Free
%defattr(-,root,root)
%{_var}/lib/mandriva/xfce-profiles/Free

%files -n %{name}-One
%defattr(-,root,root)
%{_var}/lib/mandriva/xfce-profiles/One

%files -n %{name}-Powerpack
%defattr(-,root,root)
%{_var}/lib/mandriva/xfce-profiles/Powerpack
