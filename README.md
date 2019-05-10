In this project, we use policy gradient method to train the building energy control network. [Building Controls Virtual TestBed](https://simulationresearch.lbl.gov/bcvtb/Download) is adopted to co-simulate and exchange data iteratively between Energyplus and our policy network.  

## Installation of BCVTB  
#### Windows  
[download BCVTB](https://simulationresearch.lbl.gov/bcvtb/Download)  
[download java environment](https://www.java.com/en/download/win10.jsp)  
open BCVTB.jar in /bin and open example xml files through 'File->open'  

#### Linux  
download BCVTB  
$ wget http://github.com/lbl-srg/bcvtb/releases/download/v1.6.0/bcvtb-install-linux64-v1.6.0.jar  
install java  
$ sudo apt-get update  
$ java -version # check if java already installed  
$ sudo apt-get install openjdk-8-jre  
$ sudo apt-get install icedtea-8-plugin (option)  
install BCVTB    
$ java -jar bcvtb-install-linux64-v1.6.0.jar  
