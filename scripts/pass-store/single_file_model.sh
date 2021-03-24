#!/usr/bin/env bash

set -euxo pipefail

# Takes a password store of the format $PASSWORD_STORE_DIR/topdir/domain.tld/username and converts it to
# $PASSWORD_STORE_DIR/topdir/domain.tld with the username appended to the pass file contents themselves.

GPG_OPTS=( "--quiet" "--yes" "--compress-algo=none" "--no-encrypt-to" "--batch" "--use-agent" )
fd -td --maxdepth 1 | while read -r directory; do
  if [ $(fd . $directory | wc -l) -eq 1 ]; then
    content="$(gpg --decrypt "$(fd . $directory)")"
    username="$(basename $(fd . $directory))"
    username="${username%.*}"
    printf "%s\nusername: %s\n" "${content}" "${username}" > "${directory}.gpg.tmp"
    cat "${directory}.gpg.tmp" | gpg -e -r "me@msfjarvis.dev" "${GPG_OPTS[@]}" -o "${directory}.gpg" "${GPG_OPTS[@]}"
    rm -rf "${directory}" "${directory}.gpg.tmp"
    git add "${directory}" "${directory}.gpg"
    git commit -m "$(basename $(pwd))/${directory}: switch to single-file model"
  fi
done
