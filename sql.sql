
DROP TABLE IF EXISTS utilisateur;
DROP TABLE IF EXISTS mots_de_passe;


CREATE TABLE utilisateur (
    id_utilisateur INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50),
    password VARCHAR(255),
    role VARCHAR(50),
    est_actif INT,
    nom VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE mots_de_passe (
    id_mot_de_passe INT AUTO_INCREMENT PRIMARY KEY,
    nom_site VARCHAR(100),
    mot_de_passe VARCHAR(255),
    date_ajout DATETIME,
    id_utilisateur INT,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur)
);



INSERT INTO utilisateur (id_utilisateur, login, password, role, est_actif, nom, email) VALUES
(1, 'admin',
    'pbkdf2:sha256:600000$VQJnbWSkoyzKReNL$c510c74149e9eea7d47fd1242064dd8bcc2968555f41c107ba0da395ab160de2',
    'ROLE_admin', 1, 'admin', 'admin@admin.fr'),
(2, 'client',
    'pbkdf2:sha256:600000$ABCsJQjDITt5Fx0k$8997971258697acd2c995ed1d5d3fb7806110e4effe562866930134273dd56b2',
    'ROLE_client', 1, 'client', 'client@client.fr'),
(3, 'client2',
    'pbkdf2:sha256:600000$Cba5KP6zIM04OMWA$e7fe8b4513ff81bf761464d12d95e1d5cbafec2dfba932ffb9de74faa6bd3eb0',
    'ROLE_client', 1, 'client2', 'client2@client2.fr');






INSERT INTO mots_de_passe (nom_site, mot_de_passe, date_ajout, id_utilisateur) VALUES
('Site 1', 'mot_de_passe_1', NOW(), 1),
('Site 2', 'mot_de_passe_2', NOW(), 1),
('Site 3', 'mot_de_passe_3', NOW(), 2),
('Site 4', 'mot_de_passe_4', NOW(), 2),
('Site 5', 'mot_de_passe_5', NOW(), 3);
