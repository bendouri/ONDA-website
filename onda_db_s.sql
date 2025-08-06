-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 05, 2025 at 09:43 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `onda_db_s`
--

-- --------------------------------------------------------

--
-- Table structure for table `activity_log`
--

CREATE TABLE `activity_log` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `action` varchar(50) NOT NULL,
  `entity_type` varchar(50) NOT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `entity_name` varchar(200) DEFAULT NULL,
  `description` text NOT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `activity_log`
--

INSERT INTO `activity_log` (`id`, `user_id`, `action`, `entity_type`, `entity_id`, `entity_name`, `description`, `created_at`) VALUES
(1, 4, 'CREATE', 'JobOffer', 1, 'aaaa', 'Offre d\'emploi créée: aaaa', '2025-08-05 02:23:49'),
(2, 4, 'UPDATE', 'JobApplication', 3, 'Test Candidat', 'Statut candidature modifié: accepted', '2025-08-05 02:29:42'),
(3, 4, 'CREATE', 'JobApplication', 4, 'achraf abderrazik', 'Nouvelle candidature pour aaaa', '2025-08-05 02:44:34'),
(4, 4, 'UPDATE', 'JobApplication', 4, 'achraf abderrazik', 'Statut candidature modifié: accepted', '2025-08-05 02:53:11'),
(5, 4, 'CREATE', 'JobApplication', 5, 'achraf abderrazik', 'Nouvelle candidature pour aaaa', '2025-08-05 02:53:49'),
(6, 4, 'CREATE', 'CallForTenders', 1, 'zerzer', 'Appel d\'offre créé: zerzer', '2025-08-05 03:05:34'),
(7, 4, 'login', 'admin', 4, 'admin', 'Connexion admin réussie pour admin', '2025-08-05 15:52:33'),
(8, 4, 'UPDATE', 'User', 5, 'userr', 'Utilisateur modifié: userr', '2025-08-05 15:52:56'),
(9, 4, 'UPDATE', 'User', 5, 'user', 'Utilisateur modifié: user', '2025-08-05 15:53:04'),
(10, 4, 'UPDATE', 'JobApplication', 7, 'achraf abderrazik', 'Statut candidature modifié: accepted', '2025-08-05 16:13:24'),
(11, 4, 'DELETE', 'Restaurant', 1, 'La Sqala', 'Restaurant supprimé: La Sqala', '2025-08-05 17:05:49'),
(12, 4, 'DELETE', 'Restaurant', 2, 'Rick\'s Café', 'Restaurant supprimé: Rick\'s Café', '2025-08-05 17:05:51'),
(13, 4, 'DELETE', 'Restaurant', 3, 'Nomad', 'Restaurant supprimé: Nomad', '2025-08-05 17:05:53'),
(14, 4, 'DELETE', 'Restaurant', 4, 'Le Jardin', 'Restaurant supprimé: Le Jardin', '2025-08-05 17:05:54'),
(15, 4, 'CREATE', 'Restaurant', 5, 'La Table du Marché', 'Nouveau restaurant ajouté: La Table du Marché', '2025-08-05 17:08:23'),
(16, 4, 'CREATE', 'Restaurant', 6, 'Matsuri', 'Nouveau restaurant ajouté: Matsuri', '2025-08-05 17:08:43'),
(17, 4, 'CREATE', 'Restaurant', 7, 'La Table du Marché', 'Nouveau restaurant ajouté: La Table du Marché', '2025-08-05 17:09:16'),
(18, 4, 'CREATE', 'Restaurant', 8, 'Matsuri Sushi', 'Nouveau restaurant ajouté: Matsuri Sushi', '2025-08-05 17:09:36'),
(19, 4, 'CREATE', 'Restaurant', 9, 'Matsuri Sushi', 'Nouveau restaurant ajouté: Matsuri Sushi', '2025-08-05 17:09:56'),
(20, 4, 'CREATE', 'Restaurant', 10, 'Dar El Medina', 'Nouveau restaurant ajouté: Dar El Medina', '2025-08-05 17:10:23'),
(21, 4, 'CREATE', 'Transport', 1, 'Grand Taxi – CMN', 'Nouveau transport ajouté: Grand Taxi – CMN', '2025-08-05 17:12:30'),
(22, 4, 'CREATE', 'Transport', 2, 'Navette AeroExpress', 'Nouveau transport ajouté: Navette AeroExpress', '2025-08-05 17:12:44'),
(23, 4, 'CREATE', 'Transport', 3, 'ONCF Aéroport ↔ Casa Voyageurs', 'Nouveau transport ajouté: ONCF Aéroport ↔ Casa Voyageurs', '2025-08-05 17:13:01'),
(24, 4, 'CREATE', 'Transport', 4, 'Bus Réseau Alsa Rabat', 'Nouveau transport ajouté: Bus Réseau Alsa Rabat', '2025-08-05 17:13:15'),
(25, 4, 'CREATE', 'Shopping', 1, 'Morocco Mall', 'Nouveau centre commercial ajouté: Morocco Mall', '2025-08-05 17:14:31'),
(26, 4, 'CREATE', 'Shopping', 2, 'Menara Mall', 'Nouveau centre commercial ajouté: Menara Mall', '2025-08-05 17:14:52'),
(27, 4, 'CREATE', 'Shopping', 3, 'Boutique Artisanat Marocain', 'Nouveau centre commercial ajouté: Boutique Artisanat Marocain', '2025-08-05 17:15:58'),
(28, 4, 'login', 'admin', 4, 'admin', 'Connexion admin réussie pour admin', '2025-08-05 17:22:01'),
(29, 4, 'login', 'admin', 4, 'admin', 'Connexion admin réussie pour admin', '2025-08-05 17:47:51'),
(30, 4, 'UPDATE', 'Contact', 1, 'sarah bendouri', 'Message de contact marqué comme lu: aaaaaaa', '2025-08-05 17:48:37'),
(31, 4, 'UPDATE', 'JobApplication', 8, 'sarah bendouri', 'Statut candidature modifié: accepted', '2025-08-05 17:49:33');

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

