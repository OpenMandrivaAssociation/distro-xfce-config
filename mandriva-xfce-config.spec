%define snap 20120314

Summary:	Mandriva Xfce configuration files
Name:		mandriva-xfce-config
Version:	2013.0
Release:	8
Group:		Graphical desktop/Xfce
License:	GPLv2+
URL:		http://wiki.mandriva.com/en/XfceLive
# (tpg) http://svn.mandriva.com/svn/soft/mandriva-xfce-config/
Source0:	%{name}-%{snap}.tar.bz2
Obsoletes:	xfce-config
BuildArch:	noarch

%description
This package regroups all specific configuration files for Mandriva Xfce
desktop environment.

%package -n %{name}-common
Summary:	Mandriva Xfce common configuration files
Group:		Graphical desktop/Xfce
Requires(pre):	update-alternatives
Requires:	ia_ora-xfce
Requires:	elementary-icons
Requires:	mandriva-release-common
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
This package regroups all common configuration files for Mandriva Xfce desktop
environment.

%package -n %{name}-Flash
Summary:	Mandriva Xfce Flash configuration files
Group:		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/XfceLive
# (tpg) mandriva stuff
Requires:	mandriva-release-Flash
Requires:	mandriva-theme-Flash
Requires(pre):	%{name}-common = %{version}-%{release}
Requires(preun):	%{name}-common = %{version}-%{release}
Conflicts:	%{name}-Free
Conflicts:	%{name}-One
Conflicts:	%{name}-Powerpack
Provides:	%{name}

%description -n %{name}-Flash
This package regroups all specific  files for Mandriva Flash Xfce desktop
environment.

%package -n %{name}-Free
Summary:	Mandriva Xfce Free configuration files
Group:		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/XfceLive
# (tpg) mandriva stuff
Requires:	mandriva-release-Free
Requires:	mandriva-theme-Free
Requires(pre):	%{name}-common = %{version}-%{release}
Requires(preun):	%{name}-common = %{version}-%{release}
Conflicts:	%{name}-Flash
Conflicts:	%{name}-One
Conflicts:	%{name}-Powerpack
Provides:	%{name}

%description -n %{name}-Free
This package regroups all specific  files for Mandriva Free Xfce desktop
environment.

%package -n %{name}-One
Summary:	Mandriva Xfce One configuration files
Group:		Graphical desktop/Xfce
Url:		http://wiki.mandriva.com/en/XfceLive
# (tpg) mandriva stuff
Requires:	mandriva-release-One
Requires:	mandriva-theme-One
Requires(pre):	%{name}-common = %{version}-%{release}
Requires(preun):	%{name}-common = %{version}-%{release}
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
Requires(preun):	%{name}-common = %{version}-%{release}
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
export sysconfdir=%{_sysconfdir}/xdg
export localstatedir=%{_var}/lib
export iconsdir=%{_iconsdir}
export prefix=%{_prefix}

%makeinstall_std


%post -n %{name}-common
%update_icon_cache Tango

%postun -n %{name}-common
%clean_icon_cache Tango

%pre -n %{name}-Flash
if [ -d %{_var}/lib/mandriva/xfce-profiles/Flash ]; then
  rm -rf %{_var}/lib/mandriva/xfce-profiles/Flash
  update-alternatives --remove-all xfce-config
fi

%post -n %{name}-Flash
update-alternatives --install %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml xfce-config %{_var}/lib/mandriva/xfce-profiles/Flash/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml 10

%postun -n %{name}-Flash
if ! [ -e %{_var}/lib/mandriva/xfce-profiles/Flash ]; then
  update-alternatives --remove xfce-config %{_var}/lib/mandriva/xfce-profiles/Flash/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
fi

%pre -n %{name}-Free
if [ -d %{_var}/lib/mandriva/xfce-profiles/Free ]; then
  rm -rf %{_var}/lib/mandriva/xfce-profiles/Free
  update-alternatives --remove-all xfce-config
fi

%post -n %{name}-Free
update-alternatives --install %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml xfce-config %{_var}/lib/mandriva/xfce-profiles/Free/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml 10

%postun -n %{name}-Free
if ! [ -e %{_var}/lib/mandriva/xfce-profiles/Free ]; then
  update-alternatives --remove xfce-config %{_var}/lib/mandriva/xfce-profiles/Free/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
fi

%pre -n %{name}-One
if [ -d %{_var}/lib/mandriva/xfce-profiles/One ]; then
  rm -rf %{_var}/lib/mandriva/xfce-profiles/One
  update-alternatives --remove-all xfce-config
fi

%post -n %{name}-One
update-alternatives --install %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml xfce-config %{_var}/lib/mandriva/xfce-profiles/One/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml 10

