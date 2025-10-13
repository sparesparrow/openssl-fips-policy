from conan import ConanFile
from conan.tools.files import copy

class OpenSSLFIPSDataConan(ConanFile):
    name = "openssl-fips-data"
    version = "140-3.1"
    description = "FIPS 140-3 certificates and compliance data"
    license = "Public-Domain"
    url = "https://github.com/sparesparrow/openssl-fips-policy"
    package_type = "header-library"
    settings = None
    exports_sources = "fips-140-3/*"

    def package(self):
        copy(self, "*", src=self.source_folder, dst=self.package_folder)

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
        self.runenv_info.define("FIPS_DATA_ROOT", self.package_folder)
        self.cpp_info.set_property("fips_certificate", "4985")