CREATE TABLE `airport` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `code` varchar(10) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `description` text DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`id`, `name`, `city`, `code`, `latitude`, `longitude`, `description`, `is_active`) VALUES
(1, 'Casablanca - Mohammed V', 'Casablanca', 'CMN', 33.367, -7.589, 'Aéroport international de Casablanca', 1),
(2, 'Marrakech - Ménara', 'Marrakech', 'RAK', 31.605, -8.036, 'Aéroport international de Marrakech', 1),
(3, 'Agadir - Al Massira', 'Agadir', 'AGA', 30.325, -9.413, 'Aéroport international de Agadir', 1),
(4, 'Fès - Saïs', 'Fès', 'FEZ', 33.927, -4.978, 'Aéroport international de Fès', 1),
(5, 'Rabat - Salé', 'Rabat', 'RBA', 34.05, -6.75, 'Aéroport international de Rabat', 1),
(6, 'Tanger - Ibn Battouta', 'Tanger', 'TNG', 35.726, -5.917, 'Aéroport international de Tanger', 1);

-- --------------------------------------------------------

--
-- Table structure for table `call_for_tenders`
--

CREATE TABLE `call_for_tenders` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `reference` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `category` varchar(100) NOT NULL,
  `budget_min` float DEFAULT NULL,
  `budget_max` float DEFAULT NULL,
  `publication_date` datetime DEFAULT NULL,
  `deadline` datetime NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `requirements` text DEFAULT NULL,
  `contact_person` varchar(100) DEFAULT NULL,
  `contact_email` varchar(120) DEFAULT NULL,
  `contact_phone` varchar(20) DEFAULT NULL,
  `document_url` varchar(200) DEFAULT NULL,
  `created_by` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `call_for_tenders`
--

