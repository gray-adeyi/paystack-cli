build-linux:
	echo "building for linux..."
	pyinstaller --onefile paystack_cli/main.py --name paystack