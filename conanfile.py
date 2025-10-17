import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "templates"))

from base_conanfile import OpenSSLFoundationConan
from conan.tools.files import copy


class OpenSSLFIPSDataConan(OpenSSLFoundationConan):
    name = "openssl-fips-data"
    version = "140-3.1"
    description = "FIPS 140-3 certificates and compliance data"
    license = "Public-Domain"
    url = "https://github.com/sparesparrow/openssl-fips-policy"
    exports_sources = "fips-140-3/*"

    def init(self):
        super().init()
        # FIPS data should always be from stable channel for compliance
        if not os.getenv("CONAN_CHANNEL"):
            self.channel = "stable"

    def package(self):
        copy(self, "*", src=self.source_folder, dst=self.package_folder)

    def package_info(self):
        super().package_info()
        self.runenv_info.define("FIPS_DATA_ROOT", self.package_folder)
        self.cpp_info.set_property("fips_certificate", "4985")
        self.runenv_info.define("FIPS_CERTIFICATE_ID", "4985")