INSERT INTO `call_for_tenders` (`id`, `title`, `reference`, `description`, `category`, `budget_min`, `budget_max`, `publication_date`, `deadline`, `status`, `requirements`, `contact_person`, `contact_email`, `contact_phone`, `document_url`, `created_by`, `created_at`, `updated_at`) VALUES
(2, 'Fourniture de matériel informatique', 'AO-Q3PVEX', 'Fourniture et installation de matériel informatique pour les bureaux de l\'aéroport.', 'Fournitures', 500000, 800000, '2025-08-05 17:37:08', '2025-09-04 17:37:08', 'active', 'Soumissionnaire doit être inscrit au registre du commerce et avoir une expérience d\'au moins 3 ans dans le domaine.', 'Service des Marchés Publics', 'marches@onda.ma', '+212 5XX-XXXXXX', '/static/documents/cahier_charges.pdf', 4, '2025-08-05 17:37:08', '2025-08-05 17:37:08'),
(3, 'Travaux de rénovation des terminaux', 'AO-X6KZW0', 'Rénovation complète des terminaux passagers, incluant électricité, plomberie et finitions.', 'Travaux', 2000000, 3500000, '2025-08-05 17:37:08', '2025-09-19 17:37:08', 'active', 'Soumissionnaire doit être inscrit au registre du commerce et avoir une expérience d\'au moins 3 ans dans le domaine.', 'Service des Marchés Publics', 'marches@onda.ma', '+212 5XX-XXXXXX', '/static/documents/cahier_charges.pdf', 4, '2025-08-05 17:37:08', '2025-08-05 17:37:08'),
(4, 'Services de nettoyage', 'AO-9KS9RY', 'Prestation de services de nettoyage pour les espaces communs et les bureaux.', 'Services', 300000, 500000, '2025-08-05 17:37:08', '2025-08-20 17:37:08', 'active', 'Soumissionnaire doit être inscrit au registre du commerce et avoir une expérience d\'au moins 3 ans dans le domaine.', 'Service des Marchés Publics', 'marches@onda.ma', '+212 5XX-XXXXXX', '/static/documents/cahier_charges.pdf', 4, '2025-08-05 17:37:08', '2025-08-05 17:37:08'),
(5, 'Étude de faisabilité pour extension de piste', 'AO-H7WD7S', 'Réalisation d\'une étude de faisabilité pour l\'extension de la piste d\'atterrissage.', 'Études', 800000, 1200000, '2025-08-05 17:37:08', '2025-10-04 17:37:08', 'active', 'Soumissionnaire doit être inscrit au registre du commerce et avoir une expérience d\'au moins 3 ans dans le domaine.', 'Service des Marchés Publics', 'marches@onda.ma', '+212 5XX-XXXXXX', '/static/documents/cahier_charges.pdf', 4, '2025-08-05 17:37:08', '2025-08-05 17:37:08'),
(6, 'Maintenance des systèmes de climatisation', 'AO-4KX8DC', 'Contrat de maintenance annuelle pour les systèmes de climatisation des terminaux.', 'Maintenance', 400000, 600000, '2025-08-05 17:37:08', '2025-08-25 17:37:08', 'active', 'Soumissionnaire doit être inscrit au registre du commerce et avoir une expérience d\'au moins 3 ans dans le domaine.', 'Service des Marchés Publics', 'marches@onda.ma', '+212 5XX-XXXXXX', '/static/documents/cahier_charges.pdf', 4, '2025-08-05 17:37:08', '2025-08-05 17:37:08');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(120) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `message` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `is_read` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `name`, `email`, `subject`, `message`, `created_at`, `is_read`) VALUES
(1, 'sarah bendouri', 'sarah.bendouri@gmail.com', 'aaaaaaa', 'aaaaaaaaaaaasadadaddada', '2025-08-05 17:47:38', 1);

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `id` int(11) NOT NULL,
  `flight_number` varchar(10) NOT NULL,
  `airline` varchar(100) NOT NULL,
  `airport_id` int(11) NOT NULL,
  `destination` varchar(100) NOT NULL,
  `flight_type` varchar(20) NOT NULL,
  `scheduled_time` datetime NOT NULL,
  `actual_time` datetime DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `gate` varchar(10) DEFAULT NULL,
  `terminal` varchar(10) DEFAULT NULL,
  `aircraft_type` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `flight`
--

