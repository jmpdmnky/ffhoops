# ffhoops
wrapper for ffmpeg/probe


# Build instructions:
## Build Package
python -m pip install --upgrade pip
python -m pip install --upgrade build
python -m build

## Push build to repo
git add -A
git commit -m "some message"
git push

# install instructions
pip uninstall ffhoops -y
pip install git+https://github.com/jmpdmnky/ffhoops

## shortcut script for windows:
./build.ps1 -message 'some message' -skipupdates -version 2 -git -install