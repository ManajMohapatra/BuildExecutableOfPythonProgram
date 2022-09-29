@ECHO OFF
rm -rf executableOnefile/build
rm -rf executableOnefile/dist
pyinstaller executableOnefile\mainOnefileOriginal.spec --workpath executableOnefile\build --distpath executableOnefile\dist