# Random project

Le projet consiste en un script Python qui permet d'encoder et de décoder des messages sous une forme spécifique et de publier ces messages sur Twitter. 

## Usage

Cloner le repo

```bash
git clone "repo URL"
```

Définir les clés API Twitter dans un fichier .env (qui contient API_KEY, API_KEY_SECRET, ACCESS_TOKEN, et ACCESS_TOKEN_SECRET, BEARER_TOKEN).
Ne pas oublier d'activer READ/WRITE dans le dashboard de X Developer

Pour executer : 

```bash
chmod +x npi.py
./npi.py -e "Phrase qui sera encodée puis tweetée"
```

**Do not forget to create an X Developer account to get your credentials and you need API V2**

## Encoder avec la commande "dc"

- Le texte que vous voulez encoder est d'abord inversé. Cela permet de traiter les caractères dans l'ordre inverse avant de les convertir en un nombre.
- L'encodage avec la commande "dc" dans ce projet consiste à transformer un texte en un nombre ASCII, puis à formater ce nombre sous une commande qui peut être traitée par l'outil dc (un calculatrice de commande en ligne de commande).
- Ces valeurs ASCII sont ensuite utilisées pour générer un nombre unique en les combinant. Cela se fait en multipliant successivement chaque valeur ASCII par 256 et en les additionnant
- Voir Notation Polonaise Inversée (NPI)

**Exemple pratique :**

Supposons que vous ayez le texte **"Hello"** :

1. Inversion du texte : "olleH". 
2. Conversion en ASCII des caractères inversés :
    - o → 111
    - l → 108
    - l → 108
    - e → 101
    - H → 72
3. Combinaison des valeurs ASCII : 
    - 111 * 256^4 + 108 * 256^3 + 108 * 256^2 + 101 * 256^1 + 72 * 256^0 = 478560413000
4. Ajout du prefix et du suffix
    - prefix = "echo '[q]sa[ln0=aln256%Pln256/snlbx]sb"
    - suffix = "snlbxq'|dc"
