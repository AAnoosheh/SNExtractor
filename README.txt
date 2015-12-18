Python Dependencies:
——————————————————————————————————————— 
	alipy - Setup Instructions Below
	astropy - pip install
	imreg_dft - pip install
	matplotlib - pip install
	numpy - pip install
	pyraf - pip install


To Install Alipy:
—————————————————————————————————————————————————————————————————————————————— 
	svn checkout https://svn.epfl.ch/svn/mtewes-public/trunk/alipy2 ./alipy
	cd alipy
	python setup.py install


To Install Alipy Dependencies: AstroAsciiData, PyFits, Sextractor
———————————————————————————————————————————————————————————————————————————————————————————————————————— 
AstroAsciiData:
	Download from here: http://www.stecf.org/software/PYTHONtools/astroasciidata/asciidata_download.php
	Unzip asciidata-1.1.1.tar.gz
	cd asciidata-1.1.1
	python setup.py install

PyFits:
	pip install pyfits

Sextractor:
Save yourself a headache and install a very old version
	Download version 2.5 from here: https://www.astromatic.net/download/sextractor/sextractor-2.5.0.tar.gz
	cd into unzipped folder
	./configure
	make
	sudo make install

To Install HOTPANTS
———————————————————————————— 
Start by downloading HOTPANTS from Andrew Becker

For Mac:
	Instructions to install on Mac OS X are provided here: http://okomestudio.net/biboroku/?p=636
	You will first need to install Scisoft for OSX, look for a CNET link, since the dyndns is gone