INSERT INTO `flight` (`id`, `flight_number`, `airline`, `airport_id`, `destination`, `flight_type`, `scheduled_time`, `actual_time`, `status`, `gate`, `terminal`, `aircraft_type`, `created_at`) VALUES
(1, 'AT456', 'Lufthansa', 4, 'Istanbul (IST)', 'departure', '2025-08-04 08:00:00', '2025-08-04 07:52:00', 'On Time', 'B18', '3', 'Boeing 787 Dreamliner', '2025-08-05 17:32:17'),
(2, 'AT813', 'Air France', 1, 'Paris (CDG)', 'arrival', '2025-08-04 18:00:00', '2025-08-04 17:51:00', 'On Time', 'B28', '1', 'Airbus A320', '2025-08-05 17:32:17'),
(3, 'AT757', 'Royal Air Maroc', 3, 'Londres (LHR)', 'departure', '2025-08-04 08:30:00', '2025-08-04 08:25:00', 'Delayed', 'C13', '1', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(4, 'AT370', 'Iberia', 3, 'Dubai (DXB)', 'arrival', '2025-08-04 19:45:00', '2025-08-04 20:05:00', 'Scheduled', 'B25', '1', 'Airbus A320', '2025-08-05 17:32:17'),
(5, 'AT646', 'Air France', 1, 'Londres (LHR)', 'departure', '2025-08-04 14:45:00', '2025-08-04 15:00:00', 'Delayed', 'C14', '2', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(6, 'AT379', 'Emirates', 4, 'Dakar (DSS)', 'arrival', '2025-08-04 10:30:00', '2025-08-04 11:09:00', 'Scheduled', 'B10', '1', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(7, 'AT227', 'Royal Air Maroc', 3, 'Paris (CDG)', 'departure', '2025-08-04 13:15:00', '2025-08-04 13:58:00', 'On Time', 'B6', '1', 'Airbus A350', '2025-08-05 17:32:17'),
(8, 'AT780', 'British Airways', 1, 'Casablanca (CMN)', 'arrival', '2025-08-04 06:45:00', '2025-08-04 07:26:00', 'On Time', 'C8', '1', 'Boeing 737-800', '2025-08-05 17:32:17'),
(9, 'AT211', 'Royal Air Maroc', 1, 'Londres (LHR)', 'departure', '2025-08-04 20:00:00', '2025-08-04 20:42:00', 'On Time', 'A23', '3', 'Boeing 787 Dreamliner', '2025-08-05 17:32:17'),
(10, 'AT472', 'Emirates', 1, 'Madrid (MAD)', 'arrival', '2025-08-04 21:45:00', '2025-08-04 22:29:00', 'On Time', 'B8', '3', 'Boeing 787 Dreamliner', '2025-08-05 17:32:17'),
(11, 'AT592', 'Emirates', 6, 'Istanbul (IST)', 'departure', '2025-08-05 07:00:00', '2025-08-05 06:54:00', 'On Time', 'C15', '3', 'Boeing 787 Dreamliner', '2025-08-05 17:32:17'),
(12, 'AT614', 'British Airways', 5, 'Paris (CDG)', 'arrival', '2025-08-05 20:15:00', '2025-08-05 20:54:00', 'On Time', 'A22', '3', 'Boeing 737-800', '2025-08-05 17:32:17'),
(13, 'AT363', 'Emirates', 2, 'Dakar (DSS)', 'departure', '2025-08-05 21:00:00', '2025-08-05 21:12:00', 'Arrived', 'A26', '1', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(14, 'AT396', 'Lufthansa', 6, 'Casablanca (CMN)', 'arrival', '2025-08-05 10:15:00', '2025-08-05 10:39:00', 'Departed', 'C13', '2', 'Airbus A350', '2025-08-05 17:32:17'),
(15, 'AT790', 'Qatar Airways', 1, 'New York (JFK)', 'departure', '2025-08-05 15:00:00', '2025-08-05 15:32:00', 'On Time', 'B19', '2', 'Boeing 737-800', '2025-08-05 17:32:17'),
(16, 'AT719', 'Qatar Airways', 5, 'Dakar (DSS)', 'arrival', '2025-08-05 15:30:00', '2025-08-05 15:47:00', 'On Time', 'B22', '1', 'Airbus A350', '2025-08-05 17:32:17'),
(17, 'AT907', 'Lufthansa', 1, 'Dubai (DXB)', 'departure', '2025-08-05 12:30:00', '2025-08-05 13:14:00', 'On Time', 'A30', '2', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(18, 'AT257', 'Emirates', 2, 'Paris (CDG)', 'arrival', '2025-08-05 14:45:00', '2025-08-05 14:40:00', 'On Time', 'B24', '2', 'Airbus A350', '2025-08-05 17:32:17'),
(19, 'AT217', 'Air France', 3, 'Paris (CDG)', 'departure', '2025-08-05 16:30:00', '2025-08-05 17:11:00', 'On Time', 'B20', '1', 'Boeing 787 Dreamliner', '2025-08-05 17:32:17'),
(20, 'AT261', 'Air France', 1, 'Paris (CDG)', 'arrival', '2025-08-05 15:00:00', '2025-08-05 15:10:00', 'Boarding', 'B11', '2', 'Airbus A350', '2025-08-05 17:32:17'),
(21, 'AT459', 'Emirates', 3, 'New York (JFK)', 'departure', '2025-08-06 14:45:00', '2025-08-06 15:11:00', 'Departed', 'A2', '2', 'Boeing 787 Dreamliner', '2025-08-05 17:32:17'),
(22, 'AT921', 'Qatar Airways', 6, 'New York (JFK)', 'arrival', '2025-08-06 21:45:00', '2025-08-06 22:24:00', 'Scheduled', 'A4', '1', 'Airbus A320', '2025-08-05 17:32:17'),
(23, 'AT680', 'Air France', 5, 'Madrid (MAD)', 'departure', '2025-08-06 13:45:00', '2025-08-06 14:30:00', 'Scheduled', 'B3', '3', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(24, 'AT355', 'Lufthansa', 5, 'Madrid (MAD)', 'arrival', '2025-08-06 16:45:00', '2025-08-06 16:30:00', 'Boarding', 'C8', '2', 'Airbus A320', '2025-08-05 17:32:17'),
(25, 'AT512', 'Emirates', 6, 'Paris (CDG)', 'departure', '2025-08-06 18:30:00', '2025-08-06 19:10:00', 'Boarding', 'C19', '1', 'Airbus A320', '2025-08-05 17:32:17'),
(26, 'AT974', 'Air France', 3, 'Madrid (MAD)', 'arrival', '2025-08-06 06:30:00', '2025-08-06 06:29:00', 'Departed', 'A30', '3', 'Boeing 787 Dreamliner', '2025-08-05 17:32:17'),
(27, 'AT205', 'Air France', 4, 'Istanbul (IST)', 'departure', '2025-08-06 06:45:00', '2025-08-06 07:16:00', 'Arrived', 'B13', '3', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(28, 'AT262', 'Lufthansa', 6, 'Istanbul (IST)', 'arrival', '2025-08-06 11:00:00', '2025-08-06 11:23:00', 'On Time', 'C9', '2', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(29, 'AT473', 'Lufthansa', 6, 'Madrid (MAD)', 'departure', '2025-08-06 11:15:00', '2025-08-06 11:53:00', 'On Time', 'B7', '3', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(30, 'AT965', 'Emirates', 3, 'New York (JFK)', 'arrival', '2025-08-06 06:00:00', '2025-08-06 06:10:00', 'On Time', 'B7', '2', 'Airbus A320', '2025-08-05 17:32:17'),
(31, 'AT582', 'Iberia', 2, 'Istanbul (IST)', 'departure', '2025-08-07 11:15:00', '2025-08-07 11:13:00', 'On Time', 'B22', '2', 'Boeing 787 Dreamliner', '2025-08-05 17:32:17'),
(32, 'AT604', 'Air France', 3, 'Istanbul (IST)', 'arrival', '2025-08-07 06:00:00', '2025-08-07 06:28:00', 'On Time', 'C6', '3', 'Boeing 737-800', '2025-08-05 17:32:17'),
(33, 'AT544', 'Emirates', 6, 'Madrid (MAD)', 'departure', '2025-08-07 21:30:00', '2025-08-07 21:46:00', 'On Time', 'C30', '1', 'Boeing 737-800', '2025-08-05 17:32:17'),
(34, 'AT852', 'Lufthansa', 4, 'New York (JFK)', 'arrival', '2025-08-07 08:00:00', '2025-08-07 08:34:00', 'On Time', 'A29', '2', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(35, 'AT736', 'Qatar Airways', 2, 'Londres (LHR)', 'departure', '2025-08-07 19:30:00', '2025-08-07 19:51:00', 'Scheduled', 'B28', '3', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(36, 'AT772', 'Qatar Airways', 5, 'Istanbul (IST)', 'arrival', '2025-08-07 11:30:00', '2025-08-07 11:53:00', 'Boarding', 'B27', '3', 'Boeing 777-300ER', '2025-08-05 17:32:17'),
(37, 'AT997', 'British Airways', 5, 'Londres (LHR)', 'departure', '2025-08-07 14:15:00', '2025-08-07 14:45:00', 'On Time', 'C25', '3', 'Airbus A320', '2025-08-05 17:32:17'),
(38, 'AT376', 'Iberia', 5, 'Dakar (DSS)', 'arrival', '2025-08-07 16:15:00', '2025-08-07 16:20:00', 'On Time', 'B3', '2', 'Boeing 787 Dreamliner', '2025-08-05 17:32:17'),
(39, 'AT781', 'Turkish Airlines', 1, 'Istanbul (IST)', 'departure', '2025-08-07 06:30:00', '2025-08-07 06:45:00', 'On Time', 'B10', '2', 'Boeing 787 Dreamliner', '2025-08-05 17:32:17'),
(40, 'AT485', 'Emirates', 3, 'Dakar (DSS)', 'arrival', '2025-08-07 13:30:00', '2025-08-07 13:19:00', 'Delayed', 'C22', '3', 'Boeing 737-800', '2025-08-05 17:32:17');

-- --------------------------------------------------------

--
-- Table structure for table `job_application`
--

CREATE TABLE `job_application` (
  `id` int(11) NOT NULL,
  `job_offer_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(120) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `address` text NOT NULL,
  `birth_date` date NOT NULL,
  `nationality` varchar(50) NOT NULL,
  `education_level` varchar(100) NOT NULL,
  `experience_years` int(11) NOT NULL,
  `current_position` varchar(100) DEFAULT NULL,
  `skills` text DEFAULT NULL,
  `languages` text DEFAULT NULL,
  `cv_url` varchar(200) NOT NULL,
  `cover_letter_url` varchar(200) DEFAULT NULL,
  `diploma_url` varchar(200) DEFAULT NULL,
  `other_documents_url` varchar(500) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `motivation_letter` text DEFAULT NULL,
  `applied_at` datetime DEFAULT NULL,
  `reviewed_at` datetime DEFAULT NULL,
  `reviewed_by` int(11) DEFAULT NULL,
  `notes` text DEFAULT NULL,
  `tracking_code` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `job_application`
--

INSERT INTO `job_application` (`id`, `job_offer_id`, `user_id`, `first_name`, `last_name`, `email`, `phone`, `address`, `birth_date`, `nationality`, `education_level`, `experience_years`, `current_position`, `skills`, `languages`, `cv_url`, `cover_letter_url`, `diploma_url`, `other_documents_url`, `status`, `motivation_letter`, `applied_at`, `reviewed_at`, `reviewed_by`, `notes`, `tracking_code`) VALUES
(8, 2, NULL, 'sarah', 'bendouri', 'sarah.bendouri@gmail.com', '0664546424', 'asasaadadad', '2004-03-11', 'marocain', 'Bac+3', 2, 'aaaaaa', 'adazdazdazd', 'francais', 'uploads/cv_20250805_184403_8f96dc7c_tender_doc_20250805_040534_CCAGEMO_1 (1).pdf', 'uploads/cover_20250805_184403_b11d40d2_tender_doc_20250805_040534_CCAGEMO_1 (2).pdf', 'uploads/diploma_20250805_184403_11355147_25.jpg', NULL, 'accepted', 'aaaaaa', '2025-08-05 17:44:03', '2025-08-05 17:49:33', 4, '', '0KGB1IZ1');

-- --------------------------------------------------------

--
-- Table structure for table `job_offer`
--

CREATE TABLE `job_offer` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `reference` varchar(50) NOT NULL,
  `department` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `contract_type` varchar(50) NOT NULL,
  `experience_level` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `requirements` text NOT NULL,
  `benefits` text DEFAULT NULL,
  `salary_min` float DEFAULT NULL,
  `salary_max` float DEFAULT NULL,
  `publication_date` datetime DEFAULT NULL,
  `deadline` datetime NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `contact_person` varchar(100) DEFAULT NULL,
  `contact_email` varchar(120) DEFAULT NULL,
  `contact_phone` varchar(20) DEFAULT NULL,
  `created_by` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `job_offer`
--

INSERT INTO `job_offer` (`id`, `title`, `reference`, `department`, `location`, `contract_type`, `experience_level`, `description`, `requirements`, `benefits`, `salary_min`, `salary_max`, `publication_date`, `deadline`, `status`, `contact_person`, `contact_email`, `contact_phone`, `created_by`, `created_at`, `updated_at`) VALUES
(2, 'Ingénieur Aéronautique', 'EMP-NXSZRZ', 'Technique', 'Casablanca', 'CDI', 'Senior', 'Nous recherchons un ingénieur aéronautique expérimenté pour rejoindre notre équipe technique.', 'Diplôme d\'ingénieur en aéronautique, minimum 5 ans d\'expérience, connaissances en réglementation aérienne.', 'Assurance santé, tickets restaurant, formation continue', 25000, 35000, '2025-08-05 17:37:08', '2025-09-04 17:37:08', 'active', 'Service des Ressources Humaines', 'recrutement@onda.ma', '+212 516-135434', 4, '2025-08-05 17:37:08', '2025-08-05 17:37:08'),
(3, 'Contrôleur Aérien', 'EMP-09X5VF', 'Contrôle Aérien', 'Marrakech', 'CDI', 'Confirmé', 'Poste de contrôleur aérien à l\'aéroport de Marrakech-Ménara.', 'Formation en contrôle aérien, certification OACI, anglais courant, résistance au stress.', 'Assurance santé, primes de vol, horaires variables', 30000, 45000, '2025-08-05 17:37:08', '2025-08-30 17:37:08', 'active', 'Service des Ressources Humaines', 'recrutement@onda.ma', '+212 543-171613', 4, '2025-08-05 17:37:08', '2025-08-05 17:37:08'),
(4, 'Agent d\'escale', 'EMP-EWP0OL', 'Exploitation', 'Agadir', 'CDD', 'Débutant accepté', 'Agent d\'escale pour l\'accueil et l\'information des passagers.', 'Bac+2 minimum, anglais obligatoire, espagnol apprécié, bon relationnel.', 'Formation assurée, tickets restaurant, avantages voyage', 7000, 9000, '2025-08-05 17:37:08', '2025-08-20 17:37:08', 'active', 'Service des Ressources Humaines', 'recrutement@onda.ma', '+212 531-410832', 4, '2025-08-05 17:37:08', '2025-08-05 17:37:08'),
(5, 'Chef de Projet IT', 'EMP-FKAE9B', 'Systèmes d\'Information', 'Rabat', 'CDI', 'Expert', 'Direction des projets informatiques stratégiques de l\'office.', 'Diplôme d\'ingénieur en informatique, 10 ans d\'expérience dont 5 en gestion de projet, certification PMP un plus.', 'Salaire compétitif, voiture de fonction, télétravail partiel', 50000, 70000, '2025-08-05 17:37:08', '2025-09-14 17:37:08', 'active', 'Service des Ressources Humaines', 'recrutement@onda.ma', '+212 566-875192', 4, '2025-08-05 17:37:08', '2025-08-05 17:37:08'),
(6, 'Stagiaire en Communication', 'EMP-R5SKT2', 'Communication', 'Tanger', 'Stage', 'Étudiant', 'Stage en communication et relations publiques.', 'Étudiant en communication, maîtrise des réseaux sociaux, créativité.', 'Indemnité de stage, expérience enrichissante, possibilité d\'embauche', 3000, 3500, '2025-08-05 17:37:08', '2025-08-15 17:37:08', 'active', 'Service des Ressources Humaines', 'recrutement@onda.ma', '+212 598-423954', 4, '2025-08-05 17:37:08', '2025-08-05 17:37:08');

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `author` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `is_published` tinyint(1) DEFAULT NULL,
  `image_url` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `restaurant`
--

CREATE TABLE `restaurant` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `cuisine_type` varchar(50) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `is_open` tinyint(1) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `restaurant`
--

INSERT INTO `restaurant` (`id`, `name`, `city`, `cuisine_type`, `description`, `location`, `phone`, `rating`, `image_url`, `is_open`, `is_active`) VALUES
(5, 'La Table du Marché', 'Casablanca', 'Internationale', '', 'CMN', NULL, 2, NULL, 1, 1),
(6, 'Matsuri', 'Casablanca', 'Internationale', '', 'CMN', NULL, 4.8, NULL, 1, 1),
(7, 'La Table du Marché', 'Marrakech', 'Internationale', '', 'RAK', NULL, 4.5, NULL, 1, 1),
(8, 'Matsuri Sushi', 'Marrakech', 'Internationale', '', 'RAK', NULL, 4.8, NULL, 1, 1),
(9, 'Matsuri Sushi', 'Rabat', 'Italienne', '', 'RBA ', NULL, 4, NULL, 1, 1),
(10, 'Dar El Medina', 'Rabat', 'Marocaine', '', 'RBA', NULL, 4, NULL, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `shopping`
--

CREATE TABLE `shopping` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `opening_hours` varchar(100) DEFAULT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `is_open` tinyint(1) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `shopping`
--

INSERT INTO `shopping` (`id`, `name`, `city`, `type`, `description`, `location`, `opening_hours`, `image_url`, `is_open`, `is_active`) VALUES
(1, 'Morocco Mall', 'Casablanca', 'Centre Commercial', '', 'Boulevard de l\'Océan Atlantique, Casablanca', '10:00 - 22:00', NULL, 1, 1),
(2, 'Menara Mall', 'Marrakech', 'Centre Commercial', '', 'Avenue Mohammed VI, Marrakech', '10:00 - 22:00', NULL, 1, 1),
(3, 'Boutique Artisanat Marocain', 'Marrakech', 'Boutique', '', 'Aéroport Menara, zone départ', '08:00 - 21:00', NULL, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `transport`
--

CREATE TABLE `transport` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `type` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `description` text DEFAULT NULL,
  `price` float DEFAULT NULL,
  `contact_info` varchar(100) DEFAULT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `available` tinyint(1) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `transport`
--

INSERT INTO `transport` (`id`, `name`, `type`, `city`, `description`, `price`, `contact_info`, `image_url`, `available`, `is_active`) VALUES
(1, 'Grand Taxi – CMN', 'Taxi', 'Casablanca', '', 30, NULL, NULL, 1, 1),
(2, 'Navette AeroExpress', 'Navette', 'Marrakech', '', 30, NULL, NULL, 1, 1),
(3, 'ONCF Aéroport ↔ Casa Voyageurs', 'Train', 'Casablanca', '', 50, NULL, NULL, 1, 1),
(4, 'Bus Réseau Alsa Rabat', 'Bus', 'Rabat', '', 5, NULL, NULL, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password_hash` varchar(120) NOT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password_hash`, `is_admin`, `created_at`) VALUES
(4, 'admin', 'admin@onda.ma', 'pbkdf2:sha256:600000$4aYZtSqbqyQj5vh3$b5fff71c2ee50c53030e4670f4a24773f634028e4a755a7f3f03ce3691945e2e', 1, '2025-08-05 02:22:13'),
(5, 'user', 'user@onda.ma', 'pbkdf2:sha256:600000$7IGG7OmlceQRlAEI$2a009ff7ae261ef34d124f9ddbad28a3b86c1728538e767e2d096c14e9fecbf0', 0, '2025-08-05 02:22:13');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activity_log`
--
ALTER TABLE `activity_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `call_for_tenders`
--
ALTER TABLE `call_for_tenders`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `reference` (`reference`),
  ADD KEY `created_by` (`created_by`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`id`),
  ADD KEY `airport_id` (`airport_id`);

--
-- Indexes for table `job_application`
--
ALTER TABLE `job_application`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tracking_code` (`tracking_code`),
  ADD KEY `job_offer_id` (`job_offer_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `reviewed_by` (`reviewed_by`);

--
-- Indexes for table `job_offer`
--
ALTER TABLE `job_offer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `reference` (`reference`),
  ADD KEY `created_by` (`created_by`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `restaurant`
--
ALTER TABLE `restaurant`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `shopping`
--
ALTER TABLE `shopping`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport`
--
ALTER TABLE `transport`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activity_log`
--
ALTER TABLE `activity_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `airport`
--
ALTER TABLE `airport`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `call_for_tenders`
--
ALTER TABLE `call_for_tenders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `flight`
--
ALTER TABLE `flight`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `job_application`
--
ALTER TABLE `job_application`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `job_offer`
--
ALTER TABLE `job_offer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `restaurant`
--
ALTER TABLE `restaurant`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `shopping`
--
ALTER TABLE `shopping`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `transport`
--
ALTER TABLE `transport`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `activity_log`
--
ALTER TABLE `activity_log`
  ADD CONSTRAINT `activity_log_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `call_for_tenders`
--
ALTER TABLE `call_for_tenders`
  ADD CONSTRAINT `call_for_tenders_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`airport_id`) REFERENCES `airport` (`id`);

--
-- Constraints for table `job_application`
--
ALTER TABLE `job_application`
  ADD CONSTRAINT `job_application_ibfk_1` FOREIGN KEY (`job_offer_id`) REFERENCES `job_offer` (`id`),
  ADD CONSTRAINT `job_application_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `job_application_ibfk_3` FOREIGN KEY (`reviewed_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `job_offer`
--
ALTER TABLE `job_offer`
  ADD CONSTRAINT `job_offer_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
