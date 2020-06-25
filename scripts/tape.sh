entry="main.py"
output="onefile.py"

while getopts e:o: OPT
do
	case $OPT in 
		"e" ) entry=${OPTARG};;
		"o" ) output=${OPTARG};;
	esac
done

stickytape ${entry} > "build/${output}"