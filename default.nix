{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonPackage {
  pname = "diskusage";
  version = "0.1";
  src = ./.;

  # Not a modern pyproject package:
  format = "other";

  # No runtime deps for this minimal script:
  propagatedBuildInputs = [ ];

  installPhase = ''
    mkdir -p $out/bin
    cp diskusage.py $out/bin/diskusage
    chmod +x $out/bin/diskusage
  '';
}
