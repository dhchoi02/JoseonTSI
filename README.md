# Joseon Dynasty Bureaucrat Career Dataset

This repository contains datasets used for analyzing the career trajectories of bureaucrats during the Joseon Dynasty (1392-1910 CE) of Korea. The data is derived from two primary historical sources:

1. **The Annals of the Joseon Dynasty** (_Joseon Wangjo Sillok_) - A comprehensive chronological record of the dynasty's governmental affairs, recognized as a UNESCO Memory of the World.
2. **The Bangmok** - A catalog listing successful candidates of the civil service examination (_Gwageo_).

## Datasets

### bangmok_passers.csv

Contains records of 14,638 individuals who passed the Mungwa (Literary) civil service examination.

| Column           | Description                                         |
| ---------------- | --------------------------------------------------- |
| bangmok_id       | Unique identifier for each exam passer              |
| name_han         | Name in Classical Chinese characters                |
| name_kor         | Name in Korean                                      |
| family_clan      | Clan affiliation (surname + ancestral seat)         |
| birth_year       | Year of birth                                       |
| death_year       | Year of death                                       |
| origin_city      | City of origin                                      |
| origin_province  | Province of origin                                  |
| reign_king       | Reigning king at the time of examination            |
| exam_year        | Year of passing the examination                     |
| exam_type        | Type of examination (siknyeonsi/byeolsi/jeunggwangsi) |
| exam_rank        | Ranking among successful candidates                 |
| bangmok_url      | URL to the Bangmok database entry                   |
| family_status    | Social status (yangban/commoner)                    |
| kinship          | Family relationship information (JSON dictionary)   |
| appearance_count | Number of appearances in the Annals                 |
| exam_id          | Identifier for the examination session              |
| cohort_size      | Total number of passers in the same exam session    |
| tsi              | Total Success Index score                           |

### career_records/

Career records extracted from the Annals, documenting appointments and positions held by bureaucrats. Split into multiple files for size management.

| Column        | Description                                  |
| ------------- | -------------------------------------------- |
| bangmok_id    | Links to bangmok_passers.csv                 |
| sillok_id     | Identifier used in the Annals                |
| gye           | Administrative category                      |
| sa            | Department/ministry                          |
| jik           | Specific position                            |
| office_name   | Name of the office held                      |
| office_grade  | Bureaucratic rank (1-18, where 1 is highest) |
| relative_date | Date relative to the king's reign            |
| solar_date    | Converted Gregorian calendar date            |

### annals_articles/

Articles from the Annals of the Joseon Dynasty. Split by reign king prefix (first 3 characters of article_id) for size management.

| Column     | Description                                        |
| ---------- | -------------------------------------------------- |
| article_id | Unique article identifier (prefix indicates reign) |
| title      | Article title                                      |
| lunar_date | Original lunar calendar date                       |
| text_kor   | Korean translation                                 |
| text_han   | Original Classical Chinese text                    |

### person_id_map.csv

Mapping between identifiers used in the Bangmok and the Annals (10,685 entries).

| Column     | Description              |
| ---------- | ------------------------ |
| bangmok_id | Identifier in Bangmok    |
| sillok_id  | Identifier in the Annals |

### gyeyu_node.csv

Network nodes representing 405 individuals involved in Prince Suyang's Revolt of 1453 (Gyeyu year). This event led to the dethronement of King Danjong and Suyang's rise to the throne.

| Column | Description                                           |
| ------ | ----------------------------------------------------- |
| index  | Node index                                            |
| id     | Person name in Korean                                 |
| label  | Romanized name                                        |
| group  | Post-revolt fate group (decorated/purged/neutral)    |

### gyeyu_edge.csv

Network edges representing 2,072 direct interactions recorded in the Annals during the two-month period surrounding Prince Suyang's Revolt.

| Column | Description                          |
| ------ | ------------------------------------ |
| id     | Edge identifier                      |
| type   | Edge type (Directed)                 |
| source | Source person (Korean name)          |
| target | Target person (Korean name)          |
| date   | Date of interaction                  |
| weight | Edge weight                          |

## Usage

### Preparing Data

The career records and annals articles are split into multiple files for storage. Use `prepare_data.py` to merge them:

```bash
python prepare_data.py
```

This will create:

- `career_records.csv` - Merged career records (247,432 entries)
- `annals_articles.csv` - Merged annals articles (372,012 entries)

## Data Sources

- **Annals of the Joseon Dynasty** (annals_articles): https://sillok.history.go.kr/
- **Career Records** (career_records): https://www.data.go.kr/data/15053645/fileData.do
- **Bangmok** (bangmok_passers): http://people.aks.ac.kr/index.aks
