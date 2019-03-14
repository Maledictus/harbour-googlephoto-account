TEMPLATE = aux

DISTFILES += rpm/harbour-googlephoto-account.spec \
    accounts/provider/googlephoto.provider \
    accounts/services/googlephoto-sharing.service \
    accounts/ui/googlephoto.qml \
    accounts/ui/GooglePhotoSettingsDisplay.qml \
    accounts/ui/googlephoto-settings.qml \
    accounts/ui/googlephoto-update.qml \
    accounts/services/googlephoto-images.service

accounts.files = accounts
accounts.path = /usr/share
INSTALLS += accounts
