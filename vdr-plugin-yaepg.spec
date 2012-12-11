
%define plugin	yaepg
%define name	vdr-plugin-%plugin
%define version	0.0.2.1
%define rel	19

Summary:	VDR plugin: Yet Another EPG
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.hoochvdr.info/
# http://www.hoochvdr.info/modules.php?name=Forums&file=viewtopic&t=98
Source:		http://www.hoochvdr.info/files/vdr-%plugin-%version.tar.bz2
# Use standard VDR logging mechanism instead of own logfile
Patch1:		yaepg-logging.patch
# Use standard types, from e-tobi repository
Patch2:		yaepg-standard-types.patch
# Change screenshot location
Patch3:		94_yaepg-1.3.38.dpatch
Patch4:		95_yaepg-0.0.2.1-vdr-1.5.3.dpatch
Patch5:		yaepg-0.0.2.1-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Yaepg (Yet Another Electronic Programming Guide) is an EPG that tries to
simulate the look and feel of a commercial IRD.

%prep
%setup -q -n %plugin-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README COPYING HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-19mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-18mdv2009.1
+ Revision: 359388
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-17mdv2009.0
+ Revision: 198001
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-16mdv2009.0
+ Revision: 197746
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch, obsoletes P0)
- change screenshot location (P3)
- adapt for api changes of VDR 1.5.3 (P4 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-15mdv2008.1
+ Revision: 145269
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-14mdv2008.1
+ Revision: 103253
- rebuild for new vdr

* Fri Jul 20 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-13mdv2008.0
+ Revision: 53734
- use standard uint64_t type (patch2)
- do not create separate logfile (patch1)

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-12mdv2008.0
+ Revision: 50065
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-11mdv2008.0
+ Revision: 42148
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-10mdv2008.0
+ Revision: 22728
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-9mdv2007.0
+ Revision: 90985
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-8mdv2007.1
+ Revision: 74100
- rebuild for new vdr
- Import vdr-plugin-yaepg

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-7mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-6mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-5mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-4mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-3mdv2007.0
- rebuild for new vdr

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-2mdv2007.0
- rebuild for new vdr

* Sat Jun 03 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2.1-1mdv2007.0
- initial Mandriva release

