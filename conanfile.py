import os
from conan import ConanFile
from conan.tools.files import copy


class OpenSSLFIPSDataConan(ConanFile):
    name = "openssl-fips-data"
    version = "140-3.2"
    description = "FIPS 140-3 certificates and compliance data"
    license = "Public-Domain"
    url = "https://github.com/sparesparrow/openssl-fips-policy"
    exports_sources = "fips-140-3/*"

    def init(self):
        # FIPS data should always be from stable channel for compliance
        if not os.getenv("CONAN_CHANNEL"):
            self.user = "sparesparrow"
            self.channel = "stable"

    def package(self):
        copy(self, "*.json", src=os.path.join(self.source_folder, "fips-140-3"), 
             dst=os.path.join(self.package_folder, "fips-140-3"), keep_path=True)
        copy(self, "*.txt", src=os.path.join(self.source_folder, "fips"), 
             dst=os.path.join(self.package_folder, "fips"), keep_path=True)
        copy(self, "*.sh", src=os.path.join(self.source_folder, "scripts"), 
             dst=os.path.join(self.package_folder, "scripts"), keep_path=True)

    def package_info(self):
        self.runenv_info.define("FIPS_DATA_ROOT", self.package_folder)
        self.cpp_info.set_property("fips_certificate", "4985")
        self.runenv_info.define("FIPS_CERTIFICATE_ID", "4985")
