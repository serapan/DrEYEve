<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Περιεχόμενα</summary>
  <ol>
    <li>
      <a href="#σχετικά-με-την-εφαρμογή">Σχετικά με την εφαρμογή</a>
      <ul>
        <li><a href="#προγραμματιστικά-εργαλεία">Προγραμματιστικά εργαλεία</a></li>
        <li><a href="#επιμέρους-συστατικά-του-συστήματος">Επιμέρους συστατικά του συστήματος</a></li>
        <li><a href="#πορεία-των-δεδομένων-στο-σύστημα">Πορεία των δεδομένων στο σύστημα</a></li>
      </ul>
    </li>
    <li>
      <a href="#παρουσίαση-του-κώδικα">Παρουσίαση του κώδικα</a>
      <ul>
        <li><a href="#σύκριση-και-αξιολόγηση-μοντέλων-μηχανικής-μάθησης">Σύκριση και αξιολόγηση μοντέλων μηχανικής μάθησης</a></li>
        <li><a href="#εκπαίδευση-του-μοντέλου-LSTM">Εκπαίδευση του μοντέλου LSTM</a></li>
        <li><a href="#ανάλυση-επεξεργασία-και-αποθήκευση-δεδομένων">Ανάλυση, επεξεργασία και αποθήκευση δεδομένων</a></li>
        <li><a href="#REST-API-και-frontend">REST API και frontend</a></li>
        <li><a href="#Αρχικοποίηση-και-προσομοίωση-της-λειτουργίας-του-συστήματος">Αρχικοποίηση και προσομοίωση της λειτουργίας του συστήματος</a></li>
      </ul>
    </li>
    <li><a href="#εγκατάσταση">Εγκατάσταση</a></li>
    <ul>
        <li><a href="#MongoDB">MongoDB</a></li>
        <li><a href="#Apache-Kafka">Apache Kafka</a></li>
        <li><a href="#Apache-Spark">Apache Spark</a></li>
        <li><a href="#PostgreSQL">PostgreSQL</a></li>
        <li><a href="#Απαιτούμενες-βιβλιοθήκες-python">Απαιτούμενες βιβλιοθήκες python</a></li>
      </ul>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Σχετικά με την εφαρμογή

Το DrEYEve είναι μια εφαρμογή η οποία αναπτύχθηκε στο πλαίσιο εκπόνησης της διπλωματικής μου εργασίας με σκοπό την ολοκλήρωση των προπτυχιακών σπουδών. Πιο συγκεκριμένα, έχει υλοποιηθεί ένα σύστημα ανάλυσης και εξαγωγής οδηγικών προφίλ, τα οποία προκύπτουν από οδηγικά δεδομένα που συλλέγονται και αποθηκεύονται σε πλατφόρμα δεδομένων μεγάλης κλίμακας, με εφαρμογή σύγχρονων μεθόδων μηχανικής μάθησης, στα πλαίσια ανάπτυξης των ευφυών συστημάτων μεταφορών. Το σύστημα που υλοποιήθηκε προσφέρει τη δυνατότητα λήψης και επεξεργασίας των δεδομένων σε πραγματικό χρόνο καθώς και την ιστορική αναδρομή αυτών, με σκοπό την αξιολόγηση της οδηγικής συμπεριφοράς των χρηστών που έχουν επιλέξει να συμμετέχουν σε αυτό. 

### Προγραμματιστικά εργαλεία

Τα προγραμματιστικά εργαλεία τα οποία χρησιμοποιούνται από το σύστημα DrEYEve είναι τα εξής:

