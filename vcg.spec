%define name vcg
%define version 1.30
%define rel 8
%define release %mkrel %{rel}

Summary: The VCG visualization tool for compiler graphs
Name: %name
Version: %version
Release: %release
License: GPL
Group: Graphics
URL: http://www.cs.uni-sb.de/RW/users/sander/html/gsvcg1.html
Source: ftp://ftp.cs.uni-sb.de/pub/graphics/vcg/vcg.tar.bz2
Patch: vcg.1.30-fix-build.patch
BuildRequires: X11-devel

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

%build
make xvcg_gcc_noxmkmf xvcg CFLAGS="-c %{optflags}" LIBPATH="-L/usr/X11R6/%{_lib}"

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

