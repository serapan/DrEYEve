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
        <li><a href="#ανάλυση,-επεξεργασία-και-αποθήκευση-δεδομένων">Ανάλυση, επεξεργασία και αποθήκευση δεδομένων</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
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



<!-- GETTING STARTED -->
## Παρουσίαση του κώδικα
Στο πλαίσιο εκπόνησης αυτής της διπλωματικής εργασίας δεν υλοποιήθηκε μόνο η εφαρμογή DrEYEve. Καθώς η εφαρμογή κάνει χρήση κάποιου μοντέλου μηχανικής προκειμένου να εξάγει αξιοποιήσιμη πληροφορία από τα οδηγικά δεδομένα, σε ένα πρώτο στάδιο αναζητήθηκε το βέλτιστο μόντελο το οποίο θα εξυπηρετούσε τους σκοπούς του συστήματος με τον αποδοτικότερο τρόπο.   

Επομένως, ο κώδικας που αναπτύχθηκε για την υλοποίηση του συστήματος μπορεί να διακριθεί σε πέντε επιμέρους κατηγορίες:
* Τον κώδικα που αφορά την εκπαίδευση και την σύγκριση διάφορων μοντέλων μηχανικής μάθησης με σκοπό την εύρεση του αποδοτικότερου μοντέλου.
* Τον κώδικα που αφορά την εκπαίδευση του μοντέλου μηχανικής μάθησης που βρέθηκε ότι είναι το αποδοτικότερο με σκοπό την ενσωμάτωση του στο συστήμα.
* Τον κώδικα που αφορά την αποθήκευση, την ανάλυση και την επεξεργασία των οδηγικών δεδομένων καθώς αυτά εισέρχονται στο σύστημα.
* Τον κώδικα που αφορά την ανάπτυξη του REST API και του frontend με σκοπό την ανάκτηση και την οπτικόποιηση των δεδομένων.
* Τον κώδικα που αφορά την αρχικοποίηση και την προσομοίωση της λειτουργίας του συστήματος.

Σε αυτό το σήμειο θα πρέπει να παρουσιαστεί ο κώδικας που βρίσκεται στον φάκελο app_ml/functionalities καθώς είναι κώδικας γενικού σκοπού και χρησιμοποιείται σε διάφορα επιμέρους σημεία. Στο αρχείο constants.py ορίζονται σταθέρες μεταβλητές που χρησιμοποιόυνται από άλλα κομμάτια κώδικα. Στο αρχείο preprocessing.py ορίζονται συναρτήσεις που αφορούν την προεπεξεργασία δεδομένων που προέρχονται από αρχεία csv. Τέλος, στο αρχείο preprocessing_mongo.py ορίζονται συναρτήσεις που αφορούν την προεπεξεργασία δεδομέων που προέρχονται από τη βάση δεδομένων MongoDB του συστήματος.

### Σύκριση και αξιολόγηση μοντέλων μηχανικής μάθησης

Στον φάκελο app_ml/models ορίζονται τα μοντέλα τα οποία εξετάστηκαν. Τα αρχεία TimeModel.py και TimelessModel.py ορίζουν δύο βασικές κλάσεις οι οποίες χρησιμοποιούνται για την κατασκευή μοντέλων που διαχειρίζονται δεδομένα χρονοσειρών η απλές εγγραφές δεδομένων, αντίστοιχα. Στα υπόλοιπα αρχεία ορίζονται οι κλάσεις των μοντέλων που εξετάστηκαν. Η παραμετροποίηση κάθε μόντελου έχει οριστεί εκ των προτέρων με τις βέλτιστες τίμες (για το εκάστοτε μοντέλο), οι οποίες βρέθηκαν με χρήση του αλγορίθμου GridSearchCV.

Στον φάκελο app_ml/train βρίσκεται τα αρχείο train_all_models.py και generate_data.py. Με την εκτέλεση του αρχείου generate_data.py πραγματοποιείται μια προεπεξεργασία των αρχείων του συνόλου δεδομένων [Traffic, Driving Style and Road Surface Condition](https://www.kaggle.com/gloseto/traffic-driving-style-road-surface-condition), έτσι ώστε τα δεδομένα να έρθουν σε μορφή που εξυπηρετεί την εκπαίδευση των μοντέλων. Τα νέα αρχεία csv που προκύπτουν αποθηκεύονται στον φάκελο app_ml/train/generated_data. Με την εκτέλεση του αρχείου train_all_models.py πραγματοποιείται η εκπαίδευση όλων των μοντέλων που ορίζονται στον φάκελο app_ml/models με σύνολο δεδομένων τα δεδομένα που βρίσκονται στον φάκελο app_ml/train/generated_data, ενώ παράλληλα τυπώνονται και τα αποτελέσματα που επιτεύχθηκαν από το κάθε μοντέλο. Προτείνεται η ανακατεύθυνση της εξόδου του προγράμματος train_all_models.py σε κάποιο αρχείο και όχι στην κονσόλα καθώς τα αποτελέσματα και εκπαίδευση των μοντέλων οδηγούν σε εκτύπωση μεγάλου όγκου χαρακτήρων. 

### Εκπαίδευση του μοντέλου LSTM

Από τη σύγκριση και την αξιολόγιση των μοντέλων μηχανικής μάθησης προέκυψε ότι το αποδοτικότερο μοντέλο ήταν το νευρωνικό δίκτυο LSTM. Για την εκπαίδευση του LSTM χρησιμοποιείται το αρχείο app_ml/train/train_rnn.py μέσω του οποίου ορίζεται το νευρωνικό δίκτυο LSTM, εκπαιδεύεται με σύνολο δεδομένων όλα τα δεδομένα που βρίσκονται στη βάση MongoDB του συστήματος και τελικά αποθηκεύεται στον φάκελο RNN_MODEL έτσι ώστε να μπορεί να χρησιμοποιηθεί από τον αναλυτή δεδομένων του συστήματος.

### Ανάλυση, επεξεργασία και αποθήκευση δεδομένων



### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```JS
   const API_KEY = 'ENTER YOUR API';
   ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
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