* [MongoDB](https://www.mongodb.com/)
* [Apache Kafka](https://kafka.apache.org/)
* [Apache Spark](https://spark.apache.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Python Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Vue.js](https://vuejs.org/)

### Επιμέρους συστατικά του συστήματος

Το σύστημα αποτελείται από τα εξής επιμέρους συστατικά:
* Μια βάση δεδομένων MongoDB
* Ένα μέσιτη (Apache Kafka Broker)
* Έναν καταναλωτή (Apache Kafka Consumer)
* Έναν αναλυτή δεδομένων (Apache Spark)
* Ένα νευρωνικό δίκτυο LSTM
* Μια βάση δεδομένων PostgreSQL
* Ένα REST API (Python Flask)

### Πορεία των δεδομένων στο σύστημα

![alt text](https://github.com/serapan/DrEYEve/blob/main/system.png)

Το σύνολο δεδομένων που χρησιμοποιήθηκε στο πλάισιο υλοποίησης του συστήματος είναι το [Traffic, Driving Style and Road Surface Condition](https://www.kaggle.com/gloseto/traffic-driving-style-road-surface-condition).

Συνοπτικά, η πορεία που ακολουθούν τα δεδομένα κατά μήκος του συστήματος είναι η εξής:
* Τα οδηγικά δεδομένα συλλεγόνται και αποθηκεύονται στη βάση δεδομένων MongoDB.
* Τα οδηγικά δεδομένα με αυτοματοποιημένο τρόπο τοποθετούνται στο μεσίτη του συστήματος. Για τον σκοπό αυτό χρησιμοποιήθηκε το [MongoDB Kafka Connector](https://docs.mongodb.com/kafka-connector/current/).
* Τα οδηγικά δεδομένα οδηγούνται στον καταναλωτή του συστήματος ο οποίος φροντίζει για την ομαδοποίησή τους.
* Τα ομαδοποιημένα οδηγικά δεδομένα οδηγούνται στον αναλυτή του συστήματος ο οποίος τα επεξεργάζεται και τα μετατρέπει σε βαθμολογικά σχήματα τα οποία αντικατοπτρίζουν την επιθετικότητα της συμπεριφοράς του οδηγού του εκάστοτε οχήματος για κάποιο συγκεκριμένο χρονικό διάστημα. Για την ανάλυση και την εξαγωγή συμπερασμάτων από τα ομαδοποιημένα οδηγικά δεδομένα, ο αναλύτης κάνει χρήση του νευρωνικού δικτύου LSTM.
* Οι βαθμολογίες, οι οποίες έχουν προκύψει από τα ομαδοποιημένα οδηγικά δεδομένα, αποθηκεύονται σε μια σχεσιακή βάση δεδομένων PostgreSQL. 
* Τα δεδομένα που έχουν αποθηκευτεί στη βάση δεδομένων PostgreSQL μπορούν να ανακτηθούν με τις κατάλληλες κλήσεις στα διάφορα endpoints του REST API του συστήματος. Επιπλέον, το REST API δύναται να λειτουργήσει και ως κλασσικός web server ο οποίος επιστρέφει html, καθώς φιλοξενεί το frontend της εφαρμογής DrEYEve μέσω του οποίου πραγματοποιείται η οπτικοποίηση των δεδομένων που έχουν αποθηκευτεί στη βάση PostgreSQL σε πραγματικό χρόνο καθώς και την ιστορική αναδρομή αυτών. 

## Παρουσίαση του κώδικα
Στο πλαίσιο εκπόνησης αυτής της διπλωματικής εργασίας δεν υλοποιήθηκε μόνο η εφαρμογή DrEYEve. Καθώς η εφαρμογή κάνει χρήση κάποιου μοντέλου μηχανικής προκειμένου να εξάγει αξιοποιήσιμη πληροφορία από τα οδηγικά δεδομένα, σε ένα πρώτο στάδιο αναζητήθηκε το βέλτιστο μόντελο το οποίο θα εξυπηρετούσε τους σκοπούς του συστήματος με τον αποδοτικότερο τρόπο.   

Επομένως, ο κώδικας που αναπτύχθηκε για την υλοποίηση του συστήματος μπορεί να διακριθεί σε πέντε επιμέρους κατηγορίες:
* Τον κώδικα που αφορά την εκπαίδευση και την σύγκριση διάφορων μοντέλων μηχανικής μάθησης με σκοπό την εύρεση του αποδοτικότερου μοντέλου.
* Τον κώδικα που αφορά την εκπαίδευση του μοντέλου μηχανικής μάθησης που βρέθηκε ότι είναι το αποδοτικότερο με σκοπό την ενσωμάτωση του στο συστήμα.
* Τον κώδικα που αφορά την αποθήκευση, την ανάλυση και την επεξεργασία των οδηγικών δεδομένων καθώς αυτά εισέρχονται στο σύστημα.
* Τον κώδικα που αφορά την ανάπτυξη του REST API και του frontend με σκοπό την ανάκτηση και την οπτικόποιηση των δεδομένων.
* Τον κώδικα που αφορά την αρχικοποίηση και την προσομοίωση της λειτουργίας του συστήματος.

Σε αυτό το σήμειο θα πρέπει να παρουσιαστεί ο κώδικας που βρίσκεται στον φάκελο app_ml/functionalities καθώς είναι κώδικας γενικού σκοπού και χρησιμοποιείται σε διάφορα επιμέρους σημεία. Στο αρχείο constants.py ορίζονται σταθέρες μεταβλητές που χρησιμοποιόυνται από άλλα κομμάτια κώδικα. Στο αρχείο preprocessing.py ορίζονται συναρτήσεις που αφορούν την προεπεξεργασία δεδομένων που προέρχονται από αρχεία csv. Τέλος, στο αρχείο preprocessing_mongo.py ορίζονται συναρτήσεις που αφορούν την προεπεξεργασία δεδομέων που προέρχονται από τη βάση δεδομένων MongoDB του συστήματος.

Τέλος, ο φάκελος running_scripts περιέχει scripts τα οποία είναι γραμμένα σε bash και διευκολύνουν την εκτέλεση της εφαρμογής. Τα αρχεία αυτά παρουσιάζονται αναλυτικότερα παρακάτω που γίνεται η περιγραφή του τρόπου εκτέλεσης της εφαρμογής.

### Σύκριση και αξιολόγηση μοντέλων μηχανικής μάθησης

Στον φάκελο app_ml/models ορίζονται τα μοντέλα τα οποία εξετάστηκαν. Τα αρχεία TimeModel.py και TimelessModel.py ορίζουν δύο βασικές κλάσεις οι οποίες χρησιμοποιούνται για την κατασκευή μοντέλων που διαχειρίζονται δεδομένα χρονοσειρών η απλές εγγραφές δεδομένων, αντίστοιχα. Στα υπόλοιπα αρχεία ορίζονται οι κλάσεις των μοντέλων που εξετάστηκαν. Η παραμετροποίηση κάθε μόντελου έχει οριστεί εκ των προτέρων με τις βέλτιστες τίμες (για το εκάστοτε μοντέλο), οι οποίες βρέθηκαν με χρήση του αλγορίθμου GridSearchCV.

Στον φάκελο app_ml/train βρίσκεται τα αρχείο train_all_models.py και generate_data.py. Με την εκτέλεση του αρχείου generate_data.py πραγματοποιείται μια προεπεξεργασία των αρχείων του συνόλου δεδομένων [Traffic, Driving Style and Road Surface Condition](https://www.kaggle.com/gloseto/traffic-driving-style-road-surface-condition), έτσι ώστε τα δεδομένα να έρθουν σε μορφή που εξυπηρετεί την εκπαίδευση των μοντέλων. Τα νέα αρχεία csv που προκύπτουν αποθηκεύονται στον φάκελο app_ml/train/generated_data. Με την εκτέλεση του αρχείου train_all_models.py πραγματοποιείται η εκπαίδευση όλων των μοντέλων που ορίζονται στον φάκελο app_ml/models με σύνολο δεδομένων τα δεδομένα που βρίσκονται στον φάκελο app_ml/train/generated_data, ενώ παράλληλα τυπώνονται και τα αποτελέσματα που επιτεύχθηκαν από το κάθε μοντέλο. Προτείνεται η ανακατεύθυνση της εξόδου του προγράμματος train_all_models.py σε κάποιο αρχείο και όχι στην κονσόλα καθώς τα αποτελέσματα και εκπαίδευση των μοντέλων οδηγούν σε εκτύπωση μεγάλου όγκου χαρακτήρων. 

### Εκπαίδευση του μοντέλου LSTM

Από τη σύγκριση και την αξιολόγιση των μοντέλων μηχανικής μάθησης προέκυψε ότι το αποδοτικότερο μοντέλο ήταν το νευρωνικό δίκτυο LSTM. Για την εκπαίδευση του LSTM χρησιμοποιείται το αρχείο app_ml/train/train_rnn.py μέσω του οποίου ορίζεται το νευρωνικό δίκτυο LSTM, εκπαιδεύεται με σύνολο δεδομένων όλα τα δεδομένα που βρίσκονται στη βάση MongoDB του συστήματος και τελικά αποθηκεύεται στον φάκελο RNN_MODEL έτσι ώστε να μπορεί να χρησιμοποιηθεί από τον αναλυτή δεδομένων του συστήματος.

### Ανάλυση, επεξεργασία και αποθήκευση δεδομένων

Στον φάκελο app_ml/predict βρίσκονται τα αρχεία kafka_consumer.py και spark_predict.py, στα οποία ορίζονται ο καταναλωτής και ο αναλυτής δεδομένων του συστήματος, αντίστοιχα.

### REST API και frontend

Για τη δημιουργία του frontend χρησιμοποιήθηκε το Vue framework. Στον φάκελο vue-app βρίσκεται ο κώδικας που σχετίζεται με την ανάπτυξη του frontend, ο οποίος ακολουθεί την τυπική οργάνωση μιας vue εφαρμογής.

Στον φάκελο app_web βρισκέται ο κώδικας που αφορά την υλοποίηση του REST API του συστήματος και ο οποίος περιέχει τα βασικά αρχεία db.py, functionalities.py, controllers.py και rest_server.py. Στο αρχείο db.py ορίζεται το σχήμα της βάσης PostgreSQL του συστήματος. Στο αρχείο functionalities.py ορίζονται κάποιες συναρτήσεις που χρησιμοποιούνται από το αρχείο controllers.py για τον μετασχηματισμό διάφορων δεδομένων. Στο αρχείο controllers.py ορίζονται οι συναρτήσεις που εκτελούνται για τις κλήσεις στα διάφορα endpoints του συστήματος. Στο αρχείο rest_server.py ορίζεται ο web server της εφαρμογής καθώς και τα διάφορα endpoints τα οποία εξυπηρετεί. Τέλος, θα πρέπει να αναφερθεί ότι στον φάκελο app_web έχουν τοποθετηθεί και τα αρχεία που έχουν προκύψει από το build της vue εφαρμογής του φακέλου vue-app. 

### Αρχικοποίηση και προσομοίωση της λειτουργίας του συστήματος

Στον φάκελο app_ml/data βρίσκονται τα αρχεία mongo_data_init.py, postgres_data_init.py και insert_data_to_postgres.py, τα οποία σχετίζονται με την αρχικοποιήση των βάσεων δεδομένων MongoDB και PostgreSQL του συστήματος. Στο αρχείο mongo_data_init.py ορίζεται η βάση MongoDB του συστήματος και τοποθετούνται τα δεδομένα δύο αρχείων csv του συνόλου δεδομένων [Traffic, Driving Style and Road Surface Condition](https://www.kaggle.com/gloseto/traffic-driving-style-road-surface-condition) καθώς τα άλλα δύο χρησιμοποιούνται για την προσομείωση της λειτουργίας του συστήματος. Στο αρχείο postgres_data_init.py ορίζεται η βάση PostgreSQL του συστήματος, ενώ το αρχείο insert_data_to_postgres.py χρησιμοποιείται για την τοποθέτηση των δεδομένων που παραγόνται από τα αντίστοιχα δεδομένα των δύο αρχείων csv, που τοποθετήθηκαν στη βάση MongoDB, σε αυτήν.

Στον φάκελο app_ml/data βρίσκεται επίσης και το αρχείο stream_data.py. Το αρχείο αυτό χρησιμοποιείται για την παραγώγη δεδομένων σε πραγματικό χρόνο, από τα δύο εναπομείναντα αρχεία του συνόλου δεδομένων [Traffic, Driving Style and Road Surface Condition](https://www.kaggle.com/gloseto/traffic-driving-style-road-surface-condition), με σκοπό την προσομοίωση της λειτουργίας του συστήματος. Προφανώς, η εκτέλεση του αρχείου αυτού έχει νόημα μόνο όταν όλα τα συστατικά του συστήματος βρίσκονται σε κατάσταση λειτουργίας.


## Εγκατάσταση

Η διαδικάσια που περιγράφεται παρακάτω πραγματοποιήθηκε σε μηχάνημα με λειτουργικό σύστημα Ubuntu 20.04 LTS. Ωστόσο, η ίδια διαδικασία μπορεί να ακολουθηθεί, θεωρητικά τουλάχιστον, για οποιαδήποτε debian διανομή.

### MongoDB

Για την εγκατάσταση της MongoDB εκτελούμε σε ένα τερματικό τις εξής εντολές:
```shell
  curl -fsSL https://www.mongodb.org/static/pgp/server-4.8.asc | sudo apt-key add -
  echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
  sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 656408E390CFB1F5
  sudo apt update
  sudo apt install mongodb-org
```

Για την διαμόρφωση της MongoDB προσθέτουμε στο αρχείο /etc/mongod.conf τις γραμμές:
```shell
  replication:
    replSetName: "rs0"
```

Έπειτα, εκτελούμε τις εντολές:
```shell
  sudo systemctl enable mongod.service
  sudo systemctl start mongod.service
  mongo
  rs.initiate()
  quit()
  sudo systemctl restart mongod.service
```
### Apache Kafka

Για την εγκατάσταση του Apache Kafka εκτελούμε σε ένα τερματικό τις εξής εντολές:
```shell
wget https://ftp.cc.uoc.gr/mirrors/apache/kafka/2.8.0/kafka_2.13-2.8.0.tgz
tar zxvf kafka_2.13-2.8.0.tgz
rm kafka_2.13-2.8.0.tgz
cd kafka_2.13-2.8.0
sudo mkdir /opt/kafka
sudo mv ./* /opt/kafka
```

Για την εγκατάσταση του MongoDB Kafka Connector εκτελούμε σε ένα τερματικό τις εξής εντολές:
```shell
  wget https://repo1.maven.org/maven2/org/mongodb/kafka/mongo-kafka-connect/1.1.0/mongo-kafka-connect-1.1.0-all.jar
  sudo mkdir /opt/kafka/plugins
  sudo mv mongo-kafka-connect-1.1.0-all.jar /opt/kafka/plugins
```

Για την διαμόρφωση του Apache Kafka προσθέτουμε στο αρχείο ~/.bashrc τις γραμμές:
```shell
  export KAFKA_HOME=/opt/kafka
  export PATH=$KAFKA_HOME/bin:$PATH
```

Έπειτα, εκτελούμε την εντολή:
```shell
  source ~/.bashrc
```

### Apache Spark

Για την εγκατάσταση του Apache Spark εκτελούμε σε ένα τερματικό τις εξής εντολές:
```shell
wget https://ftp.cc.uoc.gr/mirrors/apache/spark/spark-3.0.2/spark-3.0.2-bin-hadoop3.2.tgz
tar zxvf spark-3.0.2-bin-hadoop3.2.tgz
rm spark-3.0.2-bin-hadoop3.2.tgz
cd spark-3.0.2-bin-hadoop3.2.tgz
sudo mkdir /opt/spark
sudo mv ./* /opt/spark
```

Για την ορθή λειτουργία του Spark απαιτείται και η εγκατάσταση του [Apache Hadoop](https://hadoop.apache.org/). Για την εγκατάσταση του Apache Hadoop εκτελούμε σε ένα τερματικό τις εξής εντολές:

```shell
wget https://ftp.cc.uoc.gr/mirrors/apache/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz
tar zxvf hadoop-3.3.0.tar.gz
rm hadoop-3.3.0.tar.gz
cd hadoop-3.3.0.tar.gz
sudo mkdir /opt/hadoop
sudo mv ./* /opt/hadoop
```

Για την διαμόρφωση του Apache Spark προσθέτουμε στο αρχείο ~/.bashrc τις γραμμές:
```shell
  export SPARK_HOME=/opt/spark
  export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
  export PYSPARK_PYTHON=python3
  export HADOOP_HOME=/opt/hadoop
  export PATH=$PATH:$HADOOP_HOME/bin
  export JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64
```
Προσοχή!!! Στην τελευταία γραμμή θα πρέπει να τοποθετηθεί η αντίστοιχη έκδοση της java που είναι εγκατεστημένη στο μηχάνημα. Οποιαδήποτε έκδοση της java από την 8 και πάνω θα πρέπει, θεωρητικά τουλάχιστον, να λειτουργεί σωστά.

Έπειτα, εκτελούμε την εντολή:
```shell
  source ~/.bashrc
```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
