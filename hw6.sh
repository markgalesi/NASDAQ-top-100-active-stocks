if [ -f tagsoup-1.2.1.jar ]
then
	echo
else
	$(wget http://vrici.lojban.org/~cowan/XML/tagsoup/tagsoup-1.2.1.jar)
fi


n=0
while [ $n -lt 61 ]
do
	datehtml=$(date +"%Y-%m-%d-%H-%M-%S").html
	datexhtml=$(date +"%Y-%m-%d-%H-%M-%S").xhtml
	$(wget wsj.com/mdc/public/page/2_3021-activnnm-actives.html)
	$(mv 2_3021-activnnm-actives.html $datehtml) 
	$(java -jar tagsoup-1.2.1.jar --files $datehtml)
	$(python3 script.py $datexhtml)
	(( n++ ))
	sleep 60
done
