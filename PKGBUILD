# Maintainer: Thomas Blair <https://github.com/ThomasB3143>

pkgname=teevee
pkgver=0.1.0
pkgrel=1
pkgdesc="Single-button cyclic launcher using dunst notifications"
arch=('any')
url="https://github.com/yourusername/teevee"
license=('MIT')
depends=('bash' 'dunst')
source=("teevee-${pkgver}.tar.gz::https://github.com/ThomasB3143/teevee/archive/v${pkgver}.tar.gz")
sha256sums=('acb1f27997f6c75d18852ad0b7ddb886b7097a8a3d27867029f70f8c9ed086c1')

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    # Main executable
    install -Dm755 teevee "${pkgdir}/usr/bin/teevee"

    # Library files
    install -d "${pkgdir}/usr/share/teevee/lib"
    install -m644 lib/*.sh "${pkgdir}/usr/share/teevee/lib/"
}
