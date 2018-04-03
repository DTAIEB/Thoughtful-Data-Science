import pandas
wnid_to_urls = pandas.read_csv('/Users/dtaieb/Downloads/fall11_urls.txt', sep='\t', names=["wnid", "url"],
                     header=0, error_bad_lines=False, warn_bad_lines=False, encoding="ISO-8859-1")
wnid_to_urls['wnid'] = wnid_to_urls['wnid'].apply(lambda x: x.split("_")[0])
wnid_to_urls = wnid_to_urls.dropna()

wnid_to_words = pandas.read_csv('/Users/dtaieb/Downloads/words.txt', sep='\t', names=["wnid", "description"],
                     header=0, error_bad_lines=False, warn_bad_lines=False, encoding="ISO-8859-1")
wnid_to_words = wnid_to_words.dropna()
