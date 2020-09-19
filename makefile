install:
	pyinstaller --noconfirm --onefile --clean --distpath=target --workpath=/tmp --specpath=/tmp gitter/entrypoint.py --name gt

run:
	./target/gt