%global  kf_version 6.18.0

Name:           kf6-kpty
Version:        6.18.0
Release:        0%{?dist}
Summary:        KDE Frameworks 6 Tier 2 module providing Pty abstraction

License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  libutempter-devel
BuildRequires:  qt6-qtbase-devel

# runtime calls %%_libexexdir/utempter/utempter
Requires:       libutempter

%description
KDE Frameworks 6 tier 2 module providing Pty abstraction.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-kcoreaddons
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
# If seems to, for some reason, not find utempter without the following:
%cmake_kf6 -DUTEMPTER_EXECUTABLE:PATH=/usr/libexec/utempter/utempter
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Pty.so.*

%files devel
%{_kf6_includedir}/KPty/
%{_kf6_libdir}/libKF6Pty.so
%{_kf6_libdir}/cmake/KF6Pty/
