// Visa Checker pour la page Documents ONDA
document.addEventListener('DOMContentLoaded', function() {
    const countrySelect = document.getElementById('countrySelect');
    const checkBtn = document.getElementById('checkVisaBtn');
    const resultDiv = document.getElementById('visaResult');

    // Données des pays et leurs exigences de visa pour le Maroc
    const visaData = {
        // Pays sans visa (séjour jusqu'à 90 jours)
        'no-visa': {
            countries: [
                'Algérie', 'Tunisie', 'Libye', 'Mauritanie', 'Mali', 'Sénégal', 'Burkina Faso', 'Niger', 'Côte d\'Ivoire', 'Guinée',
                'France', 'Allemagne', 'Espagne', 'Italie', 'Belgique', 'Pays-Bas', 'Suisse', 'Royaume-Uni', 'Irlande', 'Portugal',
                'États-Unis', 'Canada', 'Brésil', 'Argentine', 'Chili', 'Mexique',
                'Japon', 'Corée du Sud', 'Singapour', 'Hong Kong', 'Australie', 'Nouvelle-Zélande'
            ],
            duration: 'Séjour jusqu\'à 90 jours',
            requirements: [
                'Passeport valide (minimum 6 mois)',
                'Billet de retour ou de continuation',
                'Justificatifs d\'hébergement',
                'Ressources financières suffisantes'
            ]
        },
        // Pays nécessitant un visa
        'visa-required': {
            countries: [
                'Inde', 'Chine', 'Russie', 'Pakistan', 'Bangladesh', 'Afghanistan', 'Iran', 'Irak', 'Syrie',
                'Nigeria', 'Ghana', 'Kenya', 'Éthiopie', 'Somalie', 'Soudan', 'République démocratique du Congo',
                'Philippines', 'Indonésie', 'Thaïlande', 'Vietnam', 'Myanmar', 'Cambodge', 'Laos',
                'Ukraine', 'Biélorussie', 'Moldavie', 'Géorgie', 'Arménie', 'Azerbaïdjan'
            ],
            duration: 'Visa obligatoire',
            requirements: [
                'Demande de visa au consulat',
                'Passeport valide (minimum 6 mois)',
                'Photos d\'identité récentes',
                'Justificatifs financiers',
                'Réservation d\'hôtel confirmée',
                'Billet d\'avion aller-retour',
                'Assurance voyage'
            ]
        }
    };

    // Fonction pour vérifier le visa
    function checkVisa() {
        const selectedCountry = countrySelect.value;
        
        if (!selectedCountry) {
            showResult('error', 'Veuillez sélectionner votre pays de résidence.');
            return;
        }

        let visaStatus = null;
        let requirements = [];
        let duration = '';

        // Chercher dans les pays sans visa
        if (visaData['no-visa'].countries.includes(selectedCountry)) {
            visaStatus = 'no-visa';
            requirements = visaData['no-visa'].requirements;
            duration = visaData['no-visa'].duration;
        }
        // Chercher dans les pays avec visa obligatoire
        else if (visaData['visa-required'].countries.includes(selectedCountry)) {
            visaStatus = 'visa-required';
            requirements = visaData['visa-required'].requirements;
            duration = visaData['visa-required'].duration;
        }
        // Pays non trouvé - visa probablement requis
        else {
            visaStatus = 'visa-required';
            requirements = visaData['visa-required'].requirements;
            duration = 'Visa probablement requis';
        }

        showResult(visaStatus, '', requirements, duration);
    }

    // Fonction pour afficher le résultat
    function showResult(status, message = '', requirements = [], duration = '') {
        let html = '';
        
        if (status === 'error') {
            html = `
                <div class="alert alert-warning" role="alert">
                    <i class="fas fa-exclamation-triangle me-2"></i>
                    ${message}
                </div>
            `;
        } else if (status === 'no-visa') {
            html = `
                <div class="visa-result-card no-visa">
                    <div class="result-header">
                        <i class="fas fa-check-circle"></i>
                        <h4>Aucun visa requis</h4>
                    </div>
                    <div class="result-body">
                        <p class="duration"><strong>${duration}</strong></p>
                        <h5>Documents requis :</h5>
                        <ul class="requirements-list">
                            ${requirements.map(req => `<li><i class="fas fa-check me-2"></i>${req}</li>`).join('')}
                        </ul>
                        <div class="result-note">
                            <i class="fas fa-info-circle me-2"></i>
                            <small>Vérifiez toujours les conditions actuelles avant votre voyage.</small>
                        </div>
                    </div>
                </div>
            `;
        } else if (status === 'visa-required') {
            html = `
                <div class="visa-result-card visa-required">
                    <div class="result-header">
                        <i class="fas fa-passport"></i>
                        <h4>Visa obligatoire</h4>
                    </div>
                    <div class="result-body">
                        <p class="duration"><strong>${duration}</strong></p>
                        <h5>Documents requis :</h5>
                        <ul class="requirements-list">
                            ${requirements.map(req => `<li><i class="fas fa-document-text me-2"></i>${req}</li>`).join('')}
                        </ul>
                        <div class="result-actions">
                            <a href="#" class="btn btn-primary btn-sm">
                                <i class="fas fa-external-link-alt me-1"></i>
                                Consulat du Maroc
                            </a>
                            <a href="#" class="btn btn-outline-primary btn-sm">
                                <i class="fas fa-phone me-1"></i>
                                Nous contacter
                            </a>
                        </div>
                        <div class="result-note">
                            <i class="fas fa-clock me-2"></i>
                            <small>Délai de traitement : 5 à 15 jours ouvrables.</small>
                        </div>
                    </div>
                </div>
            `;
        }

        resultDiv.innerHTML = html;
        resultDiv.style.display = 'block';
        
        // Scroll vers le résultat
        resultDiv.scrollIntoView({ 
            behavior: 'smooth', 
            block: 'nearest' 
        });
    }

    // Event listeners
    if (checkBtn) {
        checkBtn.addEventListener('click', checkVisa);
    }

    if (countrySelect) {
        countrySelect.addEventListener('change', function() {
            if (resultDiv.style.display === 'block') {
                resultDiv.style.display = 'none';
            }
        });
    }

    // Styles CSS pour les résultats (ajoutés dynamiquement)
    const style = document.createElement('style');
    style.textContent = `
        .visa-result-card {
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            animation: slideIn 0.3s ease-out;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .visa-result-card.no-visa {
            border: 2px solid #27ae60;
        }

        .visa-result-card.visa-required {
            border: 2px solid #f39c12;
        }

        .result-header {
            padding: 20px;
            color: white;
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .visa-result-card.no-visa .result-header {
            background: linear-gradient(135deg, #27ae60, #229954);
        }

        .visa-result-card.visa-required .result-header {
            background: linear-gradient(135deg, #f39c12, #e67e22);
        }

        .result-header i {
            font-size: 1.5rem;
        }

        .result-header h4 {
            margin: 0;
            font-weight: 600;
        }

        .result-body {
            padding: 25px;
            background: white;
        }

        .duration {
            font-size: 1.1rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 20px;
            text-align: center;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 10px;
        }

        .requirements-list {
            list-style: none;
            padding: 0;
            margin-bottom: 20px;
        }

        .requirements-list li {
            padding: 8px 0;
            color: #2c3e50;
            display: flex;
            align-items: center;
        }

        .requirements-list i {
            color: #27ae60;
            margin-right: 10px;
        }

        .visa-result-card.visa-required .requirements-list i {
            color: #f39c12;
        }

        .result-actions {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
            flex-wrap: wrap;
        }

        .result-note {
            display: flex;
            align-items: center;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
            color: #6c757d;
        }

        .result-note i {
            color: #17a2b8;
        }

        @media (max-width: 768px) {
            .result-actions {
                flex-direction: column;
            }
            
            .result-actions .btn {
                width: 100%;
            }
        }
    `;
    document.head.appendChild(style);
});
