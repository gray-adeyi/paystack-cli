build-linux:
	echo "building for linux..."
	pyinstaller --onefile src/paystack_cli/__main__.py --name paystack