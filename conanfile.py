#!/usr/bin/env python3
"""
OpenSSL FIPS Policy Package Recipe
Provides FIPS 140-3 compliance configuration and policy files
"""

from conan import ConanFile
from conan.tools.files import copy, save
from conan.tools.cmake import CMakeToolchain, CMakeDeps, cmake_layout
import os


class OpenSSLFipsPolicyConan(ConanFile):
    name = "openssl-fips-policy"
    version = "3.3.0"
    description = "OpenSSL FIPS 140-3 compliance policy and configuration"
    license = "Apache-2.0"
    homepage = "https://www.openssl.org"
    topics = ("openssl", "fips", "security", "compliance")

    settings = "os", "arch", "compiler", "build_type"

    def export_sources(self):
        copy(self, "*", src=self.source_folder, dst=self.export_sources_folder)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        tc = CMakeToolchain(self)
        tc.generate()

    def package(self):
        """Package FIPS policy files"""
        # Copy FIPS configuration files
        copy(self, "*.cnf", src=self.source_folder, dst=os.path.join(self.package_folder, "res"))
        copy(self, "*.md", src=self.source_folder, dst=os.path.join(self.package_folder, "res"))

        # Copy license
        copy(self, "LICENSE*", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))

    def package_info(self):
        """Provide FIPS policy information"""
        # Set FIPS configuration path
        fips_config = os.path.join(self.package_folder, "res", "fipsmodule.cnf")
        self.conf_info.define("openssl:fips_config", fips_config)

        # Set environment variables for consumers
        self.env_info.OPENSSL_FIPS = "1"
        self.env_info.OPENSSL_CONF = fips_config

        # Add to PATH for FIPS utilities
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
