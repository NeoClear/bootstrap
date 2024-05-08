# Generates new ssh key.
# ssh-keygen -t ed25519 -C "neoclear@outlook.com"

# Installs mise
curl https://mise.run | sh

# Installs rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Installs rust-analyzer, the lsp server for Rust
rustup component add rust-analyzer

# Installs OCaml
opam init
opam install ocaml-lsp-server odoc ocamlformat utop

# Softlink Dropbox folder
ln -s $HOME/Dropbox $HOME/shrine
