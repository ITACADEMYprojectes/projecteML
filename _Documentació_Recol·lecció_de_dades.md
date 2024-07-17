# Exemple de documentació del Procés de Recol·lecció de Dades per al Projecte de Predicció de Despesa Anual de la Botiga de Roba
## 1. Fonts

**Identificació de Fonts:**
- Base de dades interna del CRM

**Descripció de les Fonts:**
- La base de dades CRM conté registres de transaccions, dades de clients i informació sobre les connexions a la web i l'aplicació que el departament d'IT captura mitjançant una 
## 2. Mètodes de recol·lecció de dades

**Procediments i Eines:**
- Exportació programada en format CSV, emmagatzemada en un repositori de GitHub diàriament. Aquesta tasca la fa el departament d'IT.

**Freqüència de Recol·lecció:**
- Diàriament
  
**Scripts de Descàrrega:****S:cr

```python

import pandas as pd

csv_url = "https://raw.githubusercontent.com/ITACADEMYprojectes/projecteML/main/Ecommerce_Customers.csv"
df = pd.read_csv(csv_url)
print(df.## 3. Format i Estructura de les Dades

**Tipus de Dades:**
- Numèrics: `Avg. Session Length`, `Time on App`, `Time on Website`, `Length of Membership`, `Yearly Amount Spent`
- Categòric: `Email`, `Address`, `Avatar`

**Format d'Emmagatzematge:**
- Dades tabulars emmagatzemades en fitx
  er## 4. Limitacions de les dades

- Diferents Temps d'Actualització: Les dades d'ús de l'app i del lloc web poden ser recol·lectades i actualitzades al CRM en moments diferents
.## 5. Consideracions sobre Dades Sensibles

**Tipus de Dades Sensibles:**
- Informació Personal Identificable (PII): `Email`, `Address`
- Informació Financera Sensible: `Yearly Amount Spent`
- Dades Comportamentals Sensibles:`Avg. Session Length`, `Time on App`, `Time on Website`, `Length of Membership`

**Mesures de Protecció:**
- **Anonimització i Pseudonimització:**
  - S'aplicaran hash per a l'email i la substitució per codis per a Address.
- **Accés Restringit:**
  - Accés a dades sensibles restringit només a personal autoritzat amb necessitat de conèixer aquestes dades per a fins específics del projecte.
- **Compliment de Regulacions:**
  - Compliment amb la GDRPdel proyecto.
- **Cumplimiento de Regulaciones:**
  - Cumplimiento con la GDRPlaciones:**
  - Cumplimiento con la GDRP
print(df.info())
