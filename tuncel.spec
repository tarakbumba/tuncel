Name:		tuncel
Summary:	Servicemenu/Actions for various desktops
Version:	1.0
Release:	%mkrel 1

License:	GPLv2
Group:		Development/Other
Source0:	https://github.com/tarakbumba/%{name}/archive/%{name}-%{version}.tar.gz
URL:		https://github.com/tarakbumba/tuncel

BuildRequires:	kdebase4-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	gettext-devel
BuildRequires:  pkgconfig(libcaja-extension)
BuildRequires:  pkgconfig(libnemo-extension)
BuildRequires:  pkgconfig(libnautilus-extension)
BuildRequires:  caja-actions
BuildRequires:  nemo-actions
BuildRequires:  nautilus-actions
BuildRequires:  gettext-devel

Requires:   coreutils
Requires:   gettext

%description
KDE3/4, Nautilus, Caja and Nemo service menus for RPM

   1. Show RPM Main Info
   2. Show Package Content
   3. Unpack RPM
   4. Unpack RPM to Directory
   5. Open RPM Url from Package in Web Browser
   6. Make Test Install
   7. Force Upgrade Test Install
   8. Install Source package in Local RPM Build Enviroment

%package -n %{name}-kde4
Summary:    KDE4 Service Menu for RPM Packages
Requires:   %{name} = %{version}-%{release}
Requires:   kdialog

%description -n %{name}-kde4
KDE4 service menu for easy RPM package operations.

%package -n %{name}-nautilus-data
Summary:    Required files for Nautilus/Caja
Requires:   %{name} = %{version}-%{release}
Requires:   zenity

%description -n %{name}-nautilus-data
This package includes shared desktop files
needed for Nautilus and Caja file managers

%package -n %{name}-nautilus
Summary:    Nautilus action for RPM Packages
Requires:   %{name}-nautilus-data = %{version}-%{release}
Requires:   nautilus-actions

%description -n %{name}-nautilus
Virtual package to satisfy dependencies for Nautilus.

%package -n %{name}-caja
Summary:    Caja action for RPM Packages
Requires:   %{name}-nautilus-data = %{version}-%{release}
Requires:   caja-actions

%description -n %{name}-caja
Virtual package to satisfy dependencies for Caja.

%package -n %{name}-nemo
Summary:    Nemo action for RPM Packages
Requires:   %{name} = %{version}-%{release}
Requires:   zenity
Requires:   nemo-actions

%description -n %{name}-nemo
Nemo-Actions actions for easy RPM package operations.


%prep
%setup -q

%build

autoreconf
automake -a

%configure  --enable-kde4 \
            --enable-nautilus-actions \
            --enable-nemo-actions \
            --sysconfdir=%{_sysconfdir}

%make

%install

%makeinstall_std
%find_lang %{name}.lang

%files -f %{name}.lang
%config %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/

%files -n %{name}-kde4
%{_kde_services}/ServiceMenus/%{name}.desktop

%files -n %{name}-nautilus-data
%{_datadir}/file-manager/actions/*.desktop

%files -n %{name}-nemo
%{_datadir}/nemo/actions/*.desktop

%files -n %{name}-nautilus

%files -n %{name}-caja

