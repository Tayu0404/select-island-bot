docker run \
	--name island -it --rm --init\
	--env-file=environment_variable.txt\
	select-island 
