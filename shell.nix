{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python39
    python39Packages.beautifulsoup4
    python39Packages.requests
  ];
}
