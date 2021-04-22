===================================================================== Εγκατάσταση Εφαρμογής =====================================================================

1) MongoDB: 
  ==> Εγκατάσταση (Ubuntu 20.04): 
  	curl -fsSL https://www.mongodb.org/static/pgp/server-4.8.asc | sudo apt-key add -
	echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
	sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 656408E390CFB1F5
	sudo apt update
	sudo apt install mongodb-org

  ==> Config (δημιουργία pseudo replica set. απαιτείται για το kafka): 
  	sudo systemctl enable mongod.service
  	sudo vim /etc/mongod.conf --> Προσθήκη γραμμής
  				replication:
  					replSetName: "rs0"
  	reboot (ή restart το service πιθανότατα)
	mongo
	rs.initiate()

2) PostgreSQL:
  ==> Εγκατάσταση (Ubuntu 20.04):
  	sudo apt install postgresql
  
  ==> Config:
  	sudo vim /etc/postgresql/12/main/pg_hba.conf --> Προσθήκη γραμμών
  		local   all             postgres                                md5
  		local   all             all                                     md5 (ίσως περιττή)	
  
  ==> Αλλαγή κωδικού του χρήστη postgres σε 'postgres':
  	sudo -u postgres psql
  	\password postgres
  	\q
  	sudo systemctl restart postgresql.service

3) Kafka:
  ==> Εγκατάσταση (Ubuntu 20.04):
  	download from apache website, unzip and put in /opt/kafka (είχα κατεβάσει το precompiled για scala 2.13 νομίζω)
  	sudo vim ~/.bashrc --> Προσθήκη γραμμών
  		export KAFKA_HOME=/opt/kafka
		export PATH=$KAFKA_HOME/bin:$PATH
	source ~/.bashrc

  ==> Εγκατάσταση του MongoConnector:
  	download MongoKafkaConnector jar from https://search.maven.org/artifact/org.mongodb.kafka/mongo-kafka-connect/1.1.0/jar (επιλογή του all.jar)
  	mkdir /opt/kafka/plugins και βάζουμε μέσα το jar
  
4) Spark και Hadoop:
  ==> Εγκατάσταση (Ubuntu 20.04):
  	download apache spark from apache website (Pre-built for apache hadoop 3.2 or later), unzip and put in /opt/spark
  	sudo vim ~/.bashrc --> Προσθήκη γραμμών
  		export SPARK_HOME=/opt/spark
		export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
		export PYSPARK_PYTHON=python3
	source ~/.bashrc
	download hadoop binaries from apache website (version 3.3.0), unzip and put in /opt/hadoop
	sudo vim ~/.bashrc --> Προσθήκη γραμμών
		export HADOOP_HOME=/opt/hadoop
		export PATH=$PATH:$HADOOP_HOME/bin
		export JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64
	source ~/.bashrc

  ==> Config (για να μην εμφανίζονται κάποια συγκεκριμένα warnings):
  	sudo vim /opt/spark/conf/spark-defaults.conf --> Προσθήκη γραμμών
  		spark.driver.extraJavaOptions="-Dio.netty.tryReflectionSetAccessible=true"
		spark.executor.extraJavaOptions="-Dio.netty.tryReflectionSetAccessible=true"
		
=================================================================================================================================================================

======================================================================= Τρέξιμο Εφαρμογής =======================================================================

Υποθέτοντας οτι βρισκόμαστε μέσα στο φάκελο running_scripts: !!! Τα .sh αρχεία κατά κύριο λόγο απλά τρέχουν αρχεία python του κώδικα !!!

1) Τρέχουμε το ./data_init.sh:
	==> Δημιουργεί τη βάση mongo
	==> Βάζει 2/4 διαδρομές στη βάση mongo (εχώ βάλει τις δύο διαδρομές να ανήκουν στον ίδιο οδηγό και καλά)
	==> Δημιουργεί τη βάση postgres (για να γίνει αυτό δεν πρέπει να υπάρχει ενέργο connection στη βάση καθώς προσπαθεί να τη κάνει drop σε περίπτωση που 	    υπάρχει)
	==> Βάζει τα αντίστοιχα δεδομένα διαδρομών της mongo στη postgres (τα δεδομένα αυτά προκύπτουν από predictions rnn μοντέλου που έχει αποθηκευτεί)

2) Τρέχουμε το ./start_kafka_server.sh: Ξεκινάει τον kafka server

3) Τρέχουμε το ./kafka_producer_consumer.sh: 
	==> Ξεκινάει τον kafka producer: Πρόκειται για τον MongoKafkaConnector ο οποίος ανιχνεύει και streamάρει ότι δεδομένα εισάγονται στη βάση mongo
	==> Ξεκινάει τον kafka_consumer: Καταναλώνει τα δεδομένα του producer, κάνει μια ομαδοποίηση τους σε 20αδες (καθώς χρησιμοποιείται rnn μοντέλο) και μέσω 		    socket τα στέλνει στο spark

4) Τρέχουμε το ./spark_receiver.sh: Ξεκινάει τον παραλήπτη δεδομένων από τον kafka_consumer. Χρήση spark streaming για διάβασμα από το socket ανά 20 δευτερόλεπτα (το 20 πάει προς αλλαγή), προεπεξεργασία δεδομένων (rdd style of course), παραγωγή αποτελεσμάτων πρόβλεψης μοντέλου rnn και αποθήκευση αυτών στη postgres.

5) Τρέχουμε το ./rest_server.sh: Ξεκινάει τον server της restapi εφαρμογής. (Σε αυτό το σημείο είναι απαραίτητο για το streaming των δεδομένων..βλέπε παρακάτω)

6) Τρέχουμε το ./stream_data.sh: Για τα 2 αρχεία διαδρομών που έχουν μείνει αρχικά στέλνονται στον server το id του οδηγού (μοναδικό) και το id της διαδρομής (μοναδικό) που έπεται να πραγματοποιηθεί, και τα οποία αποθηκεύονται στη postgres. Στη συνέχεια προσομοιώνεται το streaming των δεδομένων τα οποία ανά ένα δευτερόλεπτο εισάγονται στη mongo. Έτσι τα παίρνει ο kafka producer, στη συνέχεια ο kafka consumer, στη συνέχεια το spark (streaming) και τελικά τα παραγόμενα αποτελέσματα αποθηκεύονται στη βάση postgres

=================================================================================================================================================================

===================================================================== Τερματισμός Εφαρμογής =====================================================================

Θα πρέπει να γίνει αναγκαστικά για να ξανατρέξει η εφαρμογή (προκειμένου να ξαναγίνει "αρχικοποίηση του kafka")

1) Ctrl+C το stream_data.sh (και ίσως λίγη αναμονή για να φτάσουν όλα τα δεδομένα στο spark)

2) Ctrl+C το spark_receiver.sh

3) Ctrl+C το kafka_producer_consumer.sh

4) Τρέχουμε το ./stop_kafka_server.sh: Τερματίζει τον kafka producer και τον kafka server

=================================================================================================================================================================
