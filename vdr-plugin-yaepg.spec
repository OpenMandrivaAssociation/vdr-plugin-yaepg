
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


