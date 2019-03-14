Name:       harbour-googlephoto-account

%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}

Summary:    Account extension for GooglePhoto
Version:    0.1
Release:    1
Group:      Applications/System
License:    The MIT License (MIT)
URL:        https://github.com/Maledictus/harbour-googlephoto-account
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-googlephoto-account.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(accounts-qt5)
BuildRequires:  pkgconfig(libsignon-qt5)

%description
Account extension for GooglePhoto

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(644,root,root,-)
%{_datadir}/accounts/services/*.service
%{_datadir}/accounts/providers/*.provider
%{_datadir}/accounts/ui/*.qml
