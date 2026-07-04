counting()
{
	if [ "$1" -le 0 ]; then
		
		echo "Invalid input"
	else	
		a=0
		for ((i = 1; i <= $1; i++))
		do
			a=$((a + 1))
			echo "$a"
		done
	fi
}

alias 360='chmod 360'




