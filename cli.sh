find $dir -name '*.jpg' -type f | while read -r file
do
	if ./upload.py "$file"; then
		echo ${file} >> ok
	else
		echo $?:${file} >> err
	fi
done

