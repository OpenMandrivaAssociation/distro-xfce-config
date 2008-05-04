%define snap 20080421

Summary: 	Mandriva Xfce configuration files
Name:    	mandriva-xfce-config
Version: 	2008.1
Release: 	%mkrel 9
Group:   	Graphical desktop/Xfce
License: 	GPLv2+
URL:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
# (tpg) http://svn.mandriva.com/svn/soft/mandriva-xfce-config/
Source0: 	%{name}-%{snap}.tar.bz2
BuildArch: 	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Configuration files for Mandriva Xfce desktop environment.

%package -n %{name}-common
Summary: 	Mandriva Xfce common configuration files
Group: 		Graphical desktop/Xfce
Requires(pre):	update-alternatives
Requires:	ia_ora-xfce
Requires:       tango-icon-theme
Requires:	mandriva-release-common

%description -n %{name}-common
Common configuration files for Mandriva Xfce desktop environment.

%package -n %{name}-Flash
Summary: 	Mandriva Xfce Flash configuration files
Group: 		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
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
Configuration files for Mandriva Flash Xfce desktop environment.

%package -n %{name}-Free
Summary: 	Mandriva Xfce Free configuration files
Group: 		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
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
Configuration files for Mandriva Free Xfce desktop environment.

%package -n %{name}-One
Summary: 	Mandriva Xfce One configuration files
Group: 		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
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
Configuration files for Mandriva One Xfce desktop environment.

%package -n %{name}-Powerpack
Summary:	Mandriva Xfce Powerpack configuration files
Group:		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/Development/Ideas/XFCE
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
Configuration files for Mandriva Powerpack Xfce desktop environment.

%prep
%setup -qn %{name}-%{snap}

%install
rm -rf %{buildroot}

export sysconfdir=%{_sysconfdir}
export localstatedir=%{_localstatedir}
export iconsdir=%{_iconsdir}

%makeinstall_std 

%clean
rm -rf %{buildroot}

%post -n %{name}-common
%update_icon_cache Tango

%postun -n %{name}-common
%clean_icon_cache Tango

%pre -n %{name}-Flash
if [ -d %{_localstatedir}/mandriva/xfce-profiles/Flash ]; then
  rm -rf %{_localstatedir}/mandriva/xfce-profiles/Flash
fi

%post -n %{name}-Flash
update-alternatives --install %{_sysconfdir}/X11/xdg/xfce4/mcs_settings xfce-config %{_localstatedir}/mandriva/xfce-profiles/Flash/xfce4/mcs_settings 10

%postun -n %{name}-Flash
if ! [ -e /var/lib/mandriva/xfce-profiles/Flash ]; then
  update-alternatives --remove xfce-config /var/lib/mandriva/xfce-profiles/Flash/xfce4/mcs_settings
fi

%pre -n %{name}-Free
if [ -d %{_localstatedir}/mandriva/xfce-profiles/Free ]; then
  rm -rf %{_localstatedir}/mandriva/xfce-profiles/Free
fi

%post -n %{name}-Free
update-alternatives --install %{_sysconfdir}/X11/xdg/xfce4/mcs_settings xfce-config %{_localstatedir}/mandriva/xfce-profiles/Free/xfce4/mcs_settings 10

%postun -n %{name}-Free
if ! [ -e /var/lib/mandriva/xfce-profiles/Free ]; then
  update-alternatives --remove xfce-config /var/lib/mandriva/xfce-profiles/Free/xfce4/mcs_settings
fi

%pre -n %{name}-One
if [ -d %{_localstatedir}/mandriva/xfce-profiles/One ]; then
  rm -rf %{_localstatedir}/mandriva/xfce-profiles/One
fi

%post -n %{name}-One
update-alternatives --install %{_sysconfdir}/X11/xdg/xfce4/mcs_settings xfce-config %{_localstatedir}/mandriva/xfce-profiles/One/xfce4/mcs_settings 10

%postun -n %{name}-One
if ! [ -e /var/lib/mandriva/xfce-profiles/One ]; then
  update-alternatives --remove xfce-config /var/lib/mandriva/xfce-profiles/One/xfce4/mcs_settings
fi

%pre -n %{name}-Powerpack
if [ -d %{_localstatedir}/mandriva/xfce-profiles/Powerpack ]; then
  rm -rf %{_localstatedir}/mandriva/xfce-profiles/Powerpack
fi

%post -n %{name}-Powerpack
update-alternatives --install %{_sysconfdir}/X11/xdg/xfce4/mcs_settings xfce-config %{_localstatedir}/mandriva/xfce-profiles/Powerpack/xfce4/mcs_settings 10

%postun -n %{name}-Powerpack
if ! [ -e /var/lib/mandriva/xfce-profiles/Powerpack ]; then
  update-alternatives --remove xfce-config /var/lib/mandriva/xfce-profiles/Powerpack/xfce4/mcs_settings
fi

%files -n %{name}-common
%defattr(-,root,root)
%doc AUTHORS ChangeLog README.update.urpmi
%{_sysconfdir}/X11/xdg/Terminal/*
%{_sysconfdir}/X11/xdg/Thunar/*
%{_sysconfdir}/X11/xdg/autostart/*
%{_sysconfdir}/X11/xdg/xfce4/*

%files -n %{name}-Flash
%defattr(-,root,root)
%{_localstatedir}/mandriva/xfce-profiles/Flash

%files -n %{name}-Free
%defattr(-,root,root)
%{_localstatedir}/mandriva/xfce-profiles/Free

%files -n %{name}-One
%defattr(-,root,root)
%{_localstatedir}/mandriva/xfce-profiles/One

%files -n %{name}-Powerpack
%defattr(-,root,root)
%{_localstatedir}/mandriva/xfce-profiles/Powerpack
