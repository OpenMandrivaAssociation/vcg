%define name vcg
%define version 1.30
%define rel 9
%define release %mkrel %{rel}

Summary: The VCG visualization tool for compiler graphs
Name: %name
Version: %version
Release: %release
License: GPL
Group: Graphics
URL: http://www.cs.uni-sb.de/RW/users/sander/html/gsvcg1.html
Source: ftp://ftp.cs.uni-sb.de/pub/graphics/vcg/vcg.tar.bz2
Patch0: vcg.1.30-fix-build.patch
Patch1: vcg.1.30-fix-link.patch
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libx11-devel

%description
The VCG tool reads a textual and readable specification of a 
graph and visualizes the graph.  If not all positions of 
nodes are fixed, the tool layouts the graph using several 
heuristics as reducing the number of crossings, minimizing 
the size of edges, centering of nodes.  The specification 
language of the VCG tool is nearly compatible to GRL, the 
language of the edge tool, but contains many extensions.  The 
VCG tool allows folding of dynamically or statically specified 
regions of the graph.  It uses colors and runs on X11.

%prep 
%setup -q -n %{name}.%{version}
%patch0 -p1 -z .pix
%patch1 -p0 -b .link

%build
make xvcg_gcc_noxmkmf xvcg CFLAGS="-c %{optflags}"

%install
rm -rf %buildroot
install -d %buildroot/{%{_bindir},%{_mandir}/manl}
make SED=sed BINDIR=%buildroot/%{_bindir} MANDIR=%buildroot/%{_mandir}/man1 MANEXT=1 install

cp -f demo/demo.csh expl
chmod 644 expl/cfg.vcg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README expl
%{_bindir}/*
%{_mandir}/*/*


%changelog
* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 1.30-9mdv2011.0
+ Revision: 633665
- rebuild
- fix link

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.30-8mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Fri Apr 27 2007 Pixel <pixel@mandriva.com> 1.30-8mdv2008.0
+ Revision: 18589
- rebuild


* Fri May 06 2005 Pixel <pixel@mandriva.com> 1.30-7mdk
- %%mkrel
- fix build on lib64

* Fri Nov 12 2004 Pixel <pixel@mandrakesoft.com> 1.30-6mdk
- rebuild

* Thu Aug 14 2003 Pixel <pixel@mandrakesoft.com> 1.30-5mdk
- fix MANEXT to .1 instead of .l

* Fri Apr 25 2003 Pixel <pixel@mandrakesoft.com> 1.30-4mdk
- don't use %%make, it seems to break
- add "BuildRequires: XFree86-devel"

* Fri Oct 19 2001 Pixel <pixel@mandrakesoft.com> 1.30-3mdk
- make rpmlint happy

* Thu Oct 18 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.30-2mdk
- rebuild

* Thu Dec 28 2000 Pixel <pixel@mandrakesoft.com> 1.30-1mdk
- initial spec

