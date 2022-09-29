@ECHO OFF
rm -rf executable/build
rm -rf executable/dist
pyinstaller executable\mainOriginal.spec --workpath executable\build --distpath executable\dist