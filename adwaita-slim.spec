%global theme_name     Adwaita-Slim

Name:           adwaita-slim
Version:        3.24.0
Release:        1%{?dist}
Summary:        A slim Adwaita version for GNOME-Shell, GTK+ 2 and 3

License:        GPLv2+ or CC-BY-SA
URL:            https://github.com/polter-rnd/%{name}
Source0:        https://github.com/polter-rnd/%{name}/archive/%{version}.tar.gz

BuildArch:      noarch

%description
Adwaita Slim is a theme for GTK2/3 and GNOME-shell started out on the basis of
Adwaita, but aims at reworking the big paddings to make it look more compact.


%package gtk2-theme
Summary:        Adwaita Compact GTK+2 theme

%description gtk2-theme
Theme for GTK+2 as part of the Adwaita Compact theme.


%package gtk3-theme
Summary:        Adwaita Compact GTK+3 theme

%description gtk3-theme
Theme for GTK+3 as part of the Adwaita Compact theme.


%package gnome-shell-theme
Summary:        Adwaita Compact GNOME-Shell theme
Requires:       gnome-shell

%description gnome-shell-theme
Theme for GNOME-SHell as part of the Adwaita Compact theme.

%prep

%setup -q -n %{name}-%{version}


%build
# Nothing to build

%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes/%{theme_name}
mkdir -p -m755 %{buildroot}%{_datadir}/themes/%{theme_name}-Dark

cp -pr %{theme_name}/* %{buildroot}%{_datadir}/themes/%{theme_name}
cp -pr %{theme_name}-Dark/* %{buildroot}%{_datadir}/themes/%{theme_name}-Dark

%files gtk2-theme
%dir %{_datadir}/themes/%{theme_name}/
%{_datadir}/themes/%{theme_name}/gtk-2.0/


%files gtk3-theme
%dir %{_datadir}/themes/%{theme_name}/
%{_datadir}/themes/%{theme_name}/gtk-3.0/


%files gnome-shell-theme
%dir %{_datadir}/themes/%{theme_name}/
%{_datadir}/themes/%{theme_name}/gnome-shell/


%changelog
* Fri Nov 30 2018 Paul Artsishevsky <polter.rnd@gmail.com> 3.24.0-1
- Renamed to Adwaita-Slim
- Updated to support GTK 3.24 and GNOME 3.30

* Mon Jan 2 2017 Paul Artsishevsky <polter.rnd@gmail.com> 3.22.0-1
- Initial spec (based on Adwaita theme)
