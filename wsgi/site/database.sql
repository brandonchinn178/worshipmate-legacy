-- MySQL dump 10.13  Distrib 5.6.19, for osx10.9 (x86_64)
--
-- Host: localhost    Database: worshipdb
-- ------------------------------------------------------
-- Server version	5.6.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add song',7,'add_song'),(20,'Can change song',7,'change_song'),(21,'Can delete song',7,'delete_song');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$FGM0iIh1lI2X$sTjWwAiI2o2t7pf+6lhDNrIB2YZilbAIRWnsf6QUtLo=','2014-07-25 19:32:12',1,'brandon','Brandon','Chinn','brandonchinn178@gmail.com',1,1,'2014-07-25 19:05:51');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `database_song`
--

DROP TABLE IF EXISTS `database_song`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `database_song` (
  `title` varchar(50) NOT NULL,
  `artist` varchar(50) NOT NULL,
  `themes` varchar(500) NOT NULL,
  `speed` varchar(10) NOT NULL,
  PRIMARY KEY (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `database_song`
--

LOCK TABLES `database_song` WRITE;
/*!40000 ALTER TABLE `database_song` DISABLE KEYS */;
INSERT INTO `database_song` VALUES ('10,000 Reasons (Bless the Lord)','Matt Redman','Worship, Praise, Devotion','F'),('Abba Father','Shaun Groves','God\'s Devotion, Devotion, God\'s Love, Love, Affirmation, Comfort, Simple','S'),('Above All','Michael W. Smith','God\'s Sovereignty, Good Friday, Easter','S'),('All For You','Phil Wickham','Devotion, Affirmation, Simple','S'),('All I Am','Phil Wickham','Devotion, Surrender, Affirmation','FS'),('All I Want Is You','Phil Wickham','Devotion, Dependence, Affirmation','S'),('All of Creation','MercyMe','Creation, Praise, Grace, Resurrection, Easter','F'),('All Things Are Possible','Hillsong','God\'s Power, Praise, Devotion','F'),('All Who Are Thirsty','Kutless','Dependence, Comfort, God\'s Power, God\'s Presence','S'),('Always Forever','Phil Wickham','Dependence, God\'s Devotion, Devotion','S'),('Amazing Grace (My Chains Are Gone)','Chris Tomlin','Grace, Sin, Humility, Mercy, Simple, Hymn','S'),('Amazing Love (You Are My King)','Newsboys','Forgiveness, Love, Affirmation, Easter','S'),('Ancient of Days','Ron Kenoly','Praise, Worship','F'),('Arms of Love','Brian Doerksen','Love, Devotion, Adoration, Comfort','S'),('As the Deer','Martin Nystrom','Devotion, Worship, Comfort','S'),('Be Glorified','Chris Tomlin','Passion, Devotion, Discipleship, Worship','F'),('Be Thou My Vision','Ascend the Hill','Guidance, Devotion, Affirmation, Simple, Hymn','S'),('Beautiful One','Tim Hughes','Praise, God\'s Power','F'),('Beautiful Things','Gungor','Praise, Renewal, Redemption, Encouragement, Comfort, God\'s Power','S'),('Beautiful, Beautiful','Francesca Battistelli','Praise, Grace, Creation','S'),('Before the Throne of God Above','Shane & Shane','Redemption, Devotion, Jesus\' Sacrifice, Good Friday, Love, Simple, Hymn','S'),('Beloved','Tenth Avenue North','God\'s Love, God\'s Devotion, Marriage, Everlasting, Devotion','S'),('Better Is One Day','Hillsong','Heaven, Future, God\'s Presence, Devotion','S'),('Blessed Assurance','Traditional','Worship, Affirmation, Redemption, Discipleship, Devotion, Simple, Hymn','F'),('Blessed Be Your Name','Tree63','Praise, Devotion, Blessings, Worship','F'),('Blessings','Laura Story','Suffering, Blessings, Comfort, Prayer','S'),('Bread of Life','Traditional','Passion, Jesus\' Sacrifice, Dependence, Hymn','FS'),('Break Every Chain','Jesus Culture','Redemption, Freedom, Jesus\' Sacrifice, Strength, Comfort, Power, Simple','S'),('Breathe','Michael W. Smith','Devotion, Dependence, Affirmation','S'),('Broken Hallelujah','The Afters','Worship, Offering, Comfort, Encouragement','FS'),('Build Your Fire','Douglas Eltzroth','Passion, Devotion, Discipleship','S'),('By Your Side (Hillsong)','Hillsong','Devotion, Discipleship','F'),('By Your Side (Tenth)','Tenth Avenue North','God\'s Presence, Love, Grace, Hope, Comfort','S'),('Came to My Rescue','Hillsong','Salvation, Devotion, Personal, Worship, Passion, Guidance, Praise','S'),('Cannons','Phil Wickham','Praise, Affirmation, Creation, Devotion','S'),('Change My Heart Oh God','Vineyard','Renewal, Devotion, Love','S'),('Christ in Me','Gary Garcia','Devotion, Affirmation, Creation','S'),('Christ is Enough','Hillsong','Dependence, Devotion, Comfort, Discipleship','S'),('City on Our Knees','TobyMac','Passion, Grace, Love, Hope','S'),('Closer','Bethel Music','Personal, Devotion, Love, Guidance','S'),('Come and Fill Me Up','Brian Doerksen','Passion, Devotion, Mercy','F'),('Come Now Is the Time to Worship','Brian Doerksen','Worship, Devotion, Acceptance, World','F'),('Come Thou Fount','Traditional','Worship, God\'s Presence, Blessings, Jesus\' Sacrifice, Discipleship, Redemption, Simple, Hymn','S'),('Consuming Fire','Hillsong','Passion, God\'s Presence, Renewal, Discipleship, Guidance','S'),('Cornerstone','Hillsong','Strength, Dependence, God\'s Promise, Comfort','S'),('Create In Me A Clean Heart','Keith Green','Renewal, God\'s Presence, Dependence, Discipleship, Simple','S'),('Crown Him With Many Crowns','Traditional','Praise, King, Affirmation, Simple, Hymn','F'),('Dancing Generation','Matt Redman','Worship, Praise, Mercy, Glory','F'),('Dead Man (Carry Me)','Jars of Clay','Renewal, Dependence','F'),('Deep Cries Out','William Matthews','Passion, Worship, Dependence, Faith, Trust, Discipleship','F'),('Desert Song','Hillsong','Worship, Emptiness, Strength, Comfort, Affirmation','S'),('Did You Feel the Mountains Tremble','Hillsong','Worship, God\'s Power, Passion, Future, World','F'),('Do You Hear What I Hear','Third Day','Christmas','S'),('Draw Me Close','Michael W. Smith','God\'s Presence, Devotion, Affirmation, Comfort, Guidance','S'),('Enough','Chris Tomlin','Devotion, Dependence, Affirmation','FS'),('Eternity','Brian Doerksen','Devotion, Future, Worship, God\'s Presence, Affirmation','S'),('Everlasting God','Chris Tomlin','Everlasting, Affirmation, Comfort, Praise','F'),('Every Move I Make','Hillsong','Devotion, Discipleship, Love','F'),('Everyday','Hillsong','Devotion, Affirmation, Guidance','F'),('Faithful One','Brian Doerksen','God\'s Devotion, Everlasting, Dependence, Comfort, Love, Hope','S'),('Famous One','Chris Tomlin','Praise, Devotion, Worship, Creation','FS'),('Father I Adore You','Matt Brouwer','Adoration, Devotion, Discipleship, Simple','FS'),('Fixin\' My Eyes on You','Jana Alayra','Discipleship, Guidance, Devotion','F'),('Flood','Jars of Clay','Dependence, Weakness, Control','F'),('Forever','Chris Tomlin','Everlasting, Praise, God\'s Presence, God\'s Sovereignty','F'),('Forever Reign','Hillsong','Praise, God\'s Sovereignty, Love, Dependence, Simple','FS'),('From the Inside Out','Hillsong','Mercy, Humility, Everlasting, Guidance, Affirmation, Devotion','S'),('Get Back Up','TobyMac','Revival, Forgiveness, Love, Comfort','F'),('Give Me Jesus','Jeremy Camp','Devotion, Surrender, Dependence','S'),('Give Me Your Eyes','Brandon Heath','Love, Outreach, Service','S'),('Give Thanks','Maranatha! Singers','Thankfulness, Faithfulness, Thanksgiving','FS'),('Give Us Clean Hands','Chris Tomlin','Devotion, Discipleship, Worship, Humility, Surrender','S'),('Glory to the Lamb','Bill Batstone','Praise, Glory, Jesus\' Sacrifice','F'),('Go Tell It on the Mountain','Tenth Avenue North','Christmas, Outreach, Testimony','F'),('God is Able','Hillsong','God\'s Power, Strength, God\'s Devotion, God\'s Presence','S'),('God of This City','Chris Tomlin','God\'s Sovereignty, Future, Hope','S'),('God of Wonders','Third Day','Creation, God\'s Power, God\'s Sovereignty, Praise','S'),('God, I Look to You','Jenn Johnson','Guidance, Affirmation, Discipleship, Love, Everlasting, Devotion','S'),('Great Is Thy Faithfulness','Traditional','Faithfulness, God\'s Devotion, God\'s Love, God\'s Presence, Comfort, Hymn, Simple','S'),('Hallelujah, Your Love Is Amazing','Brian Doerksen','Praise, Worship, Love, Joy','F'),('He Is God','Jana Alayra','Affirmation, God\'s Sovereignty, God\'s Power','F'),('He Knows My Name','Maranatha! Singers','Personal, God\'s Devotion, God\'s Sovereignty, Comfort, Omnipotence','S'),('Healing Begins','Tenth Avenue North','Healing, Renewal, Comfort, Redemption','FS'),('Heart of Worship','Matt Redman','Worship, Devotion, Guidance, Refocus','S'),('Heaven Fall Down','Phil Wickham','God\'s Presence, Dependence, God\'s Glory','F'),('Here I Am to Worship','Michael W. Smith','Worship, Devotion, Praise','S'),('High Above','Phil Wickham','God\'s Sovereignty, Creation, Praise, Affirmation','S'),('Hold My Heart','Tenth Avenue North','Loneliness, Dependence, Comfort','S'),('Hold You High','By the Tree','Praise, Discipleship, Devotion, Witness, Testimony','F'),('Holy and Anointed One','Brian Doerksen','Praise, Devotion, Dependence, Guidance, Simple','S'),('Holy Is the Lord','Chris Tomlin','Worship, Praise, Holiness, World','F'),('Hosanna','Hillsong','Praise, Forgiveness, Revival, Passion, Future, Easter','S'),('How Deep the Father\'s Love for Us','Stuart Townend','Love, God\'s Devotion, Redemption, Sin, Good Friday, Easter','S'),('How Great Is Our God','Chris Tomlin','Praise, God\'s Glory','S'),('How He Loves','David Crowder','Love, God\'s Devotion, Grace, Praise','S'),('Hungry','Kathryn Scott','Humility, Devotion, Comfort','S'),('I Am Free','Newsboys','God\'s Power, Passion, Redemption, Devotion, Discipleship, Freedom','F'),('I Can Only Imagine','MercyMe','Future, Heaven, God\'s Glory, Worship, God\'s Presence, Devotion','FS'),('I Could Sing of Your Love Forever','Sonicflood','Devotion, Praise, Worship, Love','FS'),('I Feel His Love','Laura Hackett','God\'s Love, Strength, Comfort, Hurt','FS'),('I Give Thanks','Andy Park','Thanksgiving, God\'s Devotion, Worship, Praise, Mercy, Life, God\'s Power','F'),('I Give You My Heart','Hillsong','Devotion, Worship, Affirmation','S'),('I Lift My Eyes Up','Brian Doerksen','Guidance, God\'s Power, God\'s Presence, Praise, Creation, Simple','S'),('I Love You Lord','Scott Riggan','Devotion, Praise, Worship, Love, Simple','FS'),('I Stand in Awe','Jeff Johnson','God\'s Glory, God\'s Sovereignty, God\'s Presence, Worship, Praise, Simple','S'),('I Wanna Do Right','Jana Alayra','Discipleship, Devotion, Guidance, Worship','F'),('I Will Follow','Chris Tomlin','Discipleship, Devotion, Outreach, Praise','FS'),('I Will Rise','Chris Tomlin','Discipleship, Humility, Affirmation','S'),('In Christ Alone','Stuart Townend','Love, Devotion, Praise, Dependence, Comfort, Freedom, Good Friday, Easter, Simple, Hymn','S'),('In the Calm','Point of Grace','Quietness, Meditation, Calm, Peace','S'),('In the Light','DC Talk','Light, Humility, Dependence','F'),('In the Secret','Andy Park','Calm, Quietness, Passion, Devotion','FS'),('Indescribable','Chris Tomlin','Praise, God\'s Sovereignty, Creation','S'),('Invitacion Fountain','Vineyard','Guidance, Invitation, Devotion, Comfort, Rest','S'),('It Is Well (With My Soul)','Traditional','Peace, Comfort, Praise, Worship, Victory','FS'),('Jesus Draw Me Close','Rick Founds','God\'s Presence, Devotion, Worship, Simple','S'),('Jesus Is A Friend','David Graham','Personal, Icebreaker, Simple','F'),('Jesus Lord of Heaven','Phil Wickham','God\'s Love, Love, Jesus\' Sacrifice, Grace, God\'s Promise, Mercy, Redemption','FS'),('Jesus Lover of My Soul','Hillsong','Devotion, Love, Dependence, Personal, Worship, Simple','S'),('Jesus Loves Me','Traditional','Love, Comfort, God\'s Devotion, Hymn, Simple','S'),('Jesus Loves Me, Alleluia','Yohann Anderson','Comfort, Love, Redemption, Renewal, Grace, Simple','S'),('Jesus Messiah','Chris Tomlin','Praise, Jesus\' Sacrifice, Good Friday, Love, Redemption','FS'),('Jesus Paid It All','Kristian Stanfill','Jesus\' Sacrifice, Redemption, Renewal, Strength, Dependence, God\'s Power','S'),('Jesus Reigns','Jana Alayra','Worship, God\'s Sovereignty, Simple','F'),('Jesus Thank You','Pat Sczebel','Redemption, Jesus\' Sacrifice, Good Friday, Thanksgiving, Devotion','S'),('Joyful, Joyful We Adore Thee','Traditional','Praise, Worship, Love, Creation, God\'s Sovereignty, Christmas','F'),('Jump Into the Light','Jana Alayra','Guidance, Devotion, Discipleship, Light, Simple','F'),('Kindness','Chris Tomlin','Devotion, God\'s Glory, Love, Mercy, Worship','S'),('Knowing You','Maranatha! Singers','Personal, Devotion, Love, Jesus\' Sacrifice, Surrender','S'),('Lead Me to the Cross','Hillsong','Dependence, Guidance, Love, Humility, Discipleship, Jesus\' Sacrifice, Good Friday','S'),('Let God Arise','Chris Tomlin','Everlasting, God\'s Sovereignty, God\'s Devotion, God\'s Power, Praise','F'),('Let Love Win','Jon Thurlow','Love, Redemption, God\'s Grace, God\'s Nature, God\'s Perspective, Affirmation','S'),('Let My Words Be Few','Matt Redman','Devotion, Love, Praise, Worship, God\'s Presence','S'),('Lifesong','Casting Crowns','Worship, Devotion, Discipleship, Surrender, Outreach','F'),('Light the Fire Again','Brian Doerksen','Passion, Dependence, Renewal, Humility','FS'),('Lord I Lift Your Name on High','Maranatha! Singers','Praise, Worship, Devotion, Affirmation, Redemption','F'),('Lord I Offer My Life to You','Hillsong','Devotion, Discipleship, Personal, Faith, Worship, Offering','S'),('Lord Most High','Ross Parsley','Creation, God\'s Sovereignty, Everlasting, Worship, Praise','S'),('Lord My Strength','Dean Krippaehne','Strength, Comfort, Guidance, Devotion, Discipleship','S'),('Lord Reign in Me','Brenton Brown','God\'s Sovereignty, Discipleship, Guidance, Creation, Devotion, Affirmation','F'),('Lord You Have My Heart','Delirious?','Devotion, Affirmation, Worship, Guidance, God\'s Glory, Discipleship','S'),('Love is Here','Tenth Avenue North','Love, Dependence, Comfort, God\'s Devotion, Rest','FS'),('Marvelous Light','Charlie Hall','Light, Discipleship, Devotion, God\'s Power, Redemption','F'),('Meet Us Here','Maranatha! Singers','God\'s Presence, Worship, Fellowship, Simple','FS'),('Meet With Me','Hillsong','God\'s Presence, Worship, Discipleship','F'),('Mighty Is Our God','Chris Rodriguez','God\'s Power, God\'s Sovereignty, Praise, Affirmation','F'),('Mighty to Save','Hillsong','God\'s Power, Humility, God\'s Glory, Mercy, Forgiveness, Devotion, Renewal, Savior','S'),('More Love, More Power','Jeff Deyo','Worship, Devotion, Passion','FS'),('My God, My King','All Sons and Daughters','Worship, Devotion, Love, Adoration, Blessings, Simple','S'),('Nails in Your Hands','Hillsong','Devotion, Love, God\'s Devotion, Discipleship, Good Friday, Easter','S'),('Never Once','Matt Redman','God\'s Presence, Dependence, Everlasting, Strength, God\'s Power, Comfort','S'),('No One Like You','David Crowder','Praise, God\'s Holiness, God\'s Presence','F'),('No Other Savior','Starfield','Praise, Holiness, God\'s Sovereignty, Everlasting, Devotion, Affirmation','S'),('None But Jesus','Hillsong','Dependence, Devotion, Worship, Trust, Disciplehsip','S'),('Not Be Shaken','David Ruis','Affirmation, Devotion, God\'s Power, Dependence, Strength','F'),('Not to Us','Chris Tomlin','Devotion, Worship, Discipleship, Praise, Creation','F'),('Nothing but the Blood of Jesus','Traditional','Jesus\' Sacrifice, Redemption, Grace, Comfort, Simple, Hymn','FS'),('Now That You\'re Near','Hillsong','God\'s Presence, Devotion, Renewal','F'),('O Lord to You','Gary Sadler','Worship, Devotion, Surrender, Searching, Discipleship','S'),('O Praise Him','David Crowder','Praise, Worship, Love, Heaven','F'),('Oceans','Hillsong','Strength, Dependence, Devotion, Rest, Guidance, Comfort','S'),('On My Cross','FFH','God\'s Devotion, Jesus\' Sacrifice, Redemption, God\'s Love, Grace, Good Friday','S'),('Once Again','Matt Redman','Devotion, Jesus\' Sacrifice, Dependence, Thankfulness, Broken, Comfort, Humility, Renewal, Good Friday','S'),('One Thing Remains','Jesus Culture','Love, Everlasting, God\'s Devotion, Comfort, God\'s Power','S'),('One Way','Hillsong','Devotion, Discipleship, God\'s Presence, Faith, Affirmation','F'),('Only You','Breakaway Ministries','God\'s Power, God\'s Sovereignty, Personal, Comfort, Creation','S'),('Open the Eyes of My Heart','Paul Baloche','Vision, Glory, Worship, Guidance','FS'),('Our God','Chris Tomlin','God\'s Power, God\'s Holiness, Praise, Comfort, Affirmation','S'),('Our Love Is Loud','David Crowder','Worship, Love, Praise, Affirmation, Fellowship','F'),('Power of Your Love','Hillsong','Love, God\'s Power, Renewal','FS'),('Precious Cornerstone','Andy Park','God\'s Power, Dependence, Love, Affirmation','F'),('Psalm 9','Vineyard','Worship, Praise, Devotion, Testimony, Witness','S'),('Reaching For You','Lincoln Brewster','Devotion, Worship, Dependence, Affirmation','F'),('Refiner\'s Fire','Brian Doerksen','Holiness, Devotion, Preparation, Purify, Renewal, Redemption','S'),('Reign in Us','Starfield','Devotion, Guidance, Renewal, God\'s Presence, Discipleship','S'),('Seek Ye First','Traditional','Searching, Dependence, Invitation, Simple, Hymn','S'),('Send Me Out','Fee','Outreach, Discipleship, Testimony, Witness','F'),('Set a Fire','Jesus Culture','Passion, Devotion, Presence, God\'s Love, Simple','S'),('Shine Jesus Shine','Hillsong','Passion, God\'s Glory, Light, God\'s Presence','F'),('Shout to the Lord','Hillsong','Worship, Praise, Devotion, Comfort, Strength','S'),('Show Us Christ','Sovereign Grace Music','Message, Listening, God\'s Presence, God\'s Glory, Preparation, Devotion','S'),('Sing A Joyful Song','Maranatha! Singers','Worship, Praise, Devotion, Joy, Simple','F'),('Sing to the King','Passion','Worship, Praise, Devotion, Salvation, Future','F'),('So Good to Me (Evans)','Darrell Evans','Praise, Mercy, Grace, Worship','F'),('So Good to Me (Matthews)','William Matthews','Praise, God\'s Devotion, Worship, Joy, Strength, Comfort, Guidance','F'),('Solution','Hillsong','Discipleship, Guidance, Affirmation, Devotion','F'),('Song of Hope','Robbie Seay Band','Worship, Hope, Presence, Praise, Renewal','F'),('Speak, O Lord','Stuart Townend','Listening, Discipleship, Devotion, Living, Outreach, Conviction, Affirmation','S'),('Stand Up, Stand Up For Jesus','Traditional','Strength, Devotion, Victory, Glory, Future, Simple, Hymn','F'),('Standing on the Promises','Traditional','God\'s Promise, Faith, Strength, Praise, Worship, Simple, Hymn','F'),('Step By Step-Forever We Will Sing','Michael W. Smith','Devotion, Worship, Discipleship, Guidance, Praise','F'),('Still','Hillsong','God\'s Sovereignty, Comfort, Dependence, Quietness, Creation','S'),('Stir In Me','Hillsong','Passion, Worship, Renewal','FS'),('Strong Tower','Kutless','Strength, Dependence, Comfort, God\'s Power','F'),('Stronger','Hillsong','God\'s Power, Redemption, Victory, God\'s Sovereignty, Worship','S'),('Surrender','Lincoln Brewster','Devotion, Discipleship, Surrender','S'),('Sweetly Broken','Jeremy Riddle','Humility, Devotion, Grace, Renewal, Jesus\' Sacrifice, Good Friday','FS'),('Take It All','Hillsong','Devotion, Worship, Affirmation, Discipleship, Passion','F'),('Take My Hand','The Kry','Guidance, Comfort, Future, Faith, Devotion','S'),('Take My Heart','Something Like Silas','Devotion, Worship, Discipleship, Humility, Simple','S'),('Take My Life (Tomlin)','Chris Tomlin','Devotion, Discipleship, Guidance, Renewal, Simple, Hymn','S'),('Take My Life (Underwood)','Scott Underwood','Renewal, Devotion, Humility, Simple','S'),('Take Your Place','Jon Thurlow','Devotion, Longing, Discipleship, Center, Simple','S'),('The Happy Song','Paul Baloche','Worship, Savior, Renewal, Affirmation, Love, Testimony','F'),('The Motions','Matthew West','Deception, Passion, Guidance, Devotion','S'),('The Power of the Cross','Stuart Townend','Jesus\' Sacrifice, Good Friday, Redemption, Simple','S'),('The Time Has Come','Hillsong','Worship, Devotion, Conviction, Affirmation, Dependence','F'),('There Is Joy in the Lord','Maranatha! Singers','Joy, Love, Praise, God\'s Power, Worship, God\'s Glory','F'),('There Is None Like You','Don Moen','Comfort, God\'s Holiness, Personal, Healing, Simple','S'),('They\'ll Know We Are Christians by Our Love','Peter Scholtes','Love, Witness, Outreach, Unity, World','FS'),('This Is the Day','Phil Wickham','Life, Grace, Salvation, Redemption','F'),('This Little Light of Mine','Traditional','Light, Witness, Endurance, Simple','F'),('This Love Will Last Forever','Phil Wickham','Love, Worship, Humility, Devotion','F'),('Today Is the Day','Lincoln Brewster','Worship, Future, God\'s Promise, Dependence, Praise','F'),('Trading My Sorrows','Darrell Evans','Affirmation, Strength, Joy, Comfort','F'),('Treasure Quest','Jana Alayra','Discipleship, Devotion, Searching, Endurance','F'),('True Love','Phil Wickham','Redemption, Good Friday, Easter, Love, God\'s Devotion','F'),('Unashamed','Starfield','Humility, Redemption, Personal, Comfort, Grace','S'),('Unchanging','Chris Tomlin','Everlasting, Worship, God\'s Promise','F'),('Undignified','David Crowder','Worship, Passion, Simple','F'),('Unfailing Love','Chris Tomlin','Devotion, Personal, Praise, God\'s Sovereignty, Love','S'),('Until the Whole World Hears','Casting Crowns','Outreach, Worship, Discipleship, World','F'),('Victory in Jesus','Traditional','Devotion, Love, Praise, God\'s Power, Glory, Easter, Simple, Hymn','F'),('Voice of Truth','Casting Crowns','Truth, Comfort, Listening, Devotion, Faith, Trust','FS'),('We Are Hungry','Jesus Culture','Dependence, Devotion, Worship, Presence','FS'),('We Fall Down','Chris Tomlin','Humility, Holiness, Mercy, Love, Surrender','S'),('We Want to See Jesus Lifted High','Doug Horley','Praise, Witness, Devotion, Simple','F'),('When I Think About the Lord','Shane & Shane','Praise, Dependence, Affirmation, God\'s Devotion','FS'),('Who Am I','Casting Crowns','Humility, Personal, Devotion, Affirmation, Guidance, Comfort','S'),('Wholly Yours','David Crowder','Discipleship, Devotion, Praise, Humility, Grace','S'),('Whom Shall I Fear','Chris Tomlin','God\'s Power, God\'s Sovereignty, Everlasting, Comfort, God\'s Presence, Personal','S'),('With Every Breath','Sixpence','Worship, Praise, Creation, Comfort, Strength','S'),('Word of God Speak','MercyMe','Listening, God\'s Presence, Quietness, Calm, Devotion','S'),('Worthy is the Lamb','Hillsong','God\'s Glory, Jesus\' Sacrifice, Redemption','S'),('Worthy of It All','David Brymer','Worship, Glory, Adoration, Simple','S'),('You Are Good','Lincoln Brewster','Praise, Worship, Mercy, World','F'),('You Are Holy (Prince of Peace)','Michael W. Smith','Praise, Devotion, Worship','F'),('You Are My All in All','Nicole Nordeman','Praise, Devotion, Dependence, Comfort, Discipleship','S'),('You Are My Hiding Place','Selah','Comfort, Trust, Devotion, Strength, Simple','S'),('You Are My Treasure','Chris Tomlin','Devotion, Discipleship, Grace, Love','F'),('You Are My World','Hillsong','Devotion, Praise, Worship, Discipleship','FS'),('You Are the Vine','Vineyard','Dependence, Growth, Witness, Outreach, Simple','S'),('You Are Worthy of My Praise','David Ruis','Worship, Devotion, Praise, Affirmation','F'),('You Shine','Brian Doerksen','Praise, God\'s Power, Love, Guidance, Devotion, Discipleship, God\'s Holiness','F'),('You\'re Beautiful','Phil Wickham','Creation, Praise, Beauty, Future','S'),('You\'re Wonderful','Phil Wickham','Creation, Praise, Worship, God\'s Power','F'),('You\'re Worthy of My Praise','Jeremy Camp','Worship, Devotion, Praise, Affirmation','F'),('Your Beloved','Vineyard','God\'s Devotion, God\'s Love, Creation, God\'s Sovereignty','S'),('Your Grace Is Enough','Chris Tomlin','Grace, God\'s Devotion, God\'s Promise','F'),('Your Love Never Fails','Jesus Culture','Love, Everlasting, God\'s Devotion, Comfort, Personal','FS'),('Your Love Oh Lord','Third Day','Love, God\'s Devotion, Creation, Worship, Strength, Comfort','FS'),('Your Name Is Holy','Vineyard','Praise, Strength, God\'s Sovereignty, Simple','F');
/*!40000 ALTER TABLE `database_song` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-07-25 19:07:11',1,4,'1','brandon',2,'Changed first_name and last_name.'),(2,'2014-07-29 21:33:15',1,7,'329','Go Tell It on the Mountain | Tenth Avenue North',2,'Changed title.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'song','database','song');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('5p6vaniws3xj0re4et77j58bjrje2zqn','ZGI4YzBmODQ2YzJmM2QyNmYyNjRmMDFlMmQ4NjZhYmE1YjBmMzJhODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-08-08 19:32:12');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-08-02 16:17:13
