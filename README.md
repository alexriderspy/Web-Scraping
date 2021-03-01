# Web-Scraping
Hello friends! 
Fun Fact: Before starting the devclub assignment, I had no idea whatsoever about python and web-scraping
Fun Fact2: Now after completing both the main task and the bonus tasks, I am humble enough to say I know quite a bit about both ;)
First coming to moodleLogin.py, 
you have to provide your username and password via command prompt/anaconda powershell whatever you use to run your python code and lo! you are logged in

Now coming to fetch_around.py 
I have implemented a basic version having just the main task specifications (strictly followed :))
You provide the contest number in argument and lo! you have all the problems and the input and output files in your directory. Well who would have thought 
web-scraping could be so useful.

Now the bonus tasks:: well they were pretty cool.
Bonus Task 1:: You need to provide number of past contests in argument. And yes my code automatically takes you to the site and brings all the 6-7 problems of each 
contest there in your directory. Wonderful isn't it?
Bonus Task 2:: Here you need to provide min diff and max diff in the arguments in that order and now you need to provide in input the number of problems 
you wish to scrape and there you go you have everything in your directory.

But now there is always some kind of exception or the other. Be it the xpath changed or maybe the title link text got altered or maybe even be a connection timeout
(in case of poor connection) so we need to always be able to leave it and move on
and yes so my code handles every such exception in a neat manner in multiple nested try-except blocks. So there you go no need to worry about stopping midway.

Hope you enjoy my code



.
