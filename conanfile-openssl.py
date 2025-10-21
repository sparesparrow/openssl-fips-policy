from conan import ConanFile
from conan.tools.files import download, unzip, copy, rm
from conan.tools.gnu import AutotoolsToolchain, Autotools
from conan.tools.layout import basic_layout
import os

class OpenSSLFIPSConan(ConanFile):
    name = "openssl-fips"
    version = "3.0.8"
    description = "OpenSSL with FIPS 140-3 module"
    license = "Apache-2.0"
    url = "https://github.com/sparesparrow/openssl-fips-policy"

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fips": [True, False],
    }
    default_options = {
        "shared": True,
        "fips": True,
    }

    requires = "openssl-fips-data/140-3.1"

    def layout(self):
        basic_layout(self, src_folder="src")

    def source(self):
        # Download OpenSSL source
        openssl_url = f"https://www.openssl.org/source/openssl-{self.version}.tar.gz"
        download(self, openssl_url, "openssl.tar.gz", verify=True)
        unzip(self, "openssl.tar.gz", strip_root=True)

        # Apply FIPS module if enabled
        if self.options.fips:
            # In a real implementation, you would download and integrate the FIPS module
            # For now, we'll assume the FIPS module is built into OpenSSL 3.0.8+
            pass

    def generate(self):
        tc = AutotoolsToolchain(self)
        tc.configure_args.append("--prefix=/")
        if self.options.fips:
            tc.configure_args.extend([
                "enable-fips",
                "--with-fips-module=/usr/local/lib/ossl-modules/fips.so"
            ])
        tc.generate()

    def build(self):
        autotools = Autotools(self)
        self.run("chmod +x Configure")
        autotools.configure()
        autotools.make()

    def package(self):
        autotools = Autotools(self)
        autotools.install()

        # Copy FIPS module if built
        if self.options.fips:
            copy(self, "*.so", src=os.path.join(self.source_folder, "providers"),
                 dst=os.path.join(self.package_folder, "lib", "ossl-modules"), keep_path=False)

        # Clean up unnecessary files
        rm(self, "*.la", os.path.join(self.package_folder, "lib"), recursive=True)

    def package_info(self):
        self.cpp_info.libs = ["crypto", "ssl"]
        self.cpp_info.includedirs = ["include"]

        if self.options.fips:
            fips_module_path = os.path.join(self.package_folder, "lib", "ossl-modules")
            self.runenv_info.define("OPENSSL_MODULES", fips_module_path)
            self.runenv_info.define("OPENSSL_CONF", os.path.join(self.package_folder, "ssl", "openssl.cnf"))