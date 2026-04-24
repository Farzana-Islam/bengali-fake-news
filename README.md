# bengali-fake-news-dataset
One of the first publicly available fake news datasets for the Bengali language, compiled by scraping local newspapers.

## Dataset
- Collected from Bengali local news sources
- Labeled for fake/real classification
- Built to address the lack of NLP resources for underrepresented languages
- 
## Methods
- Scraped Bengali news from local newspapers
- Labeled articles as fake/real
- Built a Bengali stemmer (`parser.py`) using rule-based suffix stripping
- Corpus builder (`corpus_builder.py`) converts CSV data into text files
- Trained ML classifiers: Naïve Bayes, Logistic Regression, Random Forest
- Best accuracy: 85% with Random Forest
  
## Related Work
- Farzana Islam et al. (2020). Bengali Fake News Detection. 
  IEEE International Conference on Intelligent Systems.

## Usage
If you use this dataset, please cite the IEEE IS 2020 paper above.

## Author
Farzana Islam  
[LinkedIn](https://linkedin.com/in/farzanaa-islam) · [Portfolio](https://farzana-islam.github.io/portal)
