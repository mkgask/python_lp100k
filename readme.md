# Python language processing 100 knock 2015

Trying "language processing 100 knock 2015" from Inui, Okazaki Lab in Tohoku University. (http://www.cl.ecei.tohoku.ac.jp/nlp100)

##### Requirements :

    docker
    docker-machine
    docker-compose

##### Usage :

    ./docker-compose-up-d
    eval $(docker-machine env)
    docker exec python_python_1 pyton -B storage/lp100k/00.py
