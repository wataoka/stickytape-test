# 初期値
entry="main.py"
output="onefile.py"

# オプション
while getopts e:o: OPT
do
	case $OPT in 
		"e" ) entry=${OPTARG};;
		"o" ) output=${OPTARG};;
	esac
done

# 実行
stickytape ${entry} > "build/${output}"