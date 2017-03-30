%define trinity 0
%{?_without_trinity: %global trinity 0}
%{?_with_trinity: %global trinity 1}
%define _tde_services /opt/trinity/share/apps/konqueror/servicemenus
%define plasma 1
%{?_without_plasma: %global plasma 0}
%{?_with_plasma: %global plasma 1}
%define kde4 0
%{?_without_kde4: %global kde4 0}
%{?_with_kde4: %global kde4 1}
%define gtk 1
%{?_without_gtk: %global gtk 0}
%{?_with_gtk: %global gtk 1}

Name:		tuncel
Summary:	Servicemenu or Actions for various desktops
Version:	2.0
Release:	%mkrel 1

License:	GPLv2
Group:		Development/Other
Source0:	https://github.com/tarakbumba/%{name}/archive/%{name}-%{version}.tar.xz
URL:		https://github.com/tarakbumba/tuncel

%if %{kde4}
BuildRequires:	kdelibs4-core
BuildRequires:  kde4-macros
%endif
%if %{plasma}
BuildRequires:  kf5-macros
%endif
%if %{trinity}
BuildRequires:	trinity-tdelibs
%endif
%if %{gtk}
BuildRequires:  zenity
%endif
%if %{kde4} && %{plasma}
BuildRequires:  kdialog
%endif
BuildRequires:	gettext-devel
BuildRequires:  python-polib
BuildRequires:  intltool

BuildArch:      noarch

%description
KDE4/Plasma Dolphin, Trinity Konqueror, Nautilus, Caja and Nemo service menus for RPM

   1. Show RPM Main Info
   2. Show Package Content
   3. Unpack RPM
   4. Unpack RPM to Directory
   5. Open RPM Url from Package in Web Browser
   6. Make Test Install
   7. Force Upgrade Test Install
   8. Install Source package in Local RPM Build Enviroment

%if %{kde4}
%package -n %{name}-kde4
Summary:    KDE4 Service Menu for RPM Packages
Requires:   %{name} = %{version}-%{release}
Requires:   kdialog

%description -n %{name}-kde4
KDE4 service menu for easy RPM package operations.
%endif

%if %{plasma}
%package -n %{name}-plasma
Summary:    Plasma Service Menu for RPM Packages
Requires:   %{name} = %{version}-%{release}
Requires:   kdialog

%description -n %{name}-plasma
KDE4 service menu for easy RPM package operations.
%endif

%if %{trinity}
%package -n %{name}-trinity
Summary:    Trinity Desktop Service Menu for RPM Packages
Requires:   %{name} = %{version}-%{release}
Requires:   kdialog

%description -n %{name}-trinity
Trinity service menu for easy RPM package operations.
%endif

%if %{gtk}
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
Requires:   zenity

%description -n %{name}-nautilus
Virtual package to satisfy dependencies for Nautilus.

%package -n %{name}-caja
Summary:    Caja action for RPM Packages
Requires:   %{name}-nautilus-data = %{version}-%{release}
Requires:   caja-actions
Requires:   zenity

%description -n %{name}-caja
Virtual package to satisfy dependencies for Caja.

%package -n %{name}-nemo
Summary:    Nemo actions for RPM Packages
Requires:   %{name} = %{version}-%{release}
Requires:   zenity
Requires:   nemo

%description -n %{name}-nemo
Nemo-Actions actions for easy RPM package operations.
%endif

%prep
%autosetup

%build
NOCONFIGURE=1 ./autogen.sh

%configure2_5x  --sysconfdir=%{_sysconfdir} \
%if %{kde4}
            --enable-kde4 \
%endif
%if %{trinity}
            --enable-trinity \
%endif
%if %{gtk}
            --enable-nautilus \
            --enable-nemo \
%endif
%if %{plasma}
            --enable-plasma
%endif
                 

%make_build

%install

%make_install
%if %{kde4}
mv %{buildroot}%{_kde_services}/ServiceMenus/%{name}_kde4.desktop \
	%{buildroot}%{_kde_services}/ServiceMenus/%{name}.desktop
%endif

%if %{plasma}
mv %{buildroot}%{_kf5_services}/ServiceMenus/%{name}_plasma.desktop \
	%{buildroot}%{_kf5_services}/ServiceMenus/%{name}.desktop
%endif

%if %{trinity}
mv %{buildroot}%{_tde_services}/%{name}_trinity.desktop \
	%{buildroot}%{_tde_services}/ServiceMenus/%{name}.desktop
%endif

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README.md
%config (noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}

%if %{kde4}
%files -n %{name}-kde4
%{_kde_services}/ServiceMenus/%{name}.desktop
%endif

%if %{plasma}
%files -n %{name}-plasma
%{_kf5_services}/ServiceMenus/%{name}.desktop
%endif

%if %{gtk}
%files -n %{name}-nautilus-data
%{_datadir}/file-manager/actions/*.desktop

%files -n %{name}-nemo
%{_datadir}/nemo/actions/*.nemo_action

%files -n %{name}-nautilus

%files -n %{name}-caja
%endif