%postun -n %{name}-One
if ! [ -e %{_var}/lib/mandriva/xfce-profiles/One ]; then
  update-alternatives --remove xfce-config %{_var}/lib/mandriva/xfce-profiles/One/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
fi

%pre -n %{name}-Powerpack
if [ -d %{_var}/lib/mandriva/xfce-profiles/Powerpack ]; then
  rm -rf %{_var}/lib/mandriva/xfce-profiles/Powerpack
  update-alternatives --remove-all xfce-config
fi

%post -n %{name}-Powerpack
update-alternatives --install %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml xfce-config %{_var}/lib/mandriva/xfce-profiles/Powerpack/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml 10

%postun -n %{name}-Powerpack
if ! [ -e %{_var}/lib/mandriva/xfce-profiles/Powerpack ]; then
  update-alternatives --remove xfce-config %{_var}/lib/mandriva/xfce-profiles/Powerpack/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
fi

%files -n %{name}-common
%doc AUTHORS ChangeLog README.update.urpmi
%dir %{_var}/lib/mandriva/xfce-profiles
%{_sysconfdir}/xdg/Terminal/*
%{_sysconfdir}/xdg/Thunar/*
%{_sysconfdir}/xdg/autostart/*
%{_sysconfdir}/xdg/xfce4/*
%{_bindir}/xfce4-firstrun

%files -n %{name}-Flash
%{_var}/lib/mandriva/xfce-profiles/Flash

%files -n %{name}-Free
%{_var}/lib/mandriva/xfce-profiles/Free

%files -n %{name}-One
%{_var}/lib/mandriva/xfce-profiles/One

%files -n %{name}-Powerpack
%{_var}/lib/mandriva/xfce-profiles/Powerpack


%changelog
* Fri Apr 06 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2011.0-9mdv2012.0
+ Revision: 789516
- rebuild

* Wed Mar 14 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2011.0-8
+ Revision: 784906
- fix shortcuts configuration file

* Fri Jan 06 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2011.0-7
+ Revision: 758139
- enable session saving feature (needs fixed xfce4-session-4.8.2-3)
- start gigolo after each login

* Thu Sep 01 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2011.0-6
+ Revision: 697751
- do not save session, always use default one
- do not scroll in terminal after print on std

* Sat Jul 30 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2011.0-5
+ Revision: 692486
- update configuration files one more time

* Sat Jul 30 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2011.0-4
+ Revision: 692478
- add corrent session configuration file

* Sat Jul 30 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2011.0-3
+ Revision: 692470
- fix workspaces plugin
- copy panel files
- add panel activators
- add xfconf settings

* Sat Jul 30 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2011.0-1
+ Revision: 692463
- update to new version 20110730

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2010.1-4mdv2011.0
+ Revision: 579733
- disable requires on xfce4-places-plugin
- use auto-choose option instead of scaled wallpaper style

* Sun Mar 14 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2010.1-2mdv2010.1
+ Revision: 519087
- add two new keyboard shortcuts
  o XF86HomePage binded to default webbrowser
  o XF86Mail binded to default Mail client

* Thu Feb 25 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2010.1-1mdv2010.1
+ Revision: 511196
-update to new snapshot 20100225:
  o fix xfce4-screnshooter syntax
  o fix /KeyRepeat/Delay xfconf key
- xfce4-firstrun:
  o add checks for running xfdesktop
  o add some verbose message
  o add header

* Sat Oct 24 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2010.0-1mdv2010.0
+ Revision: 459132
- use Ia Ora Steel as a default theme for Free flavour

* Mon Jul 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.1-6mdv2010.0
+ Revision: 392974
- add requires on dynamic
- add requires on xfce4-places-plugin

* Thu Mar 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.1-5mdv2009.1
+ Revision: 361407
- adjust window size and separator places for Thunar

* Wed Mar 18 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.1-4mdv2009.1
+ Revision: 357516
- provide a better menu layout, inspired by KDE one ;)

* Fri Mar 13 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.1-3mdv2009.1
+ Revision: 354637
- BS is hungry, feed it ;)
- and pin up window button
- move xfce4-power-manager.desktop file to the xfce4-power-manager package
- bind amixer command to volume keys, with aumix-text toggling mute/unmute is impossible
- use Smoke theme for notification bubbles

* Tue Feb 17 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.1-1mdv2009.1
+ Revision: 341647
- add support for volume keys (mdvbz #47218)

* Wed Feb 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.1-0.9mdv2009.1
+ Revision: 339505
- fix latest commit

* Tue Feb 10 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.1-0.8mdv2009.1
+ Revision: 339030
- fix file list
- update configs for Xfce-4.6-rc1
  o rename xfce4-update-config to xfce4-firstrun
  o update configs for mdv flavours
  o update xfce4-power-manager settings
  o run xfce4-screenshooter while print screen key is presse
  o place xfswitch-plugin on main panel
  o use LCD clock display

* Mon Jan 19 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.1-0.7mdv2009.1
+ Revision: 331257
- fix xfce4-session.xml file, xfce should start fine
- add config files for xfce4-appfinder.xml
- tune up Thunar windw apperance, use compact view as default
- use evdev as a default driver for keyboard
- add more xfwm4 settings
- tune up keyboard shortcuts, should be working again

* Sun Jan 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.1-0.6mdv2009.1
+ Revision: 328351
- update xfconf settings
- set DPI to 96
- set keyboard shortcuts
- set default options for xfce4-notifyd, xfce4-power-manager and keyboard-layout

* Wed Jan 07 2009 Götz Waschk <waschk@mandriva.org> 2009.1-0.5mdv2009.1
+ Revision: 326764
- new snapshot to fiix the power manager desktop entry

* Mon Nov 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.1-0.4mdv2009.1
+ Revision: 306461
- add more support for Xfce-6.4 xfconf settings
  o install all xml files
  o handle nicely update-alternatives on 4.4.2 -> 4.6 update
- pre and pre un requires on xfconf

* Tue Nov 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.1-0.1mdv2009.1
+ Revision: 304270
- new version, works only with Xfce-4.6
  o sync xfce4-keyboard-shortcuts.xml with upstream
  o reduce font size to 12 for terminal
  o add support for xfce4-power-manager
  o adjust panels size

* Mon Sep 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.0-7mdv2009.0
+ Revision: 286708
- plays login sound on startup (needs canberra-gtk)

* Mon Sep 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.0-6mdv2009.0
+ Revision: 286665
- add xfce4-update-config tool
  o add missing icons on Xfce desktop
  o show draklive-install on desktop if found (to ease installation for iso)
- show icon for places plugin (no more visual conflict with file manager icon launcher)
- use Thunar icon for file manager launcher
- do not scroll Terminal on new output

* Sun Sep 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.0-5mdv2009.0
+ Revision: 282280
- set DPI to 96 as a default value
- set font size to 14 for terminal
- add conflicts for xfce-utils < 4.2.2-22, since Xft.xrdb is now in mandriva-xfce-config-common package

* Fri Sep 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.0-4mdv2009.0
+ Revision: 281332
- use dynamic scripts for user actions

* Wed Jul 09 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.0-3mdv2009.0
+ Revision: 232880
- fix all urls
- use %%_var instead of %%_localstatedir

* Tue Jul 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2009.0-2mdv2009.0
+ Revision: 232869
- update url
- xfce4-volstatus-icon app should be autostarted only under Xfce (#41906)

* Mon Jun 09 2008 Thierry Vignaud <tv@mandriva.org> 2009.0-1mdv2009.0
+ Revision: 217058
- bump version for 2009.0

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Tue May 27 2008 Thierry Vignaud <tv@mandriva.org> 2008.1-16mdv2009.0
+ Revision: 211571
- better descriptions

* Sun May 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-15mdv2009.0
+ Revision: 211226
- use exaile for playing audio cd's (#40342)

* Mon May 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-14mdv2009.0
+ Revision: 206289
- fix update-alternatives scripts for new sysconfdir place on mdv 2009 and newer

* Sun May 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-13mdv2009.0
+ Revision: 205683
- change sysconfdir from /etc/X11/xdg to /etc/xdg only for Mandriva releases newer than 2008.1

* Sun May 04 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-12mdv2009.0
+ Revision: 201074
- restore old changelog (don't know how but i've deleted it somehow)
- re-commit my last changes
  o use xfburn as a default burning tool
  o import photos with gthumb
- hello ?

* Mon Apr 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-9mdv2009.0
+ Revision: 196049
- fix the gtkrc file
  o correct icon label transparency
  o set background pixmap only for Xfce panel widget

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-8mdv2009.0
+ Revision: 194773
- add theme
  o add background panel (image stolen from kde ;)
  o make transparent labels of icons on desktop
- fix del key behaviour under terminal (#39550 and #36455)

* Fri Mar 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-6mdv2008.1
+ Revision: 189396
- make the second panel bigger
- add mixer on panel
- handle brasero nicely on empty medium insert action

* Tue Mar 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-5mdv2008.1
+ Revision: 188541
- use svn icon for drakconf
- use the mandriva svg icons from tango package
- add missing icon for "about" menu entry

* Thu Mar 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-4mdv2008.1
+ Revision: 187460
- icon's size on desktop is ono 48
- main panel size is reduced to 32
- secondary panel size is reduced to 24
- correct the color theme for Flash

* Wed Mar 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-3mdv2008.1
+ Revision: 187158
- fix executing of ristretto-import.sh

* Wed Mar 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-2mdv2008.1
+ Revision: 187113
- use ristretto-import.sh instead of f-spot-import

* Fri Feb 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.1-1mdv2008.1
+ Revision: 176626
- new snapshot:
  o fixes against latest ia_ora-xfce
  o ready for 2008.1

* Sun Feb 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.0-2mdv2008.1
+ Revision: 174123
- new snapshot
  o fix theme for Powerpack
  o add configs for Flash
  o update Makefile
- hardcode requires for a specific mdv flavour

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Thu Jan 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2008.0-1mdv2008.1
+ Revision: 157637
- change versioning

* Tue Jan 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.8-1mdv2008.1
+ Revision: 146809
- new version
  o provide README.update.urpmi
  o remove Mdkapplet.desktop as it is now useless
  o add better thunarrc and settings rc for notification-daemon-xfce
  o better description for README and README.update.urpmi files

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jan 02 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.7-1mdv2008.1
+ Revision: 140543
- workaround for a vte's bug, backspace should now work under screen (#36455)
- add ChangeLog

* Wed Dec 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.6-1mdv2008.1
+ Revision: 137829
- new version 1.3.6
- remove icons, as they are handled by xfdesktop package
- make panel looks nicer
    o add some separators
    o do not use flat buttons in task list
    o add windowlist to the panel

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.5-3mdv2008.1
+ Revision: 117601
- fix summary

* Tue Dec 11 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.5-2mdv2008.1
+ Revision: 117320
- do not require task-xfce-minimal for common package, fixes bug #35753
- new version
  o add makefile inside tarball and make use of this in spec file
  o add AUTHORS
  o merge Tango icons into main tarball
  o multilevel menus are gone
  o do not hardcode Firefox icon in menu and panel entries for webbrowser

* Tue Dec 11 2007 Jérôme Soyer <saispo@mandriva.org> 1.3.4-1mdv2008.1
+ Revision: 117198
- Add file
- Add Tango Icon by default

* Wed Nov 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.3-4mdv2008.1
+ Revision: 113739
- fix wrong category (s/Photograph/Photography)

* Fri Nov 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.3-3mdv2008.1
+ Revision: 111655
- xfwm default theme is now Ia Ora
- requires ia_ora-xfce

* Fri Nov 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.3-1mdv2008.1
+ Revision: 111632
- new version
  o do not use xfbrowser4 in menus to start webbrowser, because this doesn't use preffered webbrowser set in by user (thanks goes to Dotan Kamber for pointing this out)
  o use exo-open --launch WebBrowser instead of

* Tue Nov 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.2-2mdv2008.1
+ Revision: 110797
- reenable menu options
- reenable mandriva related icons

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.2-1mdv2008.1
+ Revision: 110580
- new version
- updated all files to Xfce version 4.4.2

* Fri Oct 05 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.1-1mdv2008.1
+ Revision: 95639
- new version
 o use new multilevel menus
 o panel launchers are multilingual again
 o use mozilla-firefox icon for webbrowser entries in panel and menu

* Sun Sep 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3-5mdv2008.0
+ Revision: 93993
+ rebuild (emptylog)

* Sun Sep 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3-4mdv2008.0
+ Revision: 93975
- fix bug #34326
- add more configuration files

* Sun Sep 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3-3mdv2008.0
+ Revision: 92367
- do not hardcode requires for a specific Mandriva flavour
- all subpackages(excluding common) provides mandriva-xfce-config

* Sat Sep 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3-2mdv2008.0
+ Revision: 92123
- fix scripts, now this should work
- fix orage config

* Fri Sep 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3-1mdv2008.0
+ Revision: 91934
- new version
    o use update-alternatives
    o change apperance of a panel
    o update all settings
- provide common package with settings for all Mandriva flavours
- install missing autostart files
- change name to mandriva-xfce-config
- add provides/obsoletes
- change name, closer with distro

* Tue Jun 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2-2mdv2008.0
+ Revision: 44288
- add correct tarball
- fix file list

* Mon Jun 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2-1mdv2008.0
+ Revision: 44133
- new version
  o add autostart andl volstatus files
- o add Xfce panel configuration files

* Wed Jun 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-2mdv2008.0
+ Revision: 41743
- add conflicts and provides

* Mon Jun 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-1mdv2008.0
+ Revision: 40917
- xfce-config holds Xfce configuration for Mandriva flavours
- Import xfce-config

