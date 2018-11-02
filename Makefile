SCRIPTS_TO_TEST := scripts/android/androidx-refactor.sh scripts/android/generate-material-mappings.sh scripts/misc/iptables_allow scripts/tg_bots/uno-bot-setup
SCRIPTS_TO_TEST += scripts/vpn/algo-setup scripts/vpn/streisand-setup

test:
		@shellcheck ${SCRIPTS_TO_TEST}
		@find . -type f -name *.py -exec pylint3 {} \;

.PHONY: test