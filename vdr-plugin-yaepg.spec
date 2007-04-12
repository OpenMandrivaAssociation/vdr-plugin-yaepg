
%define plugin	yaepg
%define name	vdr-plugin-%plugin
%define version	0.0.2.1
%define rel	9

Summary:	VDR plugin: Yet Another EPG
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.hoochvdr.info/
# http://www.hoochvdr.info/modules.php?name=Forums&file=viewtopic&t=98
Source:		http://www.hoochvdr.info/files/vdr-%plugin-%version.tar.bz2

# From http://users.tkk.fi/~rahrenbe/vdr/
Patch0:		vdr-yaepg-0.0.2-finnish.diff

BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
Yaepg (Yet Another Electronic Programming Guide) is an EPG that tries to
simulate the look and feel of a commercial IRD.

%prep
%setup -q -n %plugin-%version
%patch0 -p1

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


