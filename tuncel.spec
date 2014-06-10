
Name:		tuncel
Summary:	Servicemenu or Actions for various desktops
Version:	1.4
Release:	%mkrel 1

License:	GPLv2
Group:		Development/Other
Source0:	https://github.com/tarakbumba/%{name}/archive/%{name}-%{version}.tar.gz
URL:		https://github.com/tarakbumba/tuncel

BuildRequires:	kdelibs4-core
BuildRequires:	gettext-devel
BuildRequires:  kde4-macros
BuildRequires:  zenity
BuildRequires:  kdialog

BuildArch:      noarch

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


%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh

%configure  --sysconfdir=%{_sysconfdir}

%make

%install

%makeinstall_std
mv %{buildroot}%{_kde_services}/ServiceMenus/%{name}_kde4.desktop \
	%{buildroot}%{_kde_services}/ServiceMenus/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README.md
%config (noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}

%files -n %{name}-kde4
%{_kde_services}/ServiceMenus/%{name}.desktop

%files -n %{name}-nautilus-data
%{_datadir}/file-manager/actions/*.desktop

%files -n %{name}-nemo
%{_datadir}/nemo/actions/*.nemo_action

%files -n %{name}-nautilus

%files -n %{name}-caja

